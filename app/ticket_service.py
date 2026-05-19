from pathlib import Path
import json


# Pfad zur JSON-Datei, in der die Tickets gespeichert werden.
DATA_FILE = Path(__file__).resolve().parent.parent / "tasks.json"


def load_tickets():
    """Lädt alle gespeicherten Tickets aus der JSON-Datei."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tickets(tickets):
    """Speichert die aktuelle Ticketliste in der JSON-Datei."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=2, ensure_ascii=False)


def get_all_tickets():
    """Gibt alle Tickets zurück."""
    return load_tickets()


def get_active_tickets():
    """Gibt alle offenen Tickets zurück."""
    tickets = load_tickets()
    return [ticket for ticket in tickets if not ticket.get("done", False)]


def get_done_tickets():
    """Gibt alle erledigten Tickets zurück."""
    tickets = load_tickets()
    return [ticket for ticket in tickets if ticket.get("done", False)]


def add_ticket(title):
    """Erstellt ein neues Ticket mit dem Status offen."""
    if not title or not title.strip():
        raise ValueError("Der Titel darf nicht leer sein.")

    tickets = load_tickets()

    new_ticket = {
        "title": title.strip(),
        "done": False
    }

    tickets.append(new_ticket)
    save_tickets(tickets)

    return new_ticket


def update_ticket(ticket_id, new_title):
    """Bearbeitet den Titel eines vorhandenen Tickets."""
    tickets = load_tickets()

    if ticket_id < 1 or ticket_id > len(tickets):
        raise IndexError("Ticket wurde nicht gefunden.")

    if not new_title or not new_title.strip():
        raise ValueError("Der neue Titel darf nicht leer sein.")

    tickets[ticket_id - 1]["title"] = new_title.strip()
    save_tickets(tickets)

    return tickets[ticket_id - 1]


def mark_ticket_done(ticket_id):
    """Markiert ein vorhandenes Ticket als erledigt."""
    tickets = load_tickets()

    if ticket_id < 1 or ticket_id > len(tickets):
        raise IndexError("Ticket wurde nicht gefunden.")

    tickets[ticket_id - 1]["done"] = True
    save_tickets(tickets)

    return tickets[ticket_id - 1]


def delete_ticket(ticket_id):
    """Löscht ein vorhandenes Ticket."""
    tickets = load_tickets()

    if ticket_id < 1 or ticket_id > len(tickets):
        raise IndexError("Ticket wurde nicht gefunden.")

    deleted_ticket = tickets.pop(ticket_id - 1)
    save_tickets(tickets)

    return deleted_ticket