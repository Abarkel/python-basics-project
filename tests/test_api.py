
"""Diese Datei enthält Tests für die API-Endpunkte der FastAPI-Anwendung.
Die Tests verwenden den TestClient, um HTTP-Anfragen zu simulieren und
die Antworten zu überprüfen. Dadurch wird sichergestellt, dass Tickets
erstellt, angezeigt und als erledigt markiert werden können.
"""
import pytest
from fastapi.testclient import TestClient

import app.ticket_service as ticket_service
from app.main import app

# Der TestClient ermöglicht es, die FastAPI-Anwendung zu testen,
# ohne sie tatsächlich zu starten. Er simuliert HTTP-Anfragen an die API-Endpunkte.
client = TestClient(app)


@pytest.fixture(autouse=True)
def nutze_temporaere_ticket_datei(tmp_path, monkeypatch):
    """Nutzt für jeden Test eine eigene temporäre JSON-Datei."""
    test_datei = tmp_path / "tasks.json"
    test_datei.write_text("[]", encoding="utf-8")

    monkeypatch.setattr(ticket_service, "DATA_FILE", test_datei)


def test_health_check():
    """Prüft, ob die API erreichbar ist."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ticket_erstellen_und_anzeigen():
    """Prüft, ob ein Ticket erstellt und anschließend angezeigt wird."""
    create_response = client.post(
        "/tickets",
        json={"title": "Fehler beim Öffnen eines Supporttickets prüfen"},
    )

    assert create_response.status_code == 201
    assert create_response.json()["ticket"]["title"] == (
        "Fehler beim Öffnen eines Supporttickets prüfen"
    )
    assert create_response.json()["ticket"]["done"] is False

    list_response = client.get("/tickets")

    assert list_response.status_code == 200
    assert len(list_response.json()["tickets"]) == 1


def test_ticket_als_erledigt_markieren():
    """Prüft, ob ein Ticket als erledigt markiert werden kann."""
    client.post(
        "/tickets",
        json={"title": "Statusänderung eines Tickets prüfen"},
    )

    response = client.put("/tickets/1/done")

    assert response.status_code == 200
    assert response.json()["ticket"]["done"] is True


def test_unbekanntes_ticket_liefert_404():
    """Prüft, ob ein nicht vorhandenes Ticket korrekt behandelt wird."""
    response = client.put("/tickets/99/done")

    assert response.status_code == 404