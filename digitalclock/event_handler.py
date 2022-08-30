from configparser import ConfigParser
import platform
import tabs_setup
import menu_setup
from main import App
import config_manager
import options_manager
from tkinter import *
from formatting import * 
from clock import Clock
import i18n as lang 
try:
    import winsound
except:
    import os

__resource_path = '../digitalclock/resources'
__window: App 
__themes  = options_manager.get_themes()
__timezones  = options_manager.get_timezones()
__time_formats  = options_manager.get_time_formats()
__clock: Clock
__cfg: ConfigParser
__is_alarm_setted: bool
__selected_lang: StringVar
__selected_theme: StringVar
__selected_timezone: StringVar
__selected_time_format: StringVar



def setup(window: App, cfg: ConfigParser, clock: Clock):
    global __cfg, __is_alarm_setted, __clock, __window
    __window = window
    __is_alarm_setted = False
    __clock = clock
    __cfg = cfg
    __set_windows_protocols(window)

def setup_alarm_events():
    __set_saved_alarm()
    tabs_setup.bind_alarm_button(__alarm_control, __set_alarm)

def setup_clock_events():
    __clock.bind_to(__update_clock_state)

def setup_menu_events():
    __widgets_data_binding()

def __widgets_data_binding():
    global __selected_lang, __selected_theme, __selected_time_format, __selected_timezone
    __selected_lang, __selected_theme, __selected_time_format, __selected_timezone = menu_setup.get_selected_menu_data()
    __selected_lang.trace('w', __change_language)
    __selected_theme.trace('w', __change_theme)
    __selected_timezone.trace('w', __change_timezone)
    __selected_time_format.trace('w', __change_time_format)

def __alarm_control(pressed: str, data: str):
    data = int(data)
    if pressed == 'hour_minus':
        if data == 0: tabs_setup.set_alarm_hour(format_digits(23))
        else: tabs_setup.set_alarm_hour(format_digits(data-1))
    elif pressed == 'minute_minus':
        if data == 0: tabs_setup.set_alarm_minute(format_digits(59)) 
        else: tabs_setup.set_alarm_minute(format_digits(data - 1))  
    elif pressed == 'second_minus':
        if data == 0: tabs_setup.set_alarm_second(format_digits(59))   
        else: tabs_setup.set_alarm_second(format_digits(data - 1))
    elif pressed == 'hour_plus':
        if data == 23: tabs_setup.set_alarm_hour(format_digits(0)) 
        else: tabs_setup.set_alarm_hour(format_digits(data + 1)) 
    elif pressed == 'minute_plus':
        if data == 59: tabs_setup.set_alarm_minute(format_digits(0))  
        else: tabs_setup.set_alarm_minute(format_digits(data + 1))  
    elif pressed == 'second_plus':
        if data == 59: tabs_setup.set_alarm_second(format_digits(0))  
        else: tabs_setup.set_alarm_second(format_digits(data + 1)) 

def __set_alarm():
    global __is_alarm_setted
    __is_alarm_setted = True
    hour, minute, second = tabs_setup.get_alarm_hour(), tabs_setup.get_alarm_minute(), tabs_setup.get_alarm_second()
    __cfg.set('alarm', 'alarm_hour', hour)
    __cfg.set('alarm', 'alarm_minute', minute)
    __cfg.set('alarm', 'alarm_second', second)
    tabs_setup.set_alarm_info(f'{lang.t("lang.alarm_info_text")}: {format_time(int(hour), int(minute), int(second), __selected_time_format.get())}')

def __set_saved_alarm():
    if __cfg.get('alarm', 'alarm_hour') != '':
        tabs_setup.set_alarm_hour(__cfg.get('alarm', 'alarm_hour'))
        tabs_setup.set_alarm_minute(__cfg.get('alarm', 'alarm_minute'))
        tabs_setup.set_alarm_second(__cfg.get('alarm', 'alarm_second'))
        __set_alarm()

def __on_closing():
    global __clock, __window
    __clock.stop()
    config_manager.save_config(__cfg)
    print("CLOCK STOPPED")
    __window.destroy()

def __change_language(*args):
    global __cfg
    print("Selected language: ", __selected_lang.get())
    __cfg.set('main', 'language', __selected_lang.get())
    lang.set('locale', __selected_lang.get())
    __window.config_window() 
    menu_setup.update()
    tabs_setup.update_alarm_frame(__themes[__selected_theme.get()], lang)
    if __is_alarm_setted:
        __set_alarm()

def __change_theme(*args):
    global __cfg
    print("Selected theme: ", __selected_theme.get())
    __cfg.set('main', 'theme', __selected_theme.get())
    __window.config_window()
    tabs_setup.update_alarm_frame(__themes[__selected_theme.get()], lang)
    tabs_setup.update_clock_frame(__themes[__selected_theme.get()], __selected_timezone.get())
    if __is_alarm_setted:
        __set_alarm()

def __change_timezone(*args):
    global __cfg, __clock
    print("Selected timezone: ", __selected_timezone.get())
    __cfg.set('main', 'timezone', __selected_timezone.get())
    tabs_setup.update_clock_frame(__themes[__selected_theme.get()], __selected_timezone.get())
    __clock.change_timezone(__timezones[__selected_timezone.get()])

def __change_time_format(self, *args):
    global __cfg
    #This change is handle with the data binding at clock callbacks
    print("Selected time format: ", __selected_time_format.get())
    __cfg.set('main', 'time_format', __selected_time_format.get())
    if __is_alarm_setted:
        __set_alarm()

def __set_windows_protocols(window: App):
    window.protocol("WM_DELETE_WINDOW", __on_closing)

def __update_clock_state():
    global __clock
    tabs_setup.set_clock_time(format_time(__clock.hour, __clock.min, __clock.sec, __selected_time_format.get()))
    tabs_setup.set_clock_date(format_date(__clock.year, __clock.month, __clock.day, lang))
    if __is_alarm_setted:
        if __clock.hour == int(tabs_setup.get_alarm_hour()) \
        and __clock.min == int(tabs_setup.get_alarm_minute()) \
        and __clock.sec == int(tabs_setup.get_alarm_second()):
            print("IT'S THE TIME!!")
            if platform.system() == 'Windows':
                winsound.PlaySound(__resource_path + '/alarm.wav', winsound.SND_ASYNC)
            elif platform.system() == 'Darwin':
                os.system('say Time is Up')
            elif platform.system() == 'Linux':
                os.system('beep -f 5000')