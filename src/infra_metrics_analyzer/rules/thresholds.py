THRESHOLDS: dict[str, dict[str, float]] = {
    "cpu_usage": {
        "low":    70.0,
        "medium": 80.0,
        "high":   90.0,
    },
    "memory_usage": {
        "low":    70.0,
        "medium": 80.0,
        "high":   90.0,
    },
    "latency_ms": {
        "low":    150.0,
        "medium": 200.0,
        "high":   300.0,
    },
    "disk_usage": {
        "low":    70.0,
        "medium": 80.0,
        "high":   90.0,
    },
    "io_wait": {
        "low":    5.0,
        "medium": 8.0,
        "high":   12.0,
    },
    "error_rate": {
        "low":    0.03,
        "medium": 0.05,
        "high":   0.10,
    },
    "temperature_celsius": {
        "low":    65.0,
        "medium": 75.0,
        "high":   85.0,
    },
}