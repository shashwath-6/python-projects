"""from datetime import datetime , timezone
#print(datetime.datetime.now())
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo
utc_now = datetime.now(timezone.utc)
francetime = zoneinfo.ZoneInfo("Europe/Paris")
france = utc_now.astimezone(francetime)
print(france)"""
from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# Get the current time in UTC
utc_now = datetime.now(timezone.utc)

# Define the time zone for France
francetime = zoneinfo.ZoneInfo("Europe/Paris")

# Convert the current time to France's time zone
france_time = utc_now.astimezone(francetime)

# Print the converted time
print(france_time)

