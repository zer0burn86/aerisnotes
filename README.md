# Aeris Notes

Aeris Notes ist ein KI-gestütztes Tool zur Erfassung, Strukturierung und Wiederauffindung von Ideen, Gedanken und Notizen.
Es hilft dabei, lose Gedanken zu sammeln, automatisch zu clustern und zusammenzufassen – damit kreative Einfälle nicht verloren gehen, sondern in ein durchsuchbares System überführt werden.

> 🔧 Aktuell in Entwicklung – als Proof of Skills im Rahmen meines Portfolios.
> 🧪 Open Source, MVP-Launch geplant im Zuge meiner Bewerbungsunterlagen.

## ✨ Funktionen

- Erfassen von Ideen in natürlicher Sprache  
- Automatisches Clustern verwandter Inhalte  
- Erstellen von Zusammenfassungen  
- Vergabe von Tags und Kategorien  
- Exportfunktionen (JSON, Markdown, CSV)  
- Geplant: Suchfunktion mit Tag- und Kontextfilter  
- Geplant: Benutzeroberfläche zur strukturierten Ansicht und Bearbeitung

## Projektstatus

Work in Progress (Start: Mai 2025)

## Technologien und Tools 

OpenAI API (ChatGPT)
Python (Input/Output-Verarbeitung)
JSON, CSV-Export (Datenstrukturierung)
Zapier 
GitHub (Versionierung und Dokumentation)

## Features (geplant)

[ ] Eingabemaske für Text- und Ideensammlung
[ ] Clustering von ähnlichen Themenfeldern
[ ] Generierung von Zusammenfassungen
[ ] Erstellung von Aufgabenplänen und Handlungsvorschlägen
[ ] Wahl der Persönlichkeit von ChatGPT
[ ] Exportmöglichkeiten in JSON und CSV

Projektphasen:
[x] Definition der Anforderung und Use Cases
[ ] Entwicklung der Promptstruktur für OpenAI API
[x] Erstellung des Python-Skripts zur Kommunikation mit der API
[ ] Entwicklung der Eingabemaske
[ ] Implementierung der Ausgabe- und Exportfunktionen
[ ] Dokumentation und erste Tests 

## Repository-Inhalte:

/docs – Konzeptunterlagen, Diagramme, Workflows
/src – Quellcode in Python
/tests – Testskripte (tbd)
README.md – Projektübersicht und Installationshinweise
FUNKTIONEN.md - Übersicht und Beschreibung der einzelnen Funktionen
RESSOURCEN.md - Übersicht der verwendeten externen Ressourcen und Anbindungen
Konzept.md - tbd
requirements.txt - Übersicht der zu installierenden Module
LICENSE – Lizenzhinweis

## Zielsetzung für MVP 

Texteingabe über eine einfache Konsole
Verarbeitung der Eingaben über OpenAI API
Ausgabe von Clustern und Zusammenfassungen
Speicherung der Ergebnisse als JSON

## Installation 

1. Repository klonen:
   ```bash
   git clone https://github.com/zer0burn86/aerisnotes.git
   cd aerisnotes

   pip install -r requirements.txt

 .env File erstellen mit Inhalt "OPENAI_API_KEY=dein-api-key-hier"  

## Lizenz

Dieses Projekt wird unter der MIT License veröffentlicht.

## Autor

Pascal Wengi

