import json
from datetime import datetime, timezone
from infra_metrics_analyzer.models.output import InfraReport
from infra_metrics_analyzer.models.state import InfraState
from infra_metrics_analyzer.settings import settings

_STATUS_PRIORITY = {"offline": 2, "degraded": 1, "online": 0}
_SERVICES = ("database", "api_gateway", "cache")


def _service_status_summary(state: InfraState) -> dict:
    worst: dict[str, str] = {s: "online" for s in _SERVICES}
    for snapshot in state["raw_data"]:
        for service in _SERVICES:
            current = getattr(snapshot.service_status, service)
            if _STATUS_PRIORITY[current] > _STATUS_PRIORITY[worst[service]]:
                worst[service] = current
    summary: dict[str, list[str]] = {"online": [], "degraded": [], "offline": []}
    for service, status in worst.items():
        summary[status].append(service)
    return summary


def write(state: InfraState) -> dict:
    """Validate the full report and write it to the output file."""

    report = InfraReport(
        timestamp=datetime.now(timezone.utc).isoformat(),
        insights=state["insights"],
        anomalies=state["anomalies"],
        recommendations=state["recommendations"],
        service_status_summary=_service_status_summary(state),
    )

    with open(settings.output_file, "w", encoding="utf-8") as f:
        json.dump(report.model_dump(), f, indent=2, ensure_ascii=False)

    return {"service_status_summary": report.service_status_summary.model_dump()}