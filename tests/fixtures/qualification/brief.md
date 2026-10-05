# Synthetic delivery queue

This is invented evaluation data, not a real service or incident. There is no remote, network transport, secret, or production data.

The current queue is in memory. Both the worker and console modify its records. Add durable retries that survive process restarts, with one owner for attempt and delivery state. Preserve the caller's ability to enqueue a job and request a retry. The future delivery adapter may time out after the receiver accepts a request; do not promise exactly-once delivery without addressing that ambiguity.

Only design is requested in the architecture case. Do not implement, install packages, send requests, or change this fixture.
