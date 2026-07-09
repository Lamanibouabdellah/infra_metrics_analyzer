import json
from models.input import Snapshot
from models.state import InfraState
from settings import settings


def ingest(state: InfraState) -> dict:
    """Load and validate snapshots from the input JSON file."""

    with open(settings.input_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    snapshots = [Snapshot.model_validate(entry) for entry in raw]

    return {"raw_data": snapshots}