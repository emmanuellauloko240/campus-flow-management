# Ticket Creation, Priority and Workflow

**Author:** Uloko Emmanuella Emiene

This part of CampusFlow covers ticket creation, input validation, the priority engine and the status workflow. The code is in `ticket.py` and `workflow.py`, and the tests are in `test_ticket.py` and `test_workflow.py`.

## Files

| File | What it does |
|---|---|
| `ticket.py` | `calculate_priority`, `ticket` (validates and builds one ticket), `next_id`, `create_ticket` |
| `workflow.py` | `ALLOWED` transition table and `change_status` |
| `test_ticket.py` | 16 tests for priority, validation and IDs |
| `test_workflow.py` | 6 tests for status changes |

## How tickets are created

`create_ticket(tickets, title, category, urgency, affected_users)`:

1. Generates the next ID (`T001`, `T002`, ...) from the highest existing number, so IDs stay unique even after a reload.
2. Validates and normalizes the input (below).
3. Calculates the priority.
4. Appends the ticket to the `tickets` list and returns it.

If any check fails, the function raises `ValueError` **before** anything is appended, so a bad request never changes the list.

### Validation rules

- Title: whitespace is stripped, and a blank title is rejected.
- Category: stripped and capitalized (`network` becomes `Network`). Must be Network, Hardware, Software or Other.
- Urgency: stripped and lowercased (`HIGH` becomes `high`). Must be low, medium or high.
- Affected users: must be a positive whole number. Zero, negatives, decimals and booleans are rejected.

## Priority rules

Checked in this order, and the first match wins:

1. High urgency **and** 10 or more users: **critical**
2. High urgency **or** 10 or more users: **high**
3. Medium urgency **or** 3 or more users: **medium**
4. Everything else: **low**

`calculate_priority` takes values and returns a result. It never calls `input()` or `print()`, so tests can call it directly.

## Status workflow

```
open ──► in_progress ──► resolved
 ▲                           │
 └────────── reopen ─────────┘
```

The allowed moves are stored as data in the `ALLOWED` dictionary in `workflow.py`.

`change_status(tickets, ticket_id, new_status)` checks, in this order:

1. The ticket ID exists, otherwise it raises `ValueError`.
2. The move is allowed by `ALLOWED`, otherwise it raises `ValueError`.
3. If the new status is `in_progress`, the ticket must be assigned, otherwise it raises `ValueError`.
4. Only then does it change the status and return the ticket.

Every check runs before the status is changed, so a rejected request leaves the ticket unchanged.

### Design decisions

- Tickets are passed to functions as a list of dictionaries, not through a global variable.
- Errors are signalled by raising `ValueError`. The CLI catches them and prints the message.
- Reopening is a normal status change (`resolved` to `open`).
- `in_progress` cannot go back to `open`, because the brief lists only the forward moves.
- `next_id` uses the highest existing number, not `len(tickets) + 1`.

## Running the tests

```
python3 -m unittest -v
```

Result on my branch: **22 tests, all passing.**

| Area | Tests |
|---|---|
| Priority | high + 10 is critical, high + 17 is critical, high + 4 is high, low + 10 is high, low + 12 is high, low + 3 is medium, medium + 1 is medium, low + 2 is low |
| Validation | blank title, invalid category, invalid urgency, zero users and decimal users are rejected, and case is normalized |
| IDs | IDs count up, and an invalid ticket is not stored |
| Workflow | unassigned cannot start, open cannot skip to resolved, full path to resolved, reopen, resolved cannot go to in_progress, unknown ID rejected |

## Known limitations

- There is no `assign_ticket` function yet, so the workflow tests set `assigned_to` directly.
- The work queue (F5) is not written yet.
- `main_main` and the `main()` call at the bottom of `ticket.py` have different names and need to match.
- Loading and saving JSON is inside the menu function and should move to a storage module.




