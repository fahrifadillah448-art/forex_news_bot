import json
import os

FILE_NAME = "sent_events.json"


def load_sent_events():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_sent_events(events):
    with open(FILE_NAME, "w") as f:
        json.dump(events, f)


def already_sent(event_id):
    sent = load_sent_events()
    return event_id in sent


def mark_sent(event_id):
    sent = load_sent_events()

    if event_id not in sent:
        sent.append(event_id)
        save_sent_events(sent)
