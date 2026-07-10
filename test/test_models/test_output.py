import pytest
from pydantic import ValidationError
from infra_metrics_analyzer.models.output import InfraReport


_VALID_REPORT = {
    "timestamp": "2023-10-01T12:00:00Z",
    "insights": {
        "average_latency_ms": 156.0,
        "max_cpu_usage": 99.0,
        "max_memory_usage": 92.0,
        "error_rate": 0.03,
        "uptime_seconds": 360000,
    },
    "anomalies": [{
        "metric": "cpu_usage",
        "value": 99.0,
        "threshold": 90.0,
        "severity": "high",
        "description": "cpu_usage reached 99.0",
    }],
    "recommendations": [{
        "id": "cpu_scale_up",
        "action": "scale_up",
        "target": "cpu",
        "parameters": {"count": 2},
        "benefit_estimate": "Reduce CPU by 20%",
    }],
    "service_status_summary": {
        "online": ["cache"],
        "degraded": ["api_gateway"],
        "offline": ["database"],
    },
}


def test_valid_report():
    report = InfraReport.model_validate(_VALID_REPORT)
    assert report.insights.max_cpu_usage == 99.0


def test_invalid_severity():
    data = _VALID_REPORT.copy()
    data["anomalies"] = [{**_VALID_REPORT["anomalies"][0], "severity": "critical"}]
    with pytest.raises(ValidationError):
        InfraReport.model_validate(data)


def test_invalid_timestamp():
    data = {**_VALID_REPORT, "timestamp": "not-a-date"}
    with pytest.raises(ValidationError):
        InfraReport.model_validate(data)