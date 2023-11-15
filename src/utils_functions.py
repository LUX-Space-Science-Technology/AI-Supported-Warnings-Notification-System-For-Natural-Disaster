from utils_class import PROCESS,NULL,DOCUMENTATION,ERROR,PATH,DATA,CLASSINIT
from utils_error import ERRORMODULE
import os,shutil

CREATEDIRECTORY:PROCESS = lambda x: os.mkdir(x) if not os.path.exists(x) else None
DELETEDIRECTORY:PROCESS = lambda x: shutil.rmtree(x) if len(os.listdir(x)) > 1 else None
CONTROLDIRECTORYLENGTH = lambda x: True if len(os.listdir(x)) > 1 else False

class SAVEFILELOCAL(object):
    def __init__(self,filePath:PATH|str)->CLASSINIT:
        self.filePath = filePath
        self.ops = None
    def __str__(self)->str:
        return "Save File - Sub(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return SAVEFILELOCAL.__doc__
    def Write(self,initialTXT:str|DATA)->PROCESS:
        self.ops.write(initialTXT)
    def __enter__(self)->PROCESS:
        self.ops = open(self.filePath,"w",errors="replace")
        return self
    def __exit__(self,etb:CLASSINIT,ety:CLASSINIT,evl:CLASSINIT)->PROCESS:
        self.ops.close()
        
class READFILELOCAL(object):
    def __init__(self,filePath:PATH|str)->CLASSINIT:
        self.filepath = filePath
        self.ops = None
    def __str__(self)->str:
        return "Read File - Sub(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return READFILELOCAL.__doc__
    def Read(self)->PROCESS:
        return self.ops.read()
    def __enter__(self)->PROCESS:
        self.ops = open(self.filePath,"r",errors="replace",encoding="utf-8")
        return self
    def __exit__(self,ety:CLASSINIT,etb:CLASSINIT,etl:CLASSINIT)->PROCESS:
        self.ops.exit()