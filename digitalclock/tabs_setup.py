from tkinter import *
from tkinter import ttk
from widgets.clock_frame import ClockFrame
from widgets.alarm_frame import AlarmFrame
from configparser import ConfigParser
import i18n as lang
import options_manager

"""This receives the window as parameter to handle the containing of the widgets"""
__theme: str 
__timezone: str 
__tab_control: ttk.Notebook 
__clock_frame: ClockFrame 
__alarm_frame: AlarmFrame 
__themes  = options_manager.get_themes()


def setup(window, config: ConfigParser):
    global __theme, __timezone
    __theme = config.get('main', 'theme')
    __timezone = config.get('main', 'timezone')
    __create_tabs(window)
    __config_tabs()

def update_clock_frame(theme: str, timezone: str):
    global __clock_frame
    __clock_frame.update(theme, timezone)
    __config_tabs()

def update_alarm_frame(theme: str, language):
    global __alarm_frame
    __alarm_frame.update(theme, language)
    __config_tabs()

def bind_alarm_button(control_callback, set_callback):
    global __alarm_frame
    __alarm_frame.bind_alarm_buttons_to(control_callback, set_callback)

def set_clock_time(data: str):
    global __clock_frame
    __clock_frame.time = data

def set_clock_date(data: str):
    global __clock_frame
    __clock_frame.date = data

def set_alarm_hour(data: str):
    global __alarm_frame
    __alarm_frame.hour = data

def set_alarm_minute(data: str):
    global __alarm_frame
    __alarm_frame.minute = data

def set_alarm_second(data: str):
    global __alarm_frame
    __alarm_frame.second = data

def set_alarm_info(data: str):
    global __alarm_frame
    __alarm_frame.info = data

def get_alarm_hour(): return __alarm_frame.hour

def get_alarm_minute(): return __alarm_frame.minute

def get_alarm_second(): return __alarm_frame.second


def get_alarm_frame_instance(): return __alarm_frame

def __create_tabs(window):
    global __tab_control, __alarm_frame, __clock_frame
    __tab_control = ttk.Notebook(window)
    __clock_frame = ClockFrame(__tab_control, __themes[__theme], __timezone)
    __alarm_frame = AlarmFrame(__tab_control, __themes[__theme], lang)
    __tab_control.add(__clock_frame)
    __tab_control.add(__alarm_frame)
    __tab_control.pack(anchor='center', expand=True, fill="both")

def __config_tabs():
        __tab_control.tab(0, text=lang.t('lang.clock_frame_name')) #clock frame tab
        __tab_control.tab(1, text=lang.t('lang.alarm_frame_name')) #alarm frame tab