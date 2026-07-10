import pytest
from infra_metrics_analyzer.models.input import Snapshot


@pytest.fixture
def snapshot_normal():
    return Snapshot.model_validate({
        "timestamp": "2023-10-01T12:00:00Z",
        "cpu_usage": 55, "memory_usage": 65, "latency_ms": 130,
        "disk_usage": 60, "network_in_kbps": 1200, "network_out_kbps": 1100,
        "io_wait": 3, "thread_count": 145, "active_connections": 50,
        "error_rate": 0.02, "uptime_seconds": 360000,
        "temperature_celsius": 60, "power_consumption_watts": 250,
        "service_status": {"database": "online", "api_gateway": "online", "cache": "online"},
    })


@pytest.fixture
def snapshot_critical():
    return Snapshot.model_validate({
        "timestamp": "2023-10-01T13:00:00Z",
        "cpu_usage": 99, "memory_usage": 92, "latency_ms": 384,
        "disk_usage": 97, "network_in_kbps": 2500, "network_out_kbps": 2000,
        "io_wait": 14, "thread_count": 150, "active_connections": 130,
        "error_rate": 0.13, "uptime_seconds": 361800,
        "temperature_celsius": 89, "power_consumption_watts": 380,
        "service_status": {"database": "offline", "api_gateway": "degraded", "cache": "degraded"},
    })