from utils_general import CLASSINIT,PROCESS,MODEL,NULL,DOCUMENTATION,ERROR,ERRORMODULE,MODELGPT
from openai import OpenAI
from read_yaml import ReadProjectFile
import os,openai

class OpenAIAgent(object):
    def __init__(self)->CLASSINIT:
        self.modelType = MODELGPT
        # self.defaultTool = [{"type":"retrieval",
        #                      "config":{"timeout":10,
        #                                "max_memory":"512MB"}},
        #                     {"type":"code_interpreter"}]
        self.defaultTool = [{"type":"code_interpreter"}]
        self.defaultName = "Natural_Disaster_Notification_Assistant"
        self.defaultInstruction = (
                "You are an expert who gives you warnings and push notifications about natural disasters. "
                "Using the data given to you and, when necessary, the data on the internet, "
                "you instantly answer the questions asked to you and make warnings to the users. "
                "You analyze data present in .csv files, understand disasters, and come up with notifications or warnings."
            )
        self.api = ReadProjectFile().GetAPI()
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = self.api
            openai.api_key = self.api
        else:
            openai.api_key = self.api
    def __str__(self)->str:
        return "OpenAI Assistant - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return OpenAIAgent.__doc__
    def LoadModel(self)->MODEL:
        return OpenAI()
    def Model(self,
              initModel:MODEL,
              fileObjectID:PROCESS|str,
              timeout:int=300)->MODEL:
        model = initModel.beta.assistants.create(
                model=self.modelType,
                instructions=self.defaultInstruction,
                tools=self.defaultTool,
                name=self.defaultName,
                description="Assistant who examines and analyzes natural disaster data",
                timeout=timeout,
                file_ids=[fileObjectID.id]
            )
        return model


    