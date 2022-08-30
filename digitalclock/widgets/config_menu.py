from cgitb import text
from tkinter import *

class ConfigMenu(Menu):

    def __init__(self, container, themes,  timezones, time_formats, langs, config):
        super().__init__(container)
        self._selected_lang = StringVar()
        self._selected_theme = StringVar()
        self._selected_timezone = StringVar()
        self._selected_time_format = StringVar()
        self._create_menus(themes,  timezones, time_formats, langs)

        #Setting default option first time launched
        self._selected_lang.set(config.get('main', 'language'))
        self._selected_theme.set(config.get('main', 'theme'))
        self._selected_timezone.set(config.get('main', 'timezone'))
        self._selected_time_format.set(config.get('main', 'time_format'))

        self.update(langs)
        self.config(tearoff=0)

    #With these porperties we return a reference of the StringVar() objects
    #so any change for those variables can be handle outside the class
    @property
    def selected_lang(self): return self._selected_lang

    @property
    def selected_theme(self): return self._selected_theme

    @property
    def selected_timezone(self): return self._selected_timezone

    @property
    def selected_time_format(self): return self._selected_time_format

    def _create_menus(self, themes,  timezones, time_formats, langs):
        self._lang_menu = Menu(self, tearoff=0)
        lang_dict = {}
        for lang in langs.get('available_locales'): lang_dict[lang] = lang
        self._add_radiobuttons(self._lang_menu, lang_dict, self._selected_lang)

        self._theme_menu = Menu(self, tearoff=0)
        self._add_radiobuttons(self._theme_menu, themes, self._selected_theme)

        self._timezone_menu = Menu(self, tearoff=0)
        self._add_radiobuttons(self._timezone_menu, timezones, self._selected_timezone)

        self._time_format_menu = Menu(self, tearoff=0)
        self._add_radiobuttons(self._time_format_menu, time_formats, self._selected_time_format)

        self.add_cascade(label="theme", menu=self._theme_menu)
        self.add_cascade(label="timezone", menu=self._timezone_menu)
        self.add_cascade(label="lang", menu=self._lang_menu)
        self.add_cascade(label="time_format", menu=self._time_format_menu)

        self._cached_labels = {"theme":"theme", "timezone":"timezone", "lang":"lang", "time_format":"time_format"} 
        self.add_separator()

    def _add_radiobuttons(self, menu, dict, selection):
        for key in dict:
            menu.add_radiobutton(label=key, value=key, variable=selection)

    def update(self, lang):
        self.entryconfig(self._cached_labels["theme"], label=lang.t('lang.theme_button'))
        self._cached_labels["theme"] = lang.t('lang.theme_button')

        self.entryconfig(self._cached_labels["timezone"], label=lang.t('lang.timezone_button'))
        self._cached_labels["timezone"] = lang.t('lang.timezone_button')

        self.entryconfig(self._cached_labels["lang"], label=lang.t('lang.lang_button'))
        self._cached_labels["lang"] = lang.t('lang.lang_button')

        self.entryconfig(self._cached_labels["time_format"], label=lang.t('lang.time_format_button'))
        self._cached_labels["time_format"] = lang.t('lang.time_format_button')