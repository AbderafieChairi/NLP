from .nlpContainer import nlp
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.tokens import Doc



class Entity():
    matchers=[]
    entities=[]
    def __init__(self, name,patterns):
        self.name = name
        self.patterns = patterns
        patterns = [nlp(text) for text in self.patterns]
        matcher = PhraseMatcher(nlp.vocab)
        matcher.add(self.name, None, *patterns)
        Entity.matchers.append([matcher,name])
        Entity.entities.append(self)

    @staticmethod
    def add_to_pipeline():
        @Language.component("entity_recognizer")
        def wrapper(doc:Doc)->Doc:
            for matcher,name in Entity.matchers:
                matches = matcher(doc)
                spans = [Span(doc, start, end, label=name) for match_id, start, end in matches]
                doc.ents = list(doc.ents) + spans
            return doc
        nlp.add_pipe("entity_recognizer", before="ner")
            

class DEntity():
    def __init__(self,name) -> None:
        self.name = name


if __name__ == "__main__":
    example_text = "Morocco is an example text containing value1 and toy2 and 9 of toy1."
    entity =Entity("device",["value1","value2"])
    entity =Entity("toy",["toy1","toy2"])
    Entity.add_to_pipeline()
    doc = nlp(example_text)
    for ent in doc.ents:
        print(ent.text, ent.label_)