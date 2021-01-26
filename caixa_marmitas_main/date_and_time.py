from datetime import datetime, date # 'date' is being imported here for debugging purposes only. TODO: remove later

today_data = datetime.now()

def get_today_weekday():
    return today_data.strftime('%A')

def get_formated_day_info():
    return today_data.strftime('%d/%m/%Y - %H:%M')

def get_current_time():
    return datetime.now().strftime('%H:%M')

def get_today_date():
    return today_data.strftime('%d/%m/%y')
