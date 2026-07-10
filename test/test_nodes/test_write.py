from infra_metrics_analyzer.nodes.write import _service_status_summary


def test_worst_status_offline_wins(snapshot_normal, snapshot_critical):
    state = {"raw_data": [snapshot_normal, snapshot_critical]}
    summary = _service_status_summary(state)

    assert "database" in summary["offline"]
    assert "api_gateway" in summary["degraded"]
    assert "cache" in summary["degraded"]


def test_all_online(snapshot_normal):
    state = {"raw_data": [snapshot_normal]}
    summary = _service_status_summary(state)

    assert summary["online"] == ["database", "api_gateway", "cache"]
    assert summary["degraded"] == []
    assert summary["offline"] == []