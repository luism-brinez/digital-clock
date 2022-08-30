from tkinter import *

class AlarmFrame (Frame):

    def __init__(self, container, theme, lang):
        super().__init__(container)
        print("ALARM FRAME INIT")
        self.configure(bg=theme["bg_color"])
        self.__create_alarm_elements()
        self.__config_alarm_elements(theme, lang)

    """Properties"""

    @property
    def hour(self): return self.__alarm_hour_data.cget('text')

    @hour.setter
    def hour(self, a): self.__alarm_hour_data.config(text=a) 

    @property
    def minute(self): return self.__alarm_minute_data.cget('text')

    @minute.setter
    def minute(self, a): self.__alarm_minute_data.config(text=a) 

    @property
    def second(self): return self.__alarm_second_data.cget('text')

    @second.setter
    def second(self, a): self.__alarm_second_data.config(text=a)

    @property
    def info(self): return self.__alarm_set_info.cget('text')

    @info.setter
    def info(self, a): self.__alarm_set_info.config(text=a)

    """Methods"""

    #BUTTONS BINDING
    def bind_alarm_buttons_to(self, control_callback, set_callback):
        self.__alarm_left_hour_button.bind("<Button-1>", lambda e: control_callback('hour_minus', self.__alarm_hour_data.cget("text")))
        self.__alarm_left_minute_button.bind("<Button-1>", lambda e: control_callback('minute_minus', self.__alarm_minute_data.cget("text")))
        self.__alarm_left_second_button.bind("<Button-1>", lambda e: control_callback('second_minus', self.__alarm_second_data.cget("text")))
        self.__alarm_right_hour_button.bind("<Button-1>", lambda e: control_callback('hour_plus', self.__alarm_hour_data.cget("text")))
        self.__alarm_right_minute_button.bind("<Button-1>", lambda e: control_callback('minute_plus', self.__alarm_minute_data.cget("text")))
        self.__alarm_right_second_button.bind("<Button-1>", lambda e: control_callback('second_plus', self.__alarm_second_data.cget("text")))
        self.__alarm_set_button.bind("<Button-1>", lambda e: set_callback())

    def update(self, theme: dict, lang):
        self.__config_alarm_elements(theme, lang)

    #CREATE ALARM ELEMENTS
    def __create_alarm_elements(self):
        self.__alarm_controls_frame = Frame(self)
        self.__alarm_left_buttons = Frame(self.__alarm_controls_frame)
        self.__alarm_data_frame = Frame(self.__alarm_controls_frame)
        self.__alarm_right_buttons = Frame(self.__alarm_controls_frame)
        self.__alarm_text_box = Frame(self.__alarm_controls_frame)
        self.__alarm_set_button = Menubutton(self)
        self.__alarm_set_info = Label(self, text='')
        self.__alarm_hour_text = Label(self.__alarm_text_box)
        self.__alarm_minute_text = Label(self.__alarm_text_box)
        self.__alarm_second_text = Label(self.__alarm_text_box)
        self.__alarm_left_hour_button = Label(self.__alarm_left_buttons)
        self.__alarm_left_minute_button = Label(self.__alarm_left_buttons)
        self.__alarm_left_second_button = Label(self.__alarm_left_buttons)
        self.__alarm_hour_data = Label(self.__alarm_data_frame, text='00')
        self.__alarm_minute_data = Label(self.__alarm_data_frame, text='00')
        self.__alarm_second_data = Label(self.__alarm_data_frame, text='00')
        self.__alarm_right_hour_button = Label(self.__alarm_right_buttons)
        self.__alarm_right_minute_button = Label(self.__alarm_right_buttons)
        self.__alarm_right_second_button = Label(self.__alarm_right_buttons)


    #CONFIG ALARM ELEMENTS
    def __config_alarm_elements(self, theme: dict, lang):
        self.configure(bg=theme["bg_color"])

        self.__alarm_controls_frame.config(background=theme['bg_color'])
        self.__alarm_controls_frame.pack(anchor='center')

        self.__alarm_text_box.config(background=theme['bg_color'])
        self.__alarm_text_box.pack(side='left')

        self.__alarm_left_buttons.config(background=theme['bg_color'])
        self.__alarm_left_buttons.pack(side='left', padx=15)

        self.__alarm_data_frame.config(background=theme['bg_color'])
        self.__alarm_data_frame.pack(side='left', padx=15)

        self.__alarm_right_buttons.config(background=theme['bg_color'])
        self.__alarm_right_buttons.pack(side='left', padx=15)

        self.__alarm_hour_text.config(text=lang.t('lang.alarm_hour_text'), font=("calibri", 20), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_hour_text.pack(anchor='center', pady=20)

        self.__alarm_minute_text.config(text=lang.t('lang.alarm_minute_text'), font=("calibri", 20), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_minute_text.pack(anchor='center', pady=20)

        self.__alarm_second_text.config(text=lang.t('lang.alarm_second_text'), font=("calibri", 20), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_second_text.pack(anchor='center', pady=20)

        self.__alarm_left_hour_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='<')
        self.__alarm_left_hour_button.pack(anchor='center')

        self.__alarm_left_minute_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='<')
        self.__alarm_left_minute_button.pack(anchor='center')

        self.__alarm_left_second_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='<')
        self.__alarm_left_second_button.pack(anchor='center')

        self.__alarm_right_hour_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='>')
        self.__alarm_right_hour_button.pack(anchor='center')

        self.__alarm_right_minute_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='>')
        self.__alarm_right_minute_button.pack(anchor='center')

        self.__alarm_right_second_button.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'], text='>')
        self.__alarm_right_second_button.pack(anchor='center')

        self.__alarm_hour_data.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_hour_data.pack(anchor='center')

        self.__alarm_minute_data.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_minute_data.pack(anchor='center')

        self.__alarm_second_data.config(font=("ds-digital", 50), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_second_data.pack(anchor='center')

        self.__alarm_set_button.config(text=lang.t('lang.alarm_set_text'), bg=theme['button_bg_color'], 
        foreground=theme['button_text_color'], activebackground=theme['active_bg_color'], activeforeground=theme['active_text_color'])
        self.__alarm_set_button.pack(anchor='center')

        self.__alarm_set_info.config(font=("calibri", 15), bg=theme['bg_color'], foreground=theme['text_color'])
        self.__alarm_set_info.pack(anchor='center')



