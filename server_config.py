from os import environ

# --- Configuration Coordinates ---
MY_LAT = 51.507351
MY_LONG = -0.127758

# --- Server/SMTP Setup ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# --- Secured Account Credentials ---
MY_EMAIL = environ.get("MY_TRACKER_EMAIL")
RECEIVER_EMAIL = environ.get("RECEIVER_EMAIL")
MY_EMAIL_PASSWORD = environ.get("SECRET_PASS_ISS_NOTIF")