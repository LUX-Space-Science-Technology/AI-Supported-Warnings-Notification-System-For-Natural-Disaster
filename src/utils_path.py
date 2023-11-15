from utils_class import PATH
import os

BASEPATH:PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTPATH:PATH = os.path.join(BASEPATH,"outputs")
FILEPATH:PATH = os.path.join(BASEPATH,"files")
CONTENTPATH:PATH = os.path.join(BASEPATH,"content")
PROJECTPATH:PATH = os.path.join(CONTENTPATH,"project.yaml")
CSVPATH:PATH = os.path.join(OUTPUTPATH,"metadata.csv")
VOICEPATH = os.path.join(OUTPUTPATH,"model_voice.mp3")
