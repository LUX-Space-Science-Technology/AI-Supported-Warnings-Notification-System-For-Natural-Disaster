from utils_general import CLASSINIT,CSVPATH,METEOSOURCE,DOCUMENTATION,DATA,URL,NULL,ERRORMODULE,ERROR
import feedparser,pandas as pd

class GetMetadata(object):
    def __init__(self)->CLASSINIT:
        self.dataDictionary = METEOSOURCE
        self.feed = None
        self.multiDataList:list = []
    def __str__(self)->str:
        return "Get Metadata - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ERRORMODULE().Default
    def __repr__(self)->DOCUMENTATION|str:
        return GetMetadata.__doc__
    def ReadParser(self,url:URL|str)->DATA:
        try:
            self.feed = feedparser.parse(url)
            return self.feed
        except:
            pass
    def GetData(self)->list|str:
        for cname,curl in self.dataDictionary.items():
            feed = self.ReadParser(url=curl)
            if feed is not None:
                entries = feed["entries"]
                if (len(entries) > 0) and (isinstance(entries,list)):
                    for index in range(len(entries)):
                        data = entries[index]
                        if data["cap_message_type"].lower() == "alert":
                            try:
                                area = data["cap_areadesc"]
                                time = data["cap_sent"]
                                event = data["cap_event"]
                                urgency = data["cap_urgency"]
                                status = data["cap_status"]
                                self.multiDataList.append(
                                        [
                                          str(area),
                                          str(cname),
                                          str(time),
                                          str(event),
                                          str(urgency),
                                          str(status)
                                                        ]
                                    )
                            except:
                                pass
                        else:
                            pass
                else:
                    try:
                        entries = feed["entry"]
                        if (len(entries) > 0) and (isinstance(entries,list)):
                            for index in range(len(entries)):
                                data = entries[index]
                                if data["cap_message_type"].lower() == "alert":
                                    try:
                                        area = data["cap_areadesc"]
                                        time = data["cap_sent"]
                                        event = data["cap_event"]
                                        urgency = data["cap_urgency"]
                                        status = data["cap_status"]
                                        self.multiDataList.append(
                                                [
                                                    str(area),
                                                    str(cname),
                                                    str(time),
                                                    str(event),
                                                    str(urgency),
                                                    str(status)
                                                        ]
                                            )
                                    except:
                                        pass
                                else:
                                    pass
                    except:
                        pass
            else:
                area = "No Information"
                time = "No Information"
                event = "No Information"
                urgency = "No Information"
                status = "No Information"
                self.multiDataList.append(
                        [
                            area,
                            cname,
                            time,
                            event,
                            urgency,
                            status
                                        ]
                    )
        if len(self.multiDataList) > 0:
            return self.multiDataList
        else:
            return "I cannot respond for this transaction, try again - MODELRSSP -"
    def GetFrame(self)->DATA:
        dataResponse = self.GetData()
        if isinstance(dataResponse,list):
            frame = pd.DataFrame(dataResponse,columns=["AREA","COUNTRY","TIME","DISASTER","URGENCY","STATUS"])
            frame.to_csv(CSVPATH)
        else:
            pass


        