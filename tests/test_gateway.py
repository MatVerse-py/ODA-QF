from gateway.decision_loop import compute_all_metrics

def test_metrics():
    omega, psi, cvar = compute_all_metrics()
    assert omega > 0
    assert psi > 0
    assert cvar >= 0
