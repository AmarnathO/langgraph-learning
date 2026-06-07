**Why did you choose 2 nodes instead of 1?
1. Nodes should have single responsibility
2. Nodes should be testable
3. Failures should be logged
4. Expensive operations should be isolated

What belongs in state?
Stae hold the data across the workflow

**What should not belong in state?
State should contain only workflow-relevant data that needs to be shared across nodes. Temporary variables, secrets, and large unnecessary payloads should not be stored in state.


**If 100,000 users use this workflow, what breaks first?
There is no database, no cache, and no LLM. So the first bottleneck is usually:

**Application Server Capacity:
The machine running the application can only handle a limited number of requests.

###Current Risks
**Application server overload
    Too many concurrent requests.
    CPU and memory exhaustion.
**No rate limiting
    One user could spam requests.
    No load balancing
**Only one application instance exists.
**No monitoring
    Hard to know what is failing.