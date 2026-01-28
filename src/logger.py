from src.models import Alert


def write_alerts_log(path: str, alerts: list[Alert]):
    file = open(path, "w", encoding="utf-8")
    file.write("timestamp\tseverity\tvital\tvalue\tmessage\n")

    for a in alerts:
        file.write(f"{a.timestamp}\t{a.severity}\t{a.vital}\t{a.value}\t{a.message}\n")

    file.close()
