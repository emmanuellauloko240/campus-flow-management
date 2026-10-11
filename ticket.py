def ticket(ticket_id, title, category, urgency, affected_users):
    fellow = {
        "id": ticket_id,
        "title": title,
        "affected_users": affected_users,
        "category": category,
        "urgency": urgency,
        "status": "open",
        "assigned_to": None
    }
    return fellow

result = ticket("T001", "Faulty laptop", "Hardware", "high", 17)
print(result)