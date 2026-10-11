def calculate_priority(urgency,affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10 :
        return "high"
    elif urgency == "medium" or affected_users >= 3:
         return "medium"
    else:
        return "low"
def ticket(ticket_id, title, category, urgency, affected_users):
    if title.strip() == "":
        raise ValueError("Title cannot be blank")
    priority = calculate_priority(urgency,affected_users)

    fellow = {
        "id": ticket_id,
        "title": title,
        "affected_users": affected_users,
        "category": category,
        "urgency": urgency,
        "status": "open",
        "assigned_to": None,
        "priority": priority
    }
    return fellow
