"""Synthetic qualification fixture; never sends a real delivery."""

MAX_ATTEMPTS = 3
MAX_BATCH = 100
JOBS = {}


def enqueue(job_id, payload):
    JOBS[job_id] = {"payload": payload, "attempts": 0, "sent": False}


def record_attempt(job_id, success):
    job = JOBS[job_id]
    if job["sent"] or job["attempts"] >= MAX_ATTEMPTS:
        return False
    job["attempts"] += 1
    job["sent"] = success
    return True
