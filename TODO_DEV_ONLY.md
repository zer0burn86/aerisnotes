## Fahrplan: Prompt & Behaviour in Aeris Notes

### 1. Grundfunktionalität vorbereiten
- [ ] Erstellung von `default.md` im Unterordner `/Persona`
- [ ] Noch KEIN Dropdown und KEIN Button – Fokus auf einfache Anbindung

---

### 2. Funktion `anfrage_an_openai(text, persona)` anpassen
- [ ] Mapping-Befehl: Persona-Name → Markdown-Datei
- [ ] Einlesen der `.md` in Variable `instructions`
- [ ] Übergabe als system-Prompt:  
      `{"role": "system", "content": instructions}`

---

### 3. Testphase 1 – Basis-Funktionalität
- [ ] Erste Tests mit `default.md` ohne UI-Komponenten

---

### 4. Fun-Faktor: Persönlichkeitsausbau
- [ ] Erstellung eines humorvollen Prompts (z. B. `pirat.md`)

---

### 5. Dynamisches Mapping vorbereiten
- [ ] Erstellung von `persoenlichkeiten.json` im Ordner `/Persona`  
- [ ] Struktur: Key = Rollenname (z. B. "Pirat"), Value = Dateiname (z. B. "persona_pirat.md")
- [ ] Definition des Dropdown-Menüs über `persoenlichkeiten.keys()`

---

### 6. Verbindung von Dropdown und Anfrage
- [ ] Erweiterung von `anfrage_an_openai()` zur Nutzung von `dropdown.value`
- [ ] Fallback: `"persona_default.md"`, falls keine Auswahl getroffen wurde

---

### 7. Testphase 2 – dynamische Auswahl testen
- [ ] Verhalten mit verschiedenen `.md`-Personas testen
- [ ] Fehlerbehandlung bei leerer oder ungültiger Auswahl

---

*Letzte Änderung durch zer0burn, Stand: 30.04.2025
