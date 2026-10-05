"""A second state writer, deliberately exposed for the architecture case."""

from queue import JOBS


def retry_from_console(job_id):
    JOBS[job_id]["attempts"] = 0
    JOBS[job_id]["sent"] = False
