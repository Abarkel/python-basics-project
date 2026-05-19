from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.ticket_service import (
    add_ticket,
    delete_ticket,
    get_active_tickets,
    get_all_tickets,
    get_done_tickets,
    mark_ticket_done,
    update_ticket,
)


# Erstellt die FastAPI-Anwendung.
app = FastAPI(
    title="A-bis-Z Solutions Ticketsystem",
    description="Einfache Web-API zur Verwaltung interner Supporttickets.",
    version="1.0.0",
)


class TicketCreate(BaseModel):
    """Datenmodell für das Erstellen eines neuen Tickets."""

    title: str


class TicketUpdate(BaseModel):
    """Datenmodell für das Bearbeiten eines vorhandenen Tickets."""

    title: str


@app.get("/health")
def health_check():
    """Prüft, ob die Anwendung erreichbar ist."""
    return {"status": "ok", "message": "Ticketsystem läuft."}


@app.get("/tickets")
def list_tickets():
    """Gibt alle Tickets zurück."""
    return {"tickets": get_all_tickets()}


@app.get("/tickets/active")
def list_active_tickets():
    """Gibt alle offenen Tickets zurück."""
    return {"tickets": get_active_tickets()}


@app.get("/tickets/done")
def list_done_tickets():
    """Gibt alle erledigten Tickets zurück."""
    return {"tickets": get_done_tickets()}


@app.post("/tickets", status_code=201)
def create_ticket(ticket: TicketCreate):
    """Erstellt ein neues Ticket."""
    try:
        created_ticket = add_ticket(ticket.title)
        return {
            "message": "Ticket wurde erstellt.",
            "ticket": created_ticket,
        }
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@app.put("/tickets/{ticket_id}")
def edit_ticket(ticket_id: int, ticket: TicketUpdate):
    """Bearbeitet den Titel eines vorhandenen Tickets."""
    try:
        updated_ticket = update_ticket(ticket_id, ticket.title)
        return {
            "message": "Ticket wurde aktualisiert.",
            "ticket": updated_ticket,
        }
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except IndexError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.put("/tickets/{ticket_id}/done")
def complete_ticket(ticket_id: int):
    """Markiert ein Ticket als erledigt."""
    try:
        completed_ticket = mark_ticket_done(ticket_id)
        return {
            "message": "Ticket wurde als erledigt markiert.",
            "ticket": completed_ticket,
        }
    except IndexError as error:
        raise HTTPException(status_code=404, detail=str(error))


@app.delete("/tickets/{ticket_id}")
def remove_ticket(ticket_id: int):
    """Löscht ein vorhandenes Ticket."""
    try:
        deleted_ticket = delete_ticket(ticket_id)
        return {
            "message": "Ticket wurde gelöscht.",
            "ticket": deleted_ticket,
        }
    except IndexError as error:
        raise HTTPException(status_code=404, detail=str(error))