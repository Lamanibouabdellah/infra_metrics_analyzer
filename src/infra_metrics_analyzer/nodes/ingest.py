import json
from infra_metrics_analyzer.models.input import Snapshot
from infra_metrics_analyzer.models.state import InfraState
from infra_metrics_analyzer.settings import settings


def ingest(state: InfraState) -> dict:
    """Load and validate snapshots from the input JSON file."""

    with open(settings.input_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    return {"raw_data": [Snapshot.model_validate(entry) for entry in raw]}