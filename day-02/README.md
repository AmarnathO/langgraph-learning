# state Management 

1. What is State?
    State is the shared source of truth that flows through the workflow. Every node can read it, update it, and pass it to the next node. This reduces complexity, avoids passing many variables between functions, and keeps workflow data centralized and consistent.

2. Why is State important?
    State is important so that each node is aware that what is the change and it's easy to manage across workflow.

3. How does State reduce complexity?
    With State we hvae single source of truth and in future if we want to change teh node defination that can be easily done and no need tp pass mutiple parameter.

4. Why should State remain small?
    So be cost effective / llm Faster in response / 

5. Give one real-world example of State.
    employee_state = {
        name: str,
        address : str,
        salary: int,
        designation: str,
        skill :list[str]
    }



Q1 Why use state instead of many variables?
    It would be easy to have single source of truth / reduce complexity also no need to chnage the signature of functions

Q3What data belongs in state?
    Data that multiple nodes need to read, update, or use for decision-making belongs in state.

Q4 What data should NOT be stored in state?
    Store facts, not raw history.

Q5 How can large state increase AI cost?
    ✅ More data passed around
    ✅ More tokens sent to LLMs
    ✅ Slower execution
    ✅ Higher cost



