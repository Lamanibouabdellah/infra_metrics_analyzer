from datetime import datetime
from typing import Annotated, Literal
from pydantic import BaseModel, BeforeValidator, Field


def _validate_iso8601(v: str) -> str:
    datetime.fromisoformat(v)
    return v

ISODatetime = Annotated[str, BeforeValidator(_validate_iso8601)]


class ServiceStatus(BaseModel):
    database: Literal["online", "degraded", "offline"]
    api_gateway: Literal["online", "degraded", "offline"]
    cache: Literal["online", "degraded", "offline"]


class Snapshot(BaseModel):
    """Single metrics snapshot — validated entry from input JSON."""

    timestamp: ISODatetime
    cpu_usage: float = Field(ge=0, le=100)
    memory_usage: float = Field(ge=0, le=100)
    latency_ms: float = Field(ge=0)
    disk_usage: float = Field(ge=0, le=100)
    network_in_kbps: float = Field(ge=0)
    network_out_kbps: float = Field(ge=0)
    io_wait: float = Field(ge=0)
    thread_count: int = Field(ge=0)
    active_connections: int = Field(ge=0)
    error_rate: float = Field(ge=0, le=1)
    uptime_seconds: int = Field(ge=0)
    temperature_celsius: float
    power_consumption_watts: float = Field(ge=0)
    service_status: ServiceStatus