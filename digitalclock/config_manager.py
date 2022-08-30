from configparser import ConfigParser, NoOptionError, MissingSectionHeaderError
import options_manager

__options_path = '../digitalclock/options'
__languages = ('en', 'es')
__themes  = options_manager.get_themes()
__timezones  = options_manager.get_timezones()
__time_formats  = options_manager.get_time_formats()

def get_config():
    cfg = __load_config_file()
    print(cfg.sections())
    __check_sections(cfg)
    __check_options(cfg)
    __check_values(cfg)
    save_config(cfg)
    return cfg

def save_config(cfg: ConfigParser):
    with open(__options_path + '/config.ini', 'w') as f:
        cfg.write(f)

def __load_config_file():
    cfg = ConfigParser()
    try: 
        cfg.read(__options_path + '/config.ini')
        return cfg
    except MissingSectionHeaderError:
        return cfg

def __check_sections(cfg: ConfigParser):
    __check_main_section(cfg)
    __check_alarm_section(cfg)

def __check_options(cfg: ConfigParser):
    __check_theme_option(cfg)
    __check_timezone_option(cfg)
    __check_language_option(cfg)
    __check_time_format_option(cfg)
    __check_alarm_hour_option(cfg)
    __check_alarm_minute_option(cfg)
    __check_alarm_second_option(cfg)

def __check_values(cfg: ConfigParser):
    __check_theme_value(cfg)
    __check_timezone_value(cfg)
    __check_language_value(cfg)
    __check_time_format_value(cfg)
    __check_alarm_hour_value(cfg)
    __check_alarm_minute_value(cfg)
    __check_alarm_second_value(cfg)


def __check_main_section(cfg: ConfigParser):
    if 'main' not in cfg.sections():
        cfg.add_section('main')

def __check_alarm_section(cfg: ConfigParser):
    if 'alarm' not in cfg.sections():
        cfg.add_section('alarm')

def __check_theme_option(cfg: ConfigParser):
    try: cfg.get('main', 'theme')
    except NoOptionError: 
        cfg.set('main', 'theme', list(__themes)[0])

def __check_timezone_option(cfg: ConfigParser):
    try: cfg.get('main', 'timezone')
    except NoOptionError:
        cfg.set('main', 'timezone', list(__timezones)[0])

def __check_language_option(cfg: ConfigParser):
    try: cfg.get('main', 'language')
    except NoOptionError:
        cfg.set('main', 'language', __languages[0])

def __check_time_format_option(cfg: ConfigParser):
    try: cfg.get('main', 'time_format')
    except NoOptionError: 
        cfg.set('main', 'time_format', list(__time_formats)[0])

def __check_alarm_hour_option(cfg: ConfigParser):
    try: cfg.get('alarm', 'alarm_hour')
    except NoOptionError: 
        cfg.set('alarm', 'alarm_hour', '')
    

def __check_alarm_minute_option(cfg: ConfigParser):
    try: cfg.get('alarm', 'alarm_minute')
    except NoOptionError: 
        cfg.set('alarm', 'alarm_minute', '')

def __check_alarm_second_option(cfg: ConfigParser):
    try: cfg.get('alarm', 'alarm_second')
    except NoOptionError: 
        cfg.set('alarm', 'alarm_second', '')

def __check_theme_value(cfg: ConfigParser):
    if cfg.get('main', 'theme') not in list(__themes):
        cfg.set('main', 'theme', list(__themes)[0])

def __check_timezone_value(cfg: ConfigParser):
    if cfg.get('main', 'timezone') not in list(__timezones):
        cfg.set('main', 'timezone', list(__timezones)[0])

def __check_language_value(cfg: ConfigParser):
    if cfg.get('main', 'language') not in __languages:
        cfg.set('main', 'language', __languages[0])

def __check_time_format_value(cfg: ConfigParser):
    if cfg.get('main', 'time_format') not in list(__time_formats):
        cfg.set('main', 'time_format', list(__time_formats)[0])

def __check_alarm_hour_value(cfg: ConfigParser):
    try: 
        if int(cfg.get('alarm', 'alarm_hour')) < 0 or int(cfg.get('alarm', 'alarm_hour')) > 23:
            cfg.set('alarm', 'alarm_hour', '')
            cfg.set('alarm', 'alarm_minute', '')
            cfg.set('alarm', 'alarm_second', '')
    except ValueError: 
        cfg.set('alarm', 'alarm_hour', '')
        cfg.set('alarm', 'alarm_minute', '')
        cfg.set('alarm', 'alarm_second', '')


def __check_alarm_minute_value(cfg: ConfigParser):
    try: 
        if int(cfg.get('alarm', 'alarm_minute')) < 0 or int(cfg.get('alarm', 'alarm_minute')) > 59:
            cfg.set('alarm', 'alarm_hour', '')
            cfg.set('alarm', 'alarm_minute', '')
            cfg.set('alarm', 'alarm_second', '')
    except ValueError: 
        cfg.set('alarm', 'alarm_hour', '')
        cfg.set('alarm', 'alarm_minute', '')
        cfg.set('alarm', 'alarm_second', '')

def __check_alarm_second_value(cfg: ConfigParser):
    try: 
        if int(cfg.get('alarm', 'alarm_second')) < 0 or int(cfg.get('alarm', 'alarm_second')) > 59:
            cfg.set('alarm', 'alarm_hour', '')
            cfg.set('alarm', 'alarm_minute', '')
            cfg.set('alarm', 'alarm_second', '')
    except ValueError: 
        cfg.set('alarm', 'alarm_hour', '')
        cfg.set('alarm', 'alarm_minute', '')
        cfg.set('alarm', 'alarm_second', '')

