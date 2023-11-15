from utils_general import PROCESS,MODEL,PATH,MODELVOICE,DEFAULTVOICE,VOICEPATH
import openai


def RETURNTHREAD()->PROCESS:
    thread = openai.beta.threads.create()
    return thread

def RETURNTHREADMESSAGE(initModel:MODEL,
                        threadID:PROCESS,
                        prompt:str,
                        role:str="user")->PROCESS:
    message = initModel.beta.threads.messages.create(
            thread_id=threadID.id,
            role=role,
            content=prompt
        )
    return message

def CREATEFILEID(initModel:MODEL,
                 filePath:PATH|str,
                 purpose:str="assistants",
                 timeout:int=300)->str|PROCESS:
    fileObject = initModel.files.create(
            file=open(filePath,"rb"),
            purpose=purpose,
            timeout=timeout
        )
    return fileObject

def AGENTRETRIEVE(initModel:MODEL,
                  threadID:PROCESS,
                  assistantID:PROCESS)->PROCESS:
    isOK:bool = False
    threadRun = initModel.beta.threads.runs.create(
            thread_id=str(threadID.id),
            assistant_id=str(assistantID.id)
        )
    while True:
        retr = initModel.beta.threads.runs.retrieve(
                thread_id=str(threadID.id),
                run_id=str(threadRun.id)
            )
        if retr.completed_at:
            isOK:bool = True
            break
    return isOK

def GETAGENTMESSAGE(initModel:MODEL,
                    threadID:PROCESS,
                    timeout:int=300)->PROCESS:
    response = initModel.beta.threads.messages.list(
            thread_id=str(threadID.id),
            timeout=timeout
        )
    message = response.data[0].content[0].text.value
    return message

def AGENTTEXTTOSPEECH(initModel:MODEL,
                      initText:str,
                      timeout:int=300)->PROCESS:
    record = initModel.audio.speech.create(
            model=MODELVOICE,
            voice=DEFAULTVOICE,
            response_format="mp3",
            timeout=timeout,
            input=str(initText)
        )
    record.stream_to_file(VOICEPATH)
            