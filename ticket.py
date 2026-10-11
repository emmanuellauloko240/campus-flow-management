ALLOWED_CATEGORIES = ["Network", "Hardware", "Software", "Other"]

def calculate_priority(urgency,affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10 :
        return "high"
    elif urgency == "medium" or affected_users >= 3:
         return "medium"
    else:
        return "low"
ALLOWED_URGENCIES = ["low","medium","high"]
def ticket(ticket_id, title, category, urgency, affected_users):
    title = title.strip()
    category = category.strip().capitalize()
    urgency = urgency.strip().lower()
    if title.strip() == "":
        raise ValueError("Title cannot be blank")
    if category not in ALLOWED_CATEGORIES:
        raise ValueError("Invalid category")
    if urgency not in ALLOWED_URGENCIES:
        raise ValueError("invalid urgency")

    if(
        not isinstance (affected_users,int)
        or isinstance (affected_users, bool)
        or affected_users <= 0
    ):

        raise ValueError("Affected users must be a positive whole number")
        
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
