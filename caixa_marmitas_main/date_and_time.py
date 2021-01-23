from datetime import datetime

today_data = datetime.now()

def get_today_weekday():
    return today_data.strftime('%A')

