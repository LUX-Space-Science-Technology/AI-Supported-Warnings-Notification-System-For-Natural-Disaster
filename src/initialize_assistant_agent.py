from utils_general import CLASSINIT,ERROR,DOCUMENTATION,MODEL,PROCESS,ERRORMODULE,NULL,CSVPATH,USERDEFAULTPROMPT
from assistant_model import OpenAIAgent
from gather_metadata import GetMetadata
from assistant_functions import RETURNTHREAD,RETURNTHREADMESSAGE,CREATEFILEID,AGENTRETRIEVE,GETAGENTMESSAGE
import os

class AgentInitialize(object):
    def __init__(self)->CLASSINIT:
        self.engine = OpenAIAgent()
    def __str__(self)->str:
        return "Agent Initialize - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return AgentInitialize.__doc__
    def GetModel(self)->MODEL:
        return self.engine.LoadModel()
    def Active(self,
               modelInitial:MODEL,
               fileObjectID:PROCESS|str)->PROCESS:
        model = self.engine.Model(initModel=modelInitial,
                                  fileObjectID=fileObjectID)
        return model
