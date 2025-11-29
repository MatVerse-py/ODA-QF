def compute_psi(completeness: float, consistency: float, traceability: float):
    """
    Cálculo real do índice Ψ.
    Ψ = 0.4C + 0.3K + 0.3T
    """
    return 0.4 * completeness + 0.3 * consistency + 0.3 * traceability
