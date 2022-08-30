from tkinter import *
from configparser import ConfigParser
import options_manager
from main import App
import i18n as lang
from widgets.config_menu import ConfigMenu

"""This receives the window as parameter to handle the containing of the widgets"""
__theme = str
__timezone: str
__config_menu: ConfigMenu
__themes  = options_manager.get_themes()
__timezones  = options_manager.get_timezones()
__time_formats  = options_manager.get_time_formats()

def setup(window: App, config: ConfigParser):
    global __theme, __timezone
    __theme = config.get('main', 'theme')
    __timezone = config.get('main', 'timezone')
    __create_menubar(window, config)

def update():
    global __config_menu
    __config_menu.update(lang)

def get_selected_menu_data(): return (__config_menu.selected_lang, __config_menu.selected_theme, __config_menu.selected_time_format, __config_menu.selected_timezone)

def __create_menubar(window: App, config: ConfigParser):
    global __config_menu
    __menubar = Menu(window)
    window.config(menu=__menubar)
    __config_menu = ConfigMenu(__menubar, __themes, __timezones, __time_formats, lang, config)
    __menubar.add_cascade(label="Config", menu=__config_menu)

