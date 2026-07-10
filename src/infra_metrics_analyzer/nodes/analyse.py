from infra_metrics_analyzer.models.state import InfraState


def analyse(state: InfraState) -> dict:
    """Compute aggregate insights from validated snapshots."""

    data = state["raw_data"]

    return {"insights": {
        "average_latency_ms": round(sum(s.latency_ms for s in data) / len(data), 2),
        "max_cpu_usage":      max(s.cpu_usage for s in data),
        "max_memory_usage":   max(s.memory_usage for s in data),
        "error_rate":         round(sum(s.error_rate for s in data) / len(data), 4),
        "uptime_seconds":     max(s.uptime_seconds for s in data),
    }}