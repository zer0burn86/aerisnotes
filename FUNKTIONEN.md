# Funktionsübersicht AerisNotes (Version 0.1)

| Funktion | Aufgabe | Notizen |
|:---------|:--------|:--------|
| `begrüßung()` | Zeigt dem Benutzer eine freundliche Begrüßung an | Nur einmal beim Start |
| `eingabe_erfassen()` | Fragt den Benutzer nach seiner Idee | Eingabeaufforderung (input) |
| `anfrage_an_openai(text)` | Sendet den Text an die OpenAI API und erhält die Antwort | API-Kommunikation |
| `antwort_verarbeiten(api_response)` | Extrahiert Cluster und Zusammenfassung aus der API-Antwort | JSON oder Textverarbeitung |
| `ergebnis_anzeigen(cluster, zusammenfassung)` | Zeigt dem Benutzer die KI-Antwort schön formatiert an | Konsole (später GUI?) |
| `ergebnis_speichern(cluster, zusammenfassung)` | Speichert die Ergebnisse lokal als JSON-Datei | Dateiname automatisch generieren? |
| `benutzer_fragen_neue_idee()` | Fragt, ob der Benutzer eine neue Idee eingeben will | Ja/Nein-Entscheidung |
