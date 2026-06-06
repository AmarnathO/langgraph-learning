# Langraph Notes

** Question :  Why we need langgraph ?
- Eariler we were unable to implement 
    - Muti Agent orchestration
    - human in loops
    - Loop back in flows
    - If app Crashed then you lost data langrpah give option for state that hold data across
    - Stateful nodes 

** Question : What is an LLM, Agent, Workflow 
    - LLM (Large Language Model) is a statistical model trained on large datasets that generates text by predicting the most likely next token.

    - Agent : These are program that can perform a given task based on reasoning and tools  to archive a goal

    - workflow : This is predefined flow of a program that can be used to perform a given task 


** Question : What would break at 10,000 users?
        - API cost 
        - API response time
        - Rate limiting 


** Question :  Three ways to reduce AI costs.
        - Intent clarification before llm call hence reducing llm calls
        - Reduce Prompt Size
            - Don;t sent entire conversastion to llm send only last fewer msg

        - Use right moel for task 
            - Clacification small chaep model we can use 
            - heavty reasioning we can use complex models

            