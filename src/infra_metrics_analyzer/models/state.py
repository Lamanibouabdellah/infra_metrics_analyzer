from typing import TypedDict
from infra_metrics_analyzer.models.input import Snapshot


class InfraState(TypedDict):
    """Shared state propagated across all LangGraph nodes."""

    raw_data:               list[Snapshot]
    insights:               dict
    anomalies:              list[dict]
    recommendations:        list[dict]
    service_status_summary: dict