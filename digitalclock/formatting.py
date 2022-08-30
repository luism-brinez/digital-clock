def format_time(hours = 0, minutes = 0, seconds = 0, format = "12H"):
    if minutes >= 0 and minutes < 10: this_minutes = f'0{minutes}'
    else: this_minutes = f'{minutes}'
    if seconds >= 0 and seconds < 10: this_seconds = f'0{seconds}'
    else: this_seconds = f'{seconds}'
    if format == "12H":
        if hours == 0: this_hours = f'{12}'
        elif hours >= 1 and hours < 10: this_hours = f'0{hours}'
        elif hours >= 13 and hours < 22: this_hours = f'0{hours - 12}'
        elif hours >= 22 and hours <24: this_hours = f'{hours - 12}' 
        else: this_hours = f'{hours}'
        if hours >= 12 and hours < 24: return f'{this_hours}:{this_minutes}:{this_seconds} PM'
        return f'{this_hours}:{this_minutes}:{this_seconds} AM'
    else:
        if hours >= 0 and hours < 10: this_hours = f'0{hours}'
        else: this_hours = f'{hours}'
        return f'{this_hours}:{this_minutes}:{this_seconds}'
    
"""This function receives a i18n object as parameter 
to return the localized text for month"""
def format_date(year, month, day, i18n):
    month = i18n.t(f'lang.month.{month}')   
    return  f'{month}  {day}  {year}'

def format_digits (number):
    if number >= 0 and number < 10:
        return f'0{number}'
    else:  return f'{number}'

