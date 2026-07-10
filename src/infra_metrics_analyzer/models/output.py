from typing import Literal
from pydantic import BaseModel
from infra_metrics_analyzer.models.input import ISODatetime


class Insights(BaseModel):
    average_latency_ms: float
    max_cpu_usage:      float
    max_memory_usage:   float
    error_rate:         float
    uptime_seconds:     int


class Anomaly(BaseModel):
    metric:      str
    value:       float
    threshold:   float
    severity:    Literal["low", "medium", "high"]
    description: str


class Recommendation(BaseModel):
    id:               str
    action:           str
    target:           str
    parameters:       dict
    benefit_estimate: str


class ServiceStatusSummary(BaseModel):
    online:   list[str]
    degraded: list[str]
    offline:  list[str]


class InfraReport(BaseModel):
    """Final validated report written to output file."""

    timestamp:              ISODatetime
    insights:               Insights
    anomalies:              list[Anomaly]
    recommendations:        list[Recommendation]
    service_status_summary: ServiceStatusSummary