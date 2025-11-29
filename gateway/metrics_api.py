from fastapi import FastAPI
from gateway.decision_loop import compute_all_metrics

app = FastAPI()

@app.get("/metrics")
def metrics():
    omega, psi, cvar = compute_all_metrics()
    return {
        "omega": float(omega),
        "psi": float(psi),
        "cvar": float(cvar)
    }
