from tkinter import *

class ClockFrame (Frame):

    def __init__(self, container, theme, tz_key):
        super().__init__(container)
        print("CLOCK FRAME INIT")
        self._create_clock_elements()
        self._config_clock_elements(theme, tz_key)

    """Properties"""
    @property
    def time(self): return self._time_label.cget("text")

    @time.setter
    def time(self, a): self._time_label.config(text=a)

    @property
    def date(self): return self._date_label.cget("text")

    @date.setter
    def date(self, a): self._date_label.config(text=a)


    """Methods"""
    #CREATE CLOCK ELEMENTS
    def _create_clock_elements(self):
        self._datetime_frame = Frame(self)
        self._time_label = Label(self._datetime_frame)
        self._date_label = Label(self._datetime_frame)
        self._timezone_label = Label(self._datetime_frame)

    #CONFIG CLOCK ELEMENTS
    def _config_clock_elements(self, theme, tz_key):
        self.configure(bg=theme['bg_color'])

        self._datetime_frame.config(bg=theme['bg_color'])
        self._datetime_frame.place(relx=.5, rely=.5, anchor="c")

        self._time_label.config(font=("ds-digital", 85), bg=theme["bg_color"], foreground=theme["text_color"])
        self._time_label.pack()

        self._date_label.config(font=("calibri", 20), bg=theme["bg_color"], foreground=theme["text_color"])
        self._date_label.pack()

        self._timezone_label.config(font=("calibri", 20), bg=theme["bg_color"], foreground=theme["text_color"], text=tz_key)
        self._timezone_label.pack()

    def update(self, theme, tz_key):
        self._config_clock_elements(theme, tz_key)
