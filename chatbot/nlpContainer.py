import spacy
import random
nlp = spacy.load("en_core_web_sm")


if __name__ == "__main__":
    msg = nlp("I want to buy 55 phone and camera")
    for ent in msg.ents:
        print(ent.text,ent.label_)