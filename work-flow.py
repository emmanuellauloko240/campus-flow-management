Search
Ctrl
K
New
Ctrl
+
Shift
+
O
Projects
Artifacts
Customize
Pinned
Drag to pin
Today
Ticket workflow assignment project
Oct 8
Your first chat with Claude
emiene🥹🎀
·
Free
Pasted text.txt
TXT

i'm working on a project  and  i need you to work me through it not just give me codes i want to understand every concept and every bit of it

Good, that’s the right way to approach this. We’ll go one concept at a time, and I won’t hand you finished code. For each step I’ll explain the idea, show you a tiny example, and then you write the real thing. Understanding it is also what lets you defend it in front of your reviewers.

The big picture

CampusFlow is a program that remembers things (tickets), applies rules to them (priority, workflow), and shows them back to a person (menu, queue, reports). Almost every program is those three jobs. Your biggest design decision is keeping them separate:

Logic: the rules, like “what priority is this ticket?” These are plain functions that take input and return a result. They never call input() or print().
Storage: reading and writing the JSON file.
Interface: the menu, which asks questions, calls the logic, and prints results.

This matters because the brief asks, “How can we test business logic without asking for interactive input?” The answer is that if your logic never asks for input, a test can just call the function with values. Keep that idea in mind through the whole project.

Suggested order
Design decisions: the questions in section 2.2, which you answer before coding.
Priority engine: the simplest piece, and it teaches you functions, conditions and testing.
Validation: using exceptions to reject bad input.
Ticket creation and IDs: dictionaries, lists and generating IDs.
Assign, workflow, queue, reports: state transitions, sorting and counting.
JSON persistence: files, and errors from files.
The CLI menu: loops, tying it all together.
Git, PRs and reviews: running alongside all of the above.

We’ll start at step 1, because everything else depends on it.

Step 1: Function contracts

A contract is a promise about a function: what it takes in, what it gives back, and what happens when something goes wrong. If you and your partner agree on contracts up front, you can each write code that plugs into the other’s without seeing it.

Take the first question: where are the tickets stored, and how are they passed around?

The simplest answer is a Python list of dictionaries:

python
tickets = [
    {"id": "T001", "title": "Wi-Fi down", ...},
    {"id": "T002", "title": "Broken laptop", ...},
]

Every function that needs tickets receives this list as a parameter, rather than reaching for a hidden global variable. That keeps functions predictable and easy to test: you can build a small list in a test, pass it in, and check what came out.

The second question is how to signal bad input. There are two common ways:

Return an error value, such as None or (False, "message"). The caller has to remember to check it every time. If they forget, the bug is silent.
Raise an exception, such as raise ValueError("Title cannot be blank"). Python stops the function immediately and carries the error up until something catches it with try/except. It’s hard to ignore by accident.

For this project, exceptions are the cleaner choice. The logic raises, and the CLI catches the error and prints it nicely. That also covers the brief’s requirement that invalid input must be rejected “WITHOUT corrupting stored tickets”, because the function stops before it ever adds anything to the list.

Your turn

I want to check you’ve got the idea before we build on it, so answer these in your own words (rough is fine):

Why would it be a problem if calculate_priority() called input() to ask the user for the urgency itself?
If create_ticket() receives a blank title, what should happen to the tickets list: a new entry, or no change? Why?

Also tell me two things so I can pitch the pace right: how comfortable are you with Python functions, dictionaries, and try/except (new, shaky, or fine)? And which role did you and your partner take, A (creation, validation, priority) or B (assign, lifecycle, queue, reports)?

Once I see your answers, we’ll write the first contract for calculate_priority together, and then you’ll write the function yourself.

what is the duty of the assign and how am i suppose to work on  it

Explaining the assign instruction's role and teaching approach.
What the assign feature is for

Assign answers the question “who is responsible for this problem?” Without it, a ticket is just a report that anyone might fix and nobody owns. Technically, assign changes one field, assigned_to, from None to a staff member’s name. That field is also what the workflow feature checks later: a ticket can’t move to in_progress unless someone is assigned.

The brief gives it two rules:

The ticket ID must exist, and unknown IDs are rejected.
The staff name must be non-empty.

There’s a third rule in F4: a resolved ticket can only be modified after an explicit reopen. Assigning counts as modifying, so your assign function should also reject resolved tickets. It’s easy to miss, and a reviewer will probably test it.

Concepts you’ll need

1. Finding one item in a list. Your tickets are a list of dictionaries, so to find T002 you walk through the list and compare each ticket’s "id" to what you’re looking for:

python
for ticket in tickets:
    if ticket["id"] == wanted_id:
        # found it

If the loop finishes without a match, the ID doesn’t exist. That’s your “unknown ticket” case.

Other features (workflow, view one ticket) also need to find a ticket by ID. Write that search once as its own small function, something like find_ticket(tickets, ticket_id), and reuse it everywhere. Duplicating the loop in four places means four places to fix a bug.

2. Changing a dictionary in place. When your loop finds the ticket, you hold a reference to the actual dictionary inside the list, not a copy. Writing ticket["assigned_to"] = "Amina" changes the stored ticket directly. That’s called mutation, and it’s why you must run all your checks before you change anything. If you assign first and validate afterwards, a rejected request has already modified the data.

3. Cleaning the input. Users type "  Amina " or "t001". Two Python tools handle this:

.strip() removes leading and trailing spaces. A name of "   " becomes "", which is empty and therefore invalid. Without strip, a name made only of spaces would pass.
.upper() normalizes "t001" to "T001", which matches the brief’s “accept and normalize valid case variations consistently.”

4. Raising errors. Reject bad input with raise ValueError("..."), as we discussed, with a useful message. Which message you write for which failure is part of your contract.

How to work on it: the order

Don’t start typing the function. Work through these steps in order:

Write the contract in docs/design-decisions.md. For example: takes tickets, ticket_id, staff_name. On success it returns the updated ticket. On failure it raises ValueError, and the ticket list is unchanged.
List the cases in plain English: success, unknown ID, blank name, spaces-only name, lowercase ID, resolved ticket.
Write the tests first, one per case. They’ll fail at first, and that’s fine. You now know exactly what “done” means.
Write find_ticket, then assign_ticket: find, validate, then mutate, in that order.
Run the tests until they pass.
Open your PR. Your partner reviews the code against your contract.

Writing tests before code feels backwards at first. The payoff is that the tests become your specification, so you can’t quietly forget the resolved-ticket rule.

One design question to decide

Should you be able to re-assign a ticket that already has a staff member, say from Amina to Chidi? The brief doesn’t say. It’s a decision for you and your partner, and it goes in your design doc. I’d allow it, because in real helpdesks people go on leave. Either answer is fine as long as you write it down and test it.

Your turn

Without writing code, put the steps of assign_ticket in order in plain English, as a numbered list. For example, “1. Check that the name isn’t blank...” Then tell me which order you’d put the checks in and why. Is it better to look up the ticket first or check the name first? There’s a reasonable answer either way, so I want to see your reasoning.

Send me that list and we’ll turn it into the function together. Also tell me whether you’re Engineer A or B. If you own assign, you’re B, and I’ll point you to what ties it to the lifecycle work.

Switching examples from pets to ticket-based scenarios.

Understood, no more pets. I’ll use your own tickets from now on.

Here is the check in terms of your real data. Your earlier output was:

python
{'id': 'T001', 'title': 'Wi-Fi down', 'affected_users': 15, ...}

If that dictionary is stored in a variable called first, then first["id"] gives 'T001', and the check is:

python
self.assertEqual(first["id"], "T001")

The same line for the second ticket uses second and "T002".

Your turn

Write the first test, test_ids_count_up, inside the class:

tickets = []
first = create_ticket(tickets, "Wi-Fi down", "Network", "high", 15)
second = create_ticket(tickets, "Broken laptop", "Hardware", "low", 1)
the two assertEqual lines, one for each ID

Everything is indented eight spaces, so it sits inside the def, which is inside the class. Paste it and I’ll check