import warnings
warnings.simplefilter("ignore", UserWarning)
import random
from .nlpContainer import nlp
class Intent:
    def __init__(self, name,messages,responses=[],required_entities=[],sub_intents=[]):
        self.name = name
        self.messages = messages
        self.responses = responses
        self.required_entities = required_entities
        self.sub_intents = sub_intents
        self.entities=[]

    def parse(self,msg_): 
        msg = nlp(msg_)
        if (msg and msg.vector_norm):
            for m in self.messages:
                if msg.similarity(nlp(m)) > 0.6:
                    self.check_required_entities(msg_)
                    res= random.choice(self.responses)
                    for text,label in self.entities:
                        res = res.replace(f"${label}",text)
                    return res
        return ""

    def check_required_entities(self,msg_):
            msg = nlp(msg_)
            for ent in msg.ents:
                if ent.label_ in [i.name for i in self.required_entities]:
                    self.entities.append([ent.text,ent.label_])

    def add_response(self,response):
        self.responses.append(response)