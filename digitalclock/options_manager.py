import json

__options_path = '../digitalclock/options'
f = open(__options_path + '/options.json')
__options = json.load(f)

__timezones = __options['timezones']
__themes = __options['themes']
__time_formats = __options['time_formats']

def get_options():
    return __options

def get_timezones():
    return __timezones

def get_themes():
    return __themes

def get_time_formats():
    return __time_formats