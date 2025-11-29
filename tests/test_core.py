from core.omega_engine import compute_omega

def test_omega_range():
    omega = compute_omega(0.0007, 0.994)
    assert 0.9 < omega < 1.2
