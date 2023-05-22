"""Custom extension of Codetimings.Timer
Enables automatically tagging timers with the name of the function they are wrapping

Author: Blake Burgstahler
Last Modified: 19 May 2023
"""

from typing import Callable, Union
from customTimer import Timer

class FunctionTimer(Timer):

    def __call__(self, func):
        """Updated so that specialized function timer is automatically named with the function that it wraps"""
        if self.name is None:
            self.name = func.__name__
        return super().__call__(func)
    
    def stop(self) -> float:
        """Updated to include logging line similar to viper timing"""
        ret = super().stop()
        if self.logger: # NOTE: all this analysis could be done ONCE at the end by calling Timer.timers.total('timer_name')
            if self.timers.count(self.name)>1:
                out = f"Total time to '{self.name}': {self.timers.total(self.name):0.{self.precision}f} seconds" 
                self.logger(out)
        return ret