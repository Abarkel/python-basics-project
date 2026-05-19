# Verwendet ein schlankes Python-Image als Basis.
FROM python:3.12-slim

# Legt das Arbeitsverzeichnis im Container fest.
WORKDIR /app

# Kopiert zuerst die Abhängigkeitsdatei, damit Docker den Installationsschritt cachen kann.
COPY requirements.txt .

# Installiert die benötigten Python-Abhängigkeiten.
RUN pip install --no-cache-dir -r requirements.txt

# Kopiert den restlichen Anwendungscode in den Container.
COPY . .

# Dokumentiert den Port, auf dem die FastAPI-Anwendung läuft.
EXPOSE 8000

# Startet die FastAPI-Anwendung über Uvicorn.
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]