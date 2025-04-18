# jarvis_core.py
from Backend.Model import FirstLayerDMM
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation 
from Backend.Chatbot import ChatBot 
from Backend.TextToSpeech import TextToSpeech

Functions = ["open", "close","play","system","content","google search","youtube search"]

def process_query(query):
    Decision = FirstLayerDMM(query)
    G = any([i for i in Decision if i.startswith("general")])
    R = any([i for i in Decision if i.startswith("realtime")]) 
    Mearged_Query = "and ".join(
        [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
    ) 

    for queries in Decision:
        if any(queries.startswith(func) for func in Functions):
            Automation(list(Decision))

    if G and R or R:
        return RealtimeSearchEngine(Mearged_Query)

    for Queries in Decision:
        if "general" in Queries:
            QueryFinal = Queries.replace("general", "")
            return ChatBot(QueryFinal)
        elif "realtime" in Queries:
            QueryFinal = Queries.replace("realtime", "")
            return RealtimeSearchEngine(QueryFinal)
        elif "exit" in Queries:
            return "Goodbye!"
