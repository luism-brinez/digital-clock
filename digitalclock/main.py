#TODO - Need to struct better the whole program, spliting into more specific modules and only apply the general setup in main file

from tkinter import *
import i18n as lang
from clock import Clock
from formatting import *
import tabs_setup
import config_manager
import options_manager
import event_handler
import menu_setup


class App(Tk):

    def __init__(self): 
        super().__init__()
        print("WINDOW INIT")

        self.resources_path = '../digitalclock/resources'
        self.locale_path = '../digitalclock/locales'
        self.options_path = '../digitalclock/options'
        lang.load_path.append(self.locale_path)

        self.app_config = config_manager.get_config()

        #Change this setting when languages files are added/removed 
        lang.set('available_locales', ['en', 'es'])
        lang.set('fallback', 'en')

        #Changes made on json file are merged with menu options
        lang.set('locale', self.app_config.get('main', 'language'))
        self.clock = Clock(options_manager.get_timezones()[self.app_config.get('main', 'timezone')])
        self.theme = options_manager.get_themes()[self.app_config.get('main', 'theme')]
        self.config_window()
        self.clock.start()
        event_handler.setup(self, self.app_config, self.clock)  
        menu_setup.setup(self, self.app_config)
        event_handler.setup_menu_events()
        tabs_setup.setup(self, self.app_config)
        event_handler.setup_alarm_events()
        event_handler.setup_clock_events()    
        
        print("CLOCK STARTED")
    
    #CONFIG WINDOW
    def config_window(self):
        self.geometry("650x350")
        self.minsize(650, 350)
        self.maxsize(650, 350)
        self.title(lang.t('lang.title'))
        self.iconbitmap(self.resources_path + "/icon.ico")
        self.configure(bg=self.theme['bg_color'])

if __name__=="__main__":
    app = App()
    app.mainloop()
    
