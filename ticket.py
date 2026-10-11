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
result = ticket("T001", "Faulty laptop", "Hardware", "high", 17)
print(result)

print(calculate_priority("high", 17))
print(calculate_priority("high", 4))
print(calculate_priority("low", 12))
print(calculate_priority("medium", 1))
print(calculate_priority("low", 3))
print(calculate_priority("low", 2))