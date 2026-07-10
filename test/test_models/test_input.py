import pytest
from pydantic import ValidationError
from infra_metrics_analyzer.models.input import Snapshot


def test_valid_snapshot(snapshot_normal):
    assert snapshot_normal.cpu_usage == 55


def test_invalid_cpu_above_100():
    with pytest.raises(ValidationError):
        Snapshot.model_validate({
            "timestamp": "2023-10-01T12:00:00Z",
            "cpu_usage": 110, "memory_usage": 65, "latency_ms": 130,
            "disk_usage": 60, "network_in_kbps": 1200, "network_out_kbps": 1100,
            "io_wait": 3, "thread_count": 145, "active_connections": 50,
            "error_rate": 0.02, "uptime_seconds": 360000,
            "temperature_celsius": 60, "power_consumption_watts": 250,
            "service_status": {"database": "online", "api_gateway": "online", "cache": "online"},
        })


def test_invalid_error_rate_above_1():
    with pytest.raises(ValidationError):
        Snapshot.model_validate({
            "timestamp": "2023-10-01T12:00:00Z",
            "cpu_usage": 55, "memory_usage": 65, "latency_ms": 130,
            "disk_usage": 60, "network_in_kbps": 1200, "network_out_kbps": 1100,
            "io_wait": 3, "thread_count": 145, "active_connections": 50,
            "error_rate": 1.5, "uptime_seconds": 360000,
            "temperature_celsius": 60, "power_consumption_watts": 250,
            "service_status": {"database": "online", "api_gateway": "online", "cache": "online"},
        })


def test_invalid_iso8601():
    with pytest.raises(ValidationError):
        Snapshot.model_validate({
            "timestamp": "not-a-date",
            "cpu_usage": 55, "memory_usage": 65, "latency_ms": 130,
            "disk_usage": 60, "network_in_kbps": 1200, "network_out_kbps": 1100,
            "io_wait": 3, "thread_count": 145, "active_connections": 50,
            "error_rate": 0.02, "uptime_seconds": 360000,
            "temperature_celsius": 60, "power_consumption_watts": 250,
            "service_status": {"database": "online", "api_gateway": "online", "cache": "online"},
        })


def test_invalid_service_status():
    with pytest.raises(ValidationError):
        Snapshot.model_validate({
            "timestamp": "2023-10-01T12:00:00Z",
            "cpu_usage": 55, "memory_usage": 65, "latency_ms": 130,
            "disk_usage": 60, "network_in_kbps": 1200, "network_out_kbps": 1100,
            "io_wait": 3, "thread_count": 145, "active_connections": 50,
            "error_rate": 0.02, "uptime_seconds": 360000,
            "temperature_celsius": 60, "power_consumption_watts": 250,
            "service_status": {"database": "unknown", "api_gateway": "online", "cache": "online"},
        })