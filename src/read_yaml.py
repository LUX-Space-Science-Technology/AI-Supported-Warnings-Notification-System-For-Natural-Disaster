from utils_general import CLASSINIT,PROJECTPATH,DOCUMENTATION,ERROR,ERRORMODULE,NULL
import yaml

class ReadProjectFile(object):
    def __init__(self)->CLASSINIT:
        self.filePath = PROJECTPATH
    def __str__(self)->str:
        return "Read Project File - Sub(Script)"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION | str:
        return ReadProjectFile.__doc__
    def GetAPI(self)->str:
        document = yaml.safe_load(
                open(self.filePath,
                     "r",
                     errors="ignore",
                     encoding="utf-8")
            )
        return document["apikey"]["OPENAI_API_KEY"]