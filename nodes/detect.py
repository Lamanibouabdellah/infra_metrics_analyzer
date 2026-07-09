from models.state import InfraState
from rules.thresholds import THRESHOLDS


def _severity(value: float, levels: dict[str, float]) -> str | None:
    for level in ("high", "medium", "low"):
        if value >= levels[level]:
            return level
    return None


def detect(state: InfraState) -> dict:
    """Detect anomalies by comparing max metric values against thresholds."""

    data = state["raw_data"]
    anomalies = []

    for metric, levels in THRESHOLDS.items():
        max_value = max(getattr(s, metric) for s in data)
        severity = _severity(max_value, levels)

        if severity:
            anomalies.append({
                "metric":      metric,
                "value":       max_value,
                "threshold":   levels[severity],
                "severity":    severity,
                "description": f"{metric} reached {max_value} (threshold: {levels[severity]})",
            })

    return {"anomalies": anomalies}