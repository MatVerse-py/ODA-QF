"""Merkle root generation aligned with Solidity keccak256."""

from identity.merkle_identity import merkle_root as solidity_merkle_root


def generate_merkle_root(leaves):
    """Return a Merkle root compatible with on-chain verification.

    Leaves are treated as raw payload strings (not pre-hashed). They are hashed
    with Keccak-256 and combined in an ordered, pairwise fashion to match
    Solidity's ``keccak256`` behavior.
    """

    return solidity_merkle_root(leaves)


def merkle_root(leaves):
    """Backward-compatible wrapper for existing scripts."""

    return generate_merkle_root(leaves)
