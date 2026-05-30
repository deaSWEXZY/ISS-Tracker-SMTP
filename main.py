import requests
from datetime import datetime
from smtplib import SMTP
import time
import server_config as cfg  # Keeps configuration clean


def is_iss_here(iss_lat, iss_lng):
    """Returns True if ISS is within +5/-5 degrees of our position."""
    return (cfg.MY_LAT - 5) <= iss_lat <= (cfg.MY_LAT + 5) and (cfg.MY_LONG - 5) <= iss_lng <= (cfg.MY_LONG + 5)


def is_nighttime(sun_rise, sun_set, curr_hour):
    """Returns True if the current UTC hour is during darkness."""
    return not (sun_rise <= curr_hour <= sun_set)


print("Starting ISS Tracker System...")

while True:
    try:
        # 1. Get Live ISS Location (Correct API Endpoint)
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()
        iss_data = iss_response.json()

        iss_latitude = float(iss_data["iss_position"]["latitude"])
        iss_longitude = float(iss_data["iss_position"]["longitude"])

        # 2. Get Sunrise/Sunset Times (UTC)
        sun_params = {"lat": cfg.MY_LAT, "lng": cfg.MY_LONG, "formatted": 0}
        sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_params)
        sun_response.raise_for_status()
        sun_data = sun_response.json()

        sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

        # 3. Get Current Hour in UTC (Matches API Timezone)
        current_hour_utc = datetime.utcnow().hour

        # 4. Run calculations using our functions
        if is_iss_here(iss_latitude, iss_longitude) and is_nighttime(sunrise_hour, sunset_hour, current_hour_utc):
            print("ISS is overhead and it's dark! Sending email...")
            with SMTP(cfg.SMTP_SERVER, cfg.SMTP_PORT) as server:
                server.starttls()
                server.login(cfg.MY_EMAIL, cfg.MY_EMAIL_PASSWORD)
                server.sendmail(
                    from_addr=cfg.MY_EMAIL,
                    to_addrs=cfg.RECEIVER_EMAIL,
                    msg="Subject: Look Up! 🚀\n\nThe ISS is close and visible!"
                )
            print("Mail sent successfully.")
        else:
            print(f"Checked. Position: ({iss_latitude}, {iss_longitude}). Conditions not met.")

    except requests.RequestException as error:
        print(f"Bro something is wrong with your  connection....\nError: {error}")
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")

    print("Sleeping for 60 seconds...\n")
    time.sleep(60)