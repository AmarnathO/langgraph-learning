# Langraph Notes
Q1 Why we need langgraph ?
- Eariler we were unable to implement 
    - Muti Agent orchestration
    - human in loops
    - Loop back in flows
    - If app Crashed then you lost data langrpah give option for state that hold data across
    - Stateful nodes 

Q2 : What is an LLM, Agent, Workflow 
    - llm are just large programs that are trained on huge data set and they can predict the next word based on user input.

    - Agent : These are program that can perform a given task based on reasoning and tools  to archive a goal

    - workflow : This is predefined flow of a program that can be used to perform a given task 


Q3 : What would break at 10,000 users?
        - API cost 
        - API response time
        - Rate limiting 

Q4 : Three ways to reduce AI costs.
        - Intent clarification before llm call hence reducing llm calls
        - Reduce Prompt Size
            - Don;t sent entire conversastion to llm send only last fewer msg

        - Use right moel for task 
            - Clacification small chaep model we can use 
            - heavty reasioning we can use complex models

            