from dataclasses import dataclass


@dataclass
class VitalSample:
    timestamp: str
    hr_bpm: int
    spo2_pct: int
    temp_f: float
    sys_mmhg: int
    dia_mmhg: int


@dataclass
class Alert:
    timestamp: str
    vital: str
    severity: str   # "WARNING" or "CRITICAL"
    value: str
    message: str


@dataclass
class EvaluationResult:
    status: str     # "NORMAL", "WARNING", "CRITICAL"
    alerts: list[Alert]
