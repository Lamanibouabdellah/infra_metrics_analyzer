from infra_metrics_analyzer.nodes.analyse import analyse


def test_analyse_averages(snapshot_normal, snapshot_critical):
    state = {"raw_data": [snapshot_normal, snapshot_critical]}
    result = analyse(state)["insights"]

    assert result["max_cpu_usage"] == 99
    assert result["max_memory_usage"] == 92
    assert result["average_latency_ms"] == round((130 + 384) / 2, 2)
    assert result["uptime_seconds"] == 361800


def test_analyse_error_rate_average(snapshot_normal, snapshot_critical):
    state = {"raw_data": [snapshot_normal, snapshot_critical]}
    result = analyse(state)["insights"]

    assert result["error_rate"] == round((0.02 + 0.13) / 2, 4)