def compute_omega(cvar: float, psi: float, alpha: float = 0.45, beta: float = 0.55):
    """
    Cálculo real do índice antifrágil Ω.
    Ω = α(1 - CVaR) + βΨ
    """
    return (alpha * (1 - cvar)) + (beta * psi)

if __name__ == "__main__":
    print("Ω:", compute_omega(7.2e-4, 0.994))
