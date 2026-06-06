# State Management Questions

** Question : What is State?
    State is the shared source of truth that flows through the workflow. Every node can read it, update it, and pass it to the next node. This reduces complexity, avoids passing many variables between functions, and keeps workflow data centralized and consistent.

** Question : Why is State important?
    State is important so that each node is aware that what is the change and it's easy to manage across workflow.

** Question : How does State reduce complexity?
    With State we hvae single source of truth and in future if we want to change teh node defination that can be easily done and no need tp pass mutiple parameter.

** Question : Why should State remain small?
    So be cost effective / llm Faster in response / 

** Question : Give one real-world example of State.
    employee_state = {
        name: str,
        address : str,
        salary: int,
        designation: str,
        skill :list[str]
    }



** Question : Why use state instead of many variables?
    It would be easy to have single source of truth / reduce complexity also no need to chnage the signature of functions

** Question : What data belongs in state?
    Data that multiple nodes need to read, update, or use for decision-making belongs in state.

** Question : What data should NOT be stored in state?
    Store facts, not raw history.

** Question : How can large state increase AI cost?
    ✅ More data passed around
    ✅ More tokens sent to LLMs
    ✅ Slower execution
    ✅ Higher cost



