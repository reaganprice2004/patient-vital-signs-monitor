import os

from src.io_utils import read_vitals_csv, generate_sample_csv
from src.monitor import run_monitor, summarize_alerts, summarize_statuses
from src.logger import write_alerts_log


def main():
    # project_root = folder that contains src/ and data/
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    data_dir = os.path.join(project_root, "data")
    os.makedirs(data_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, "sample_vitals.csv")
    log_path = os.path.join(data_dir, "alerts.log")

    if not os.path.exists(csv_path):
        generate_sample_csv(csv_path, n=80)
        print(f"Generated sample data at: {csv_path}")

    samples = read_vitals_csv(csv_path)
    statuses, alerts = run_monitor(samples)
    status_summary = summarize_statuses(statuses)

    write_alerts_log(log_path, alerts)

    summary = summarize_alerts(alerts)

    print("\n=== Vital Signs Monitoring Summary ===")
    print(f"Samples processed: {len(samples)}")
    print(f"Total alerts: {summary['total']}")
    print(f"WARNING alerts: {summary['warning']}")
    print(f"CRITICAL alerts: {summary['critical']}")
    print("\nStatus timeline (per sample):")
    print(f"  NORMAL: {status_summary['NORMAL']}")
    print(f"  WARNING: {status_summary['WARNING']}")
    print(f"  CRITICAL: {status_summary['CRITICAL']}")


    print("\nAlerts by vital:")
    for vital in summary["by_vital"]:
        print(f"  - {vital}: {summary['by_vital'][vital]}")

    print(f"\nAlerts log written to: {log_path}")

    if len(alerts) > 0:
        print("\nFirst 10 alerts:")
        for a in alerts[:10]:
            print(f"{a.timestamp} | {a.severity} | {a.vital} | {a.value} | {a.message}")
    else:
        print("\nNo alerts detected.")


if __name__ == "__main__":
    main()

