# ISS-Tracker-SMTP 🚀

A modular Python script that tracks the International Space Station (ISS) in real-time. If the ISS passes within a +-5 degree bounding box of your geographic coordinates and it is dark outside, the system automatically triggers a secure email notification.

## Features
* **Real-Time API Integration:** Consumes live geospatial telemetry from the OpenNotify ISS API.
* **Dynamic Day/Night Calculation:** References the Sunrise-Sunset API using localized coordinates to ensure alerts only fire during tracking visibility windows (darkness).
* **Decoupled Architecture:** Separates system configurations and secret credentials (`server_config.py`) from core execution logic (`main.py`).
* **Secure Environment Routing:** Utilizes environment variables (`os.environ`) to safe-guard sensitive SMTP application passwords and mail relays.

## Stack
* **Language:** Python 3
* **Libraries:** `requests` (API operations), `smtplib` (SMTP protocol connection), `time`, `datetime`

---
Thank you for checking out the repository!

Created by *Swexzy.*
