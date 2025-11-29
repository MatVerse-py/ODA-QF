from statistics import mean
from typing import Iterable


def _quantile(values, alpha: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("Losses cannot be empty")
    position = alpha * (len(ordered) - 1)
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return (1 - weight) * ordered[lower] + weight * ordered[upper]


def estimate_cvar(losses: Iterable[float], alpha: float = 0.95):
    """
    Cálculo real do CVaR (Conditional Value at Risk).
    """
    losses = list(losses)
    var = _quantile(losses, alpha)
    tail = [loss for loss in losses if loss >= var]
    return float(mean(tail))
