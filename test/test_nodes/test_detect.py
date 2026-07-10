from infra_metrics_analyzer.nodes.detect import detect, _severity


def test_severity_high():
    assert _severity(95.0, {"low": 70.0, "medium": 80.0, "high": 90.0}) == "high"


def test_severity_medium():
    assert _severity(75.0, {"low": 70.0, "medium": 80.0, "high": 90.0}) == "low"


def test_severity_none():
    assert _severity(50.0, {"low": 70.0, "medium": 80.0, "high": 90.0}) is None


def test_detect_critical_snapshot(snapshot_critical):
    result = detect({"raw_data": [snapshot_critical]})
    metrics = {a["metric"] for a in result["anomalies"]}

    assert "cpu_usage" in metrics
    assert "memory_usage" in metrics
    assert "error_rate" in metrics


def test_detect_no_anomaly(snapshot_normal):
    result = detect({"raw_data": [snapshot_normal]})

    assert result["anomalies"] == []


def test_detect_anomaly_severity(snapshot_critical):
    result = detect({"raw_data": [snapshot_critical]})
    cpu_anomaly = next(a for a in result["anomalies"] if a["metric"] == "cpu_usage")

    assert cpu_anomaly["severity"] == "high"
    assert cpu_anomaly["value"] == 99