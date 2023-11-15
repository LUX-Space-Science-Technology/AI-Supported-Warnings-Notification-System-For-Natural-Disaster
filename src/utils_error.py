from utils_class import CLASSINIT,ERROR,DOCUMENTATION

class ERRORMODULE(object):
    def __init__(self)->CLASSINIT:
        self.error:ERROR = NotImplementedError(NotImplemented)
    def __str__(self)->str:
        return "Error Module Creation - Sub(Script)"
    def __call__(self)->ERROR:
        return self.error
    def __getstate__(self)->ERROR:
        raise self.error
    def __repr__(self)->DOCUMENTATION | str:
        return ERRORMODULE.__doc__
    @property
    def Default(self)->ERROR:
        raise self.error
    def Manuel(self,errorType:ERROR,errorMessage:str)->ERROR:
        raise errorType(errorMessage)