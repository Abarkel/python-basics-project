# 🛠️ A2Z ServiceDesk

**A2Z ServiceDesk** ist eine interne Anwendung der fiktiven **A-bis-Z Solutions GmbH** zur Verwaltung von Support- und Entwicklungsaufgaben.

Die Anwendung wurde zunächst als lokales internes Tool genutzt. Da Tests, Qualitätssicherung und Bereitstellung bisher überwiegend manuell erfolgten, wird sie im Rahmen dieses Projekts zu einer FastAPI-basierten Web-API erweitert und in einen DevOps-orientierten CI/CD-Prozess integriert.

Ziel ist es, manuelle Prüf- und Bereitstellungsschritte durch automatisierte Tests, Codequalitätsprüfung, Docker-Containerisierung und GitHub Actions nachvollziehbarer, zuverlässiger und reproduzierbarer zu gestalten.

---

## 📌 Funktionen

- Tickets anzeigen
- Tickets erstellen
- Tickets bearbeiten
- Tickets als erledigt markieren
- Tickets löschen
- Health-Check-Endpunkt zur Prüfung der Erreichbarkeit
- Speicherung der Ticketdaten in einer JSON-Datei

---

## 🧰 Technologien

| Bereich            | Technologie    |
| ------------------ | -------------- |
| Programmiersprache | Python         |
| Web-Framework      | FastAPI        |
| Server             | Uvicorn        |
| Tests              | pytest         |
| Codequalität       | Ruff           |
| Containerisierung  | Docker         |
| CI/CD              | GitHub Actions |

---

## 📁 Projektstruktur

```text
backend-roadmap/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── ticket_service.py
├── legacy/
│   └── cli_main.py
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── tasks.example.json
└── README.md
```

---

## ⚙️ Lokale Installation

Python-Abhängigkeiten installieren:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Anwendung lokal starten

```bash
python -m uvicorn app.main:app --reload
```

Danach ist die API erreichbar unter:

```text
http://127.0.0.1:8000
```

Die automatische API-Dokumentation ist erreichbar unter:

```text
http://127.0.0.1:8000/docs
```

---

## 🔗 Wichtige API-Endpunkte

| Methode | Endpunkt                    | Beschreibung                        |
| ------- | --------------------------- | ----------------------------------- |
| GET     | `/health`                   | Prüft, ob die API erreichbar ist    |
| GET     | `/tickets`                  | Gibt alle Tickets zurück            |
| GET     | `/tickets/active`           | Gibt alle offenen Tickets zurück    |
| GET     | `/tickets/done`             | Gibt alle erledigten Tickets zurück |
| POST    | `/tickets`                  | Erstellt ein neues Ticket           |
| PUT     | `/tickets/{ticket_id}`      | Bearbeitet ein Ticket               |
| PUT     | `/tickets/{ticket_id}/done` | Markiert ein Ticket als erledigt    |
| DELETE  | `/tickets/{ticket_id}`      | Löscht ein Ticket                   |

---

## ✅ Tests ausführen

```bash
python -m pytest
```

---

## 🔍 Codequalität prüfen

```bash
python -m ruff check app tests
```

---

## 🐳 Docker Image bauen

```bash
docker build -t a2z-servicedesk:1.0 .
```

---

## 🚀 Docker Container starten

```bash
docker run --name a2z-servicedesk-api --rm -p 8000:8000 a2z-servicedesk:1.0
```

Danach ist die API erreichbar unter:

```text
http://127.0.0.1:8000/docs
```

---

## 🔄 CI/CD mit GitHub Actions

Das Projekt enthält einen GitHub-Actions-Workflow unter:

```text
.github/workflows/ci.yml
```

Der Workflow wird bei Pushes und Pull Requests ausgeführt und umfasst folgende Schritte:

1. Repository auschecken
2. Python einrichten
3. Abhängigkeiten installieren
4. Codequalität mit Ruff prüfen
5. Tests mit pytest ausführen
6. Docker Image bauen

Damit werden zentrale Qualitätssicherungs- und Build-Schritte automatisiert ausgeführt.

---

## 💾 Datenhaltung

Die Anwendung nutzt lokal eine Datei `tasks.json` zur Speicherung von Ticketdaten.  
Diese Datei wird nicht versioniert, da sie lokale Laufzeitdaten enthalten kann.

Als Beispiel für die Datenstruktur dient:

```text
tasks.example.json
```

---

## 🕘 Ursprung des Projekts

Die ursprüngliche Version war eine Python-Kommandozeilenanwendung zur Aufgabenverwaltung.  
Diese Version wurde zur Nachvollziehbarkeit im Ordner `legacy/` abgelegt.

---

## 👨‍💻 Autor

Ahmed Barkel  
Interner Entwicklungsprototyp für die A-bis-Z Solutions GmbH

---

## 📄 Lizenz

Alle Rechte vorbehalten.  
Dieses Projekt dient als interner Prototyp der A-bis-Z Solutions GmbH und ist nicht zur externen Nutzung oder Weiterverbreitung vorgesehen.
