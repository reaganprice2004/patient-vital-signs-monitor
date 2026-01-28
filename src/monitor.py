from src.models import VitalSample, Alert, EvaluationResult
from src.rules import rule_hr, rule_spo2, rule_temp, rule_bp


def evaluate_sample(sample: VitalSample) -> EvaluationResult:
    alerts = []

    hits = [
        rule_hr(sample.hr_bpm),
        rule_spo2(sample.spo2_pct),
        rule_temp(sample.temp_f),
        rule_bp(sample.sys_mmhg, sample.dia_mmhg),
    ]

    for hit in hits:
        if hit is not None:
            vital, severity, value_str, message = hit
            alerts.append(
                Alert(
                    timestamp=sample.timestamp,
                    vital=vital,
                    severity=severity,
                    value=value_str,
                    message=message,
                )
            )

    status = "NORMAL"
    for a in alerts:
        if a.severity == "CRITICAL":
            status = "CRITICAL"
            break
        if a.severity == "WARNING":
            status = "WARNING"

    return EvaluationResult(status=status, alerts=alerts)


def run_monitor(samples: list[VitalSample]):
    statuses = []
    all_alerts = []

    for s in samples:
        result = evaluate_sample(s)
        statuses.append(result.status)
        all_alerts.extend(result.alerts)

    return statuses, all_alerts


def summarize_alerts(alerts: list[Alert]):
    summary = {"total": len(alerts), "warning": 0, "critical": 0, "by_vital": {}}

    for a in alerts:
        if a.severity == "WARNING":
            summary["warning"] += 1
        elif a.severity == "CRITICAL":
            summary["critical"] += 1

        if a.vital not in summary["by_vital"]:
            summary["by_vital"][a.vital] = 0
        summary["by_vital"][a.vital] += 1

    return summary
def summarize_statuses(statuses: list[str]):
    summary = {"NORMAL": 0, "WARNING": 0, "CRITICAL": 0}

    for s in statuses:
        if s in summary:
            summary[s] += 1

    return summary


























