import hashlib

def merkle_root(leaves):
    if len(leaves) == 1:
        return leaves[0]

    new = []
    for i in range(0, len(leaves), 2):
        left = leaves[i]
        right = leaves[i+1] if i+1 < len(leaves) else left
        new.append(hashlib.sha256((left + right).encode()).hexdigest())

    return merkle_root(new)
