# AerisNotes - Wissensmanagementsystem
# Autor: Pascal Wengi
# Start: Mai 2025
import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv() 

# openai.api_key = os.getenv("OPENAI_API_KEY") ## openai ver 0.28 Code
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

def begruessung(): 
    print("Willkommen bei AerisNotes") # TBD wird durch UI ersetzt

def eingabe_erfassen():
    text = input("Teile mir deine Idee mit: ") 

    if text.strip() != "": # Kurze Abfrage ob Eingabe einfach aus Leerzeichen besteht ("!=" = "ist nicht")
        print("Danke für deine Idee, ich übergebe sie an OpenAI. Einen Moment bitte...")
        return text
    else:
        print("Oups, da ist was schief gelaufen. Bitte teile mir deine Idee nochmal mit.")      # Fallback Prozess falls User nur Leerzeichen tippt
        return eingabe_erfassen()

def anfrage_an_openai(text, persona=None):
    if persona is None or persona == "":
        filename = "personas/default.md"
    else:
        pass # Hier kommt später das Mapping für Personas

    with open(filename, "r", encoding="utf-8") as file:
        instructions = file.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "developer", "content": instructions},
            {"role": "user", "content": text}
        ]
    )
    return response     # Gibt komplett alle Infos aus OpenAI API zurück

def antwort_verarbeiten(api_response):
    antwort_kurz = api_response.choices[0].message.content
    return antwort_kurz     # Gibt gefiltert nur Antwort von GPT zurück

def ergebnis_anzeigen(cl_zf):
    pass

def ergebnis_speichern(cl_zf):
    pass

def abfrage_neue_idee():
    pass

def test():
    text = eingabe_erfassen()                      
    api_response = anfrage_an_openai(text)
    antwort_kurz = antwort_verarbeiten(api_response)
    print(antwort_kurz)

begruessung()
test()

