
from datetime import date, datetime 

class Profiler(object):

    def __init__(self,args) -> None:
        self.__args = args

    def __call__(self):

        print(f"Started the function: {str(self.__args)} at {datetime.now()} ")
        ret = self.__args(self)
        print(f"Ended the function:  {str(self.__args)} at {datetime.now()} ")
        return ret

 