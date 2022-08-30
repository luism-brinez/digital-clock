""" This class init with a determined timezone and require the pytz package """
from datetime import datetime as dt
import time as tm
import pytz
import threading 

class Clock(object):
    
    def __init__(self, timezone):
        self._timezone = pytz.timezone(timezone)
        self._datetime = dt.now(self._timezone)
        self._isStarted = False
        self._t = None
        self._observers = [] 

    @property
    def month(self): return self._datetime.month
    
    @property
    def day(self): return self._datetime.day

    @property
    def year(self): return self._datetime.year

    @property
    def sec(self): return self._datetime.second

    @property
    def min(self): return self._datetime.minute

    @property
    def hour(self): return self._datetime.hour
    
    @property
    def started(self): return self._isStarted

    def update(self):
        while self._isStarted:
            self._datetime = self._datetime.now(self._timezone)
            for callback in self._observers:
                callback()
            tm.sleep(0.5)
            
    def bind_to(self, callback):
        print('data bound')
        self._observers.append(callback)
         

    def start(self):
        self._t = self._t = threading.Thread(target=self.update)
        self._isStarted = True
        self._t.start()

    def stop(self):
        self._isStarted = False
        self._t = None

    def change_timezone(self, timezone):
        self._timezone = pytz.timezone(timezone)

if __name__=='__main__':
    clock = Clock('America/Caracas')
