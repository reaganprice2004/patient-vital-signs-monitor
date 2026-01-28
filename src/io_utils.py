import csv
import random

from src.models import VitalSample


def read_vitals_csv(path: str):
    """
    Read patient vital sign samples from a CSV file and return
    a list of VitalSample objects.
    """
    samples = []

    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sample = VitalSample(
                timestamp=row["timestamp"],
                hr_bpm=int(row["hr_bpm"]),
                spo2_pct=int(row["spo2_pct"]),
                temp_f=float(row["temp_f"]),
                sys_mmhg=int(row["sys_mmhg"]),
                dia_mmhg=int(row["dia_mmhg"]),
            )
            samples.append(sample)

    return samples


def generate_sample_csv(path: str, n: int = 80):
    """
    Generate a CSV file with simulated patient vital signs.
    Includes both normal values and injected warning/critical events.
    """
    random.seed(7)

    fieldnames = [
        "timestamp",
        "hr_bpm",
        "spo2_pct",
        "temp_f",
        "sys_mmhg",
        "dia_mmhg",
    ]

    def normal_hr():
        return random.randint(60, 95)

    def normal_spo2():
        return random.randint(95, 100)

    def normal_temp():
        return round(random.uniform(97.2, 99.2), 1)

    def normal_sys():
        return random.randint(105, 130)

    def normal_dia():
        return random.randint(65, 85)

    rows = []
    for i in range(n):
        rows.append(
            {
                "timestamp": f"t{i:03d}",
                "hr_bpm": normal_hr(),
                "spo2_pct": normal_spo2(),
                "temp_f": normal_temp(),
                "sys_mmhg": normal_sys(),
                "dia_mmhg": normal_dia(),
            }
        )

    # Inject warning and critical events
    if n >= 40:
        rows[10]["spo2_pct"] = 92     # WARNING
        rows[12]["spo2_pct"] = 88     # CRITICAL
        rows[18]["hr_bpm"] = 45       # WARNING
        rows[22]["hr_bpm"] = 145      # CRITICAL
        rows[28]["temp_f"] = 100.8    # WARNING
        rows[30]["temp_f"] = 104.2    # CRITICAL
        rows[36]["sys_mmhg"] = 155    # WARNING
        rows[38]["sys_mmhg"] = 182    # CRITICAL
        rows[38]["dia_mmhg"] = 121    # CRITICAL

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
