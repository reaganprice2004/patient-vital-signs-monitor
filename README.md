# Patient Vital Signs Monitoring & Alert System

A Python-based patient monitoring system that analyzes time-series vital signs data and generates interpretable, severity-based alerts using clinically inspired thresholds. This project emphasizes safety, transparency, and system-level decision logic rather than black-box machine learning.

## Overview

Continuous monitoring of patient vital signs is critical in healthcare environments, where timely and interpretable alerts can directly impact patient safety. This project simulates a clinical monitoring system that evaluates multiple physiological signals and determines patient status at each time step.

The system classifies patient condition as **NORMAL**, **WARNING**, or **CRITICAL**, generates human-readable alerts with explanations, and logs events for traceability.

## Features

- Processes time-series vital signs data
- Monitors four core physiological signals:
  - Heart Rate (bpm)
  - Oxygen Saturation (SpO₂ %)
  - Body Temperature (°F)
  - Blood Pressure (systolic / diastolic, mmHg)
- Applies clinically inspired threshold rules
- Generates severity-based alerts (**WARNING**, **CRITICAL**)
- Determines overall patient status per sample
- Logs alerts with timestamps and explanations
- Produces summary statistics and a patient status timeline

## Example Output

```
=== Vital Signs Monitoring Summary ===
Samples processed: 80
Total alerts: 8
WARNING alerts: 4
CRITICAL alerts: 4

Status timeline (per sample):
  NORMAL: 72
  WARNING: 4
  CRITICAL: 4
```

Alerts are also written to a log file for review and auditing:

```
data/alerts.log
```

## Project Structure

```
patient-vital-signs-monitor/
  data/
    sample_vitals.csv
    alerts.log
  src/
    __init__.py
    main.py
    models.py
    rules.py
    monitor.py
    io_utils.py
    logger.py
```

### Key Components

- **rules.py** — Clinical threshold logic for each vital sign
- **monitor.py** — Core monitoring engine and patient status evaluation
- **io_utils.py** — CSV ingestion and simulated data generation
- **logger.py** — Alert logging utilities
- **models.py** — Data models for samples, alerts, and evaluation results

## How to Run

From the project root:

```bash
python -m src.main
```

The program will:
1. Generate sample vital sign data (if not already present)
2. Evaluate each sample using clinical rules
3. Print a monitoring summary
4. Write alerts to `data/alerts.log`

## Design Philosophy

This project intentionally avoids opaque machine learning models in favor of:
- Rule-based, interpretable logic
- Explicit safety thresholds
- Transparent decision-making

Such approaches are commonly preferred in safety-critical healthcare systems where explainability, validation, and traceability are essential.

## Technologies Used

- Python
- Rule-based decision logic
- Time-series data processing
- Modular system design

## Potential Extensions

- Visualization of vital sign trends
- Configurable thresholds via external configuration files
- Integration with real sensor data streams
- Alert prioritization or escalation logic
- Unit testing and continuous integration (CI)

## Author

Reagan Price
