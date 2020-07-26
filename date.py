from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+5))
dt = datetime(2019, 12, 5, 5, 30, 0, tzinfo=JST)
print(dt)
