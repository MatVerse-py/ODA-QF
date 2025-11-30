"""Merkle tree utilities compatible with Solidity keccak256 hashing."""
from __future__ import annotations

from typing import Iterable, List

try:
    from Crypto.Hash import keccak
except ImportError as exc:  # pragma: no cover - makes dependency error explicit
    raise ImportError(
        "pycryptodome is required for keccak256 hashing; install with `pip install pycryptodome`."
    ) from exc


def _keccak256(data: bytes) -> bytes:
    """Return the Keccak-256 digest for *data*.

    This matches Solidity's ``keccak256`` opcode and should be used for every
    Merkle tree operation to remain compatible with on-chain verification.
    """

    return keccak.new(data=data, digest_bits=256).digest()


def _hash_pair(a: bytes, b: bytes) -> bytes:
    """Hash an ordered pair of nodes using Keccak-256.

    The pair is sorted to make the hash order independent, mirroring common
    Solidity implementations that sort sibling nodes before hashing.
    """

    if a > b:
        a, b = b, a
    return _keccak256(a + b)


def _build_level(nodes: List[bytes]) -> List[bytes]:
    """Build the next level of the Merkle tree from ``nodes``."""

    next_level: List[bytes] = []
    for i in range(0, len(nodes), 2):
        left = nodes[i]
        right = nodes[i + 1] if i + 1 < len(nodes) else left
        next_level.append(_hash_pair(left, right))
    return next_level


def merkle_root(leaves: Iterable[str]) -> str:
    """Compute the Merkle root for ``leaves`` using Keccak-256.

    Args:
        leaves: Iterable of leaf payloads. Each item is encoded as UTF-8 and
            hashed with Keccak-256 before tree construction.

    Returns:
        Root hash as a lowercase hex string without ``0x`` prefix.

    Raises:
        ValueError: If no leaves are provided.
    """

    leaf_list = list(leaves)
    if not leaf_list:
        raise ValueError("Empty leaves")

    layer = [_keccak256(leaf.encode()) for leaf in leaf_list]
    while len(layer) > 1:
        layer = _build_level(layer)
    return layer[0].hex()


def merkle_proof(leaves: Iterable[str], index: int) -> List[str]:
    """Generate a Merkle proof for the leaf at ``index``.

    Args:
        leaves: Iterable of leaf payloads.
        index: Position of the leaf in the provided iterable.

    Returns:
        List of sibling node hashes as lowercase hex strings.

    Raises:
        IndexError: If ``index`` is outside the leaf range.
        ValueError: If ``leaves`` is empty.
    """

    leaf_list = list(leaves)
    if not leaf_list:
        raise ValueError("Empty leaves")
    if index < 0 or index >= len(leaf_list):
        raise IndexError("Index out of range")

    layer = [_keccak256(leaf.encode()) for leaf in leaf_list]
    proof: List[str] = []
    idx = index

    while len(layer) > 1:
        next_level: List[bytes] = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i + 1] if i + 1 < len(layer) else left

            if i == idx - (idx % 2):
                sibling = right if idx % 2 == 0 else left
                proof.append(sibling.hex())

            next_level.append(_hash_pair(left, right))
        layer = next_level
        idx //= 2

    return proof


def verify_merkle_proof(leaf: str, proof: Iterable[str], expected_root: str) -> bool:
    """Verify a Merkle proof against an expected root.

    Args:
        leaf: Leaf payload to verify.
        proof: Iterable of sibling node hashes as hex strings.
        expected_root: Expected Merkle root, with or without ``0x`` prefix.

    Returns:
        ``True`` if the proof resolves to ``expected_root`` using Keccak-256
        hashing, ``False`` otherwise.
    """

    computed = _keccak256(leaf.encode())
    for sibling_hex in proof:
        computed = _hash_pair(computed, bytes.fromhex(sibling_hex))

    normalized_expected = expected_root.lower()
    if normalized_expected.startswith("0x"):
        normalized_expected = normalized_expected[2:]

    return computed.hex() == normalized_expected
