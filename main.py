from datetime import datetime, timedelta
dt_obj = datetime(2023, 4, 1, 15, 30, 0)
future_dt = dt_obj + timedelta(days=7)
print(future_dt.strftime("%Y-%m-%d %H:%M;%S"))