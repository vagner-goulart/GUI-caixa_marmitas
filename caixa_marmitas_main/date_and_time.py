from datetime import datetime, date # 'date' is being imported here for debugging purposes only. TODO: remove later

today_data = datetime.now()
today_data = date(2021, 1, 30) # this is being used here for debugging purposes only. TODO: remove later

dias_semana_PT = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
dias_semana_ENG = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

dias_semana_ENG_to_PT_dict = {
    'Monday': 'SEGUNDA',
    'Tuesday': 'TERÇA',
    'Wednesday': 'QUARTA',
    'Thursday': 'QUINTA',
    'Friday': 'SEXTA',
    'Saturday': 'SÁBADO',
    'Sunday': 'DOMINGO'
    }

def get_today_weekday():
    return today_data.strftime('%A')

def get_formated_day_info():
    return today_data.strftime('%d/%m/%Y - %H:%M')

def get_current_time():
    return datetime.now().strftime('%H:%M')

def get_today_date():
    return today_data.strftime('%d/%m/%y')

def get_today_weekday_in_PT():
    return dias_semana_ENG_to_PT_dict[get_today_weekday()]
