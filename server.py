import uvicorn
from fastapi import FastAPI
from gateway.decision_loop import compute_all_metrics

app = FastAPI()

@app.get("/metrics")
def get_metrics():
    omega, psi, cvar = compute_all_metrics()
    return {
        "omega": float(omega),
        "psi": float(psi),
        "cvar": float(cvar)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
