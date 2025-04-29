# AerisNotes - Wissensmanagementsystem
# Autor: Pascal Wengi
# Start: Mai 2025
import openai
from dotenv import load_dotenv
import os

load_dotenv() 

openai.api.key = os.getenv("OPENAI_API_KEY")

def begruessung(): 
    print("Willkommen bei AerisNotes") # TBD wird durch UI ersetzt

def eingabe_erfassen():
    text = input("Teile mir deine Idee mit: ") 

    if text.stip() != "": # Kurze Abfrage ob Eingabe einfach aus Leerzeichen besteht ("!=" = "ist nicht")
        print("Danke für deine Idee, ich übergebe sie an OpenAI. Einen Moment bitte...")
        return text
    else:
        print("Oups, da ist was schief gelaufen. Bitte teile mir deine Idee nochmal mit.")
        return eingabe_erfassen()

def anfrage_an_openai(text):
    pass

def antwort_verarbeiten(api_response):
    pass

def ergebnis_anzeigen(cl_zf):
    pass

def ergebnis_speichern(cl_zf):
    pass

def abfrage_neue_idee():
    pass