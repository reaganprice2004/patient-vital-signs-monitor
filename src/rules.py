def _mk(vital: str, severity: str, value_str: str, message: str):
    return (vital, severity, value_str, message)


def rule_hr(hr_bpm: int):
    if hr_bpm < 40:
        return _mk("Heart Rate", "CRITICAL", f"{hr_bpm} bpm", "Heart rate is dangerously low (< 40 bpm).")
    if hr_bpm > 130:
        return _mk("Heart Rate", "CRITICAL", f"{hr_bpm} bpm", "Heart rate is dangerously high (> 130 bpm).")

    if 40 <= hr_bpm < 50:
        return _mk("Heart Rate", "WARNING", f"{hr_bpm} bpm", "Heart rate is low (40–49 bpm).")
    if 110 < hr_bpm <= 130:
        return _mk("Heart Rate", "WARNING", f"{hr_bpm} bpm", "Heart rate is high (111–130 bpm).")

    return None


def rule_spo2(spo2_pct: int):
    if spo2_pct < 90:
        return _mk("SpO₂", "CRITICAL", f"{spo2_pct}%", "Oxygen saturation is critically low (< 90%).")

    if 90 <= spo2_pct <= 92:
        return _mk("SpO₂", "WARNING", f"{spo2_pct}%", "Oxygen saturation is borderline low (90–92%).")

    return None


def rule_temp(temp_f: float):
    if temp_f < 95.0:
        return _mk("Temperature", "CRITICAL", f"{temp_f:.1f}°F", "Temperature is critically low (< 95°F).")
    if temp_f > 103.0:
        return _mk("Temperature", "CRITICAL", f"{temp_f:.1f}°F", "Temperature is critically high (> 103°F).")

    if 95.0 <= temp_f <= 96.5:
        return _mk("Temperature", "WARNING", f"{temp_f:.1f}°F", "Temperature is low (95–96.5°F).")
    if 100.4 <= temp_f <= 103.0:
        return _mk("Temperature", "WARNING", f"{temp_f:.1f}°F", "Fever range (100.4–103°F).")

    return None


def rule_bp(sys_mmhg: int, dia_mmhg: int):
    if sys_mmhg >= 180 or dia_mmhg >= 120:
        return _mk(
            "Blood Pressure",
            "CRITICAL",
            f"{sys_mmhg}/{dia_mmhg} mmHg",
            "Blood pressure is critically high (>=180 systolic or >=120 diastolic).",
        )

    if (140 <= sys_mmhg <= 179) or (90 <= dia_mmhg <= 119):
        return _mk(
            "Blood Pressure",
            "WARNING",
            f"{sys_mmhg}/{dia_mmhg} mmHg",
            "Blood pressure is elevated (140–179 systolic or 90–119 diastolic).",
        )

    return None
