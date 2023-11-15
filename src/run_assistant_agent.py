from utils_general import ds__,VOICEPATH,INTERFACEEXAMPLES,RESULT,CREATEDIRECTORY,CSVPATH,OUTPUTPATH,FILEPATH,ERRORMODULE,USERDEFAULTPROMPT
from initialize_assistant_agent import AgentInitialize
from gather_metadata import GetMetadata
from assistant_functions import AGENTTEXTTOSPEECH,RETURNTHREAD,RETURNTHREADMESSAGE,CREATEFILEID,AGENTRETRIEVE,GETAGENTMESSAGE
import gradio as gr,os

CREATEDIRECTORY(OUTPUTPATH)
CREATEDIRECTORY(FILEPATH)

userInput = gr.Textbox(
        lines=10,
        label="> Your Question",
        placeholder="Waiting..."
    )
responseOutput = gr.Textbox(
        lines=10,
        label="> Answer",
        placeholder="Waiting"
    )
audioOutput = gr.Audio(label="> Audio Response",
                       autoplay=True,
                       interactive=False)

if not os.path.exists(CSVPATH):
    print("\n[WAIT] FOR COLLECTING DATA FROM INSTANT-DATABASE [...]")
    GetMetadata().GetFrame()
    print("[DONE] - MODEL DATA HAS BEEN ACTIVATED [+++]\n\n")
if os.path.exists(CSVPATH):
    baseEngine = AgentInitialize()
    baseModel = baseEngine.GetModel()
    fileID = CREATEFILEID(initModel=baseModel,
                          filePath=CSVPATH)
    model = baseEngine.Active(modelInitial=baseModel,
                              fileObjectID=fileID)
else:
    raise ERRORMODULE(OSError,"[PROCESS-CRASH] CHECK YOUR NETWORK CONNECTION OR SYSTEM REQUIREMENTS [---]")

if __name__ == "__main__":
    def OutputActions(question:str)->RESULT:
        prompt = USERDEFAULTPROMPT + str(question)
        thread = RETURNTHREAD()
        threadMessage = RETURNTHREADMESSAGE(initModel=baseModel,
                                            threadID=thread,
                                            prompt=prompt)
        isOK = AGENTRETRIEVE(initModel=baseModel,
                             threadID=thread,
                             assistantID=model)
        if isOK:
            answer = GETAGENTMESSAGE(initModel=baseModel,
                                     threadID=thread)
            AGENTTEXTTOSPEECH(initModel=baseModel,
                              initText=str(answer))
            if os.path.exists(VOICEPATH):
                return answer,VOICEPATH
            else:
                return answer,None
        else:
            return "[UNEXPECTED ERROR] - PLEASE TRY AGAIN"
    iface = gr.Interface(
        fn=OutputActions,
        inputs=[userInput],
        outputs=[responseOutput,audioOutput],
        theme=gr.themes.Monochrome(),
        description=ds__,
        examples=INTERFACEEXAMPLES
                         )
    iface.launch(
        server_name="127.0.0.1",
        server_port=8800,
        inbrowser=False,
        debug=False,
        show_error=True,
        show_api=False,
        share=True,
        max_threads=10
                 )
    
        
    