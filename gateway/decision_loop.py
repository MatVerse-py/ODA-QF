import random
from core.omega_engine import compute_omega
from core.psi_index import compute_psi
from core.cvar_monitor import estimate_cvar

def compute_all_metrics():
    psi = compute_psi(0.99, 0.98, 1.0)
    losses = [random.gauss(0, 0.00095) for _ in range(50000)]
    cvar = estimate_cvar(losses)
    omega = compute_omega(cvar, psi)
    return omega, psi, cvar

if __name__ == "__main__":
    Ω, Ψ, CVaR = compute_all_metrics()
    print(f"Ω={Ω:.6f} | Ψ={Ψ:.6f} | CVaR={CVaR:.6f}")
