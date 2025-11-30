import pytest

try:
    from Crypto.Hash import keccak  # type: ignore
except ImportError:
    pytest.skip("Crypto keccak not available", allow_module_level=True)

from identity.merkle_identity import merkle_proof, merkle_root, verify_merkle_proof


def _reference_merkle_root(leaves):
    hashed = [keccak.new(data=leaf.encode(), digest_bits=256).digest() for leaf in leaves]
    while len(hashed) > 1:
        next_level = []
        for i in range(0, len(hashed), 2):
            left = hashed[i]
            right = hashed[i + 1] if i + 1 < len(hashed) else left
            if left > right:
                left, right = right, left
            next_level.append(keccak.new(data=left + right, digest_bits=256).digest())
        hashed = next_level
    return hashed[0].hex()


def test_merkle_root_matches_keccak_reference():
    leaves = ["alice", "bob", "charlie", "david"]
    expected_root = _reference_merkle_root(leaves)
    assert merkle_root(leaves) == expected_root


def test_merkle_proof_reconstructs_root():
    leaves = ["alice", "bob", "charlie", "david", "eve"]
    target_index = 2
    proof = merkle_proof(leaves, target_index)
    expected_root = _reference_merkle_root(leaves)
    assert verify_merkle_proof(leaves[target_index], proof, expected_root)


def test_merkle_root_rejects_empty_input():
    with pytest.raises(ValueError):
        merkle_root([])


def test_merkle_proof_rejects_out_of_bounds_index():
    leaves = ["only-one"]
    with pytest.raises(IndexError):
        merkle_proof(leaves, 1)
