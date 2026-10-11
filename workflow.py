ALLOWED = {
    "open": ["in_progress"],
    "in_progress": ["resolved"],
    "resolved": ["open"],
}

def change_status(tickets, ticket_id,new_status):
    found = None
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            found = ticket
    if found is None:
        raise ValueError("unknown ticket....")
    if new_status not in ALLOWED[found["status"]]:
        raise ValueError ("Invalid status change")
    if new_status == "in_progress" and found["assigned_to"] is None:
        raise ValueError("Ticket must be assigned first")
    found["status"] = new_status
    return found
