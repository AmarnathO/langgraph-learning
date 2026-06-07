from langgraph.graph import START, END, StateGraph
from state import AgentState
from nodes import *

# define grapoh 
graph = StateGraph(AgentState)

# Making node
graph.add_node("query", query)
graph.add_node("intent", intent)
graph.add_node("answer", answer)

# making edges
graph.add_edge(START, "query")
graph.add_edge("query", "intent")
graph.add_edge("intent", "answer")
graph.add_edge("answer", END)

# invoking graph 
app = graph.compile()

response =app.invoke({
    "query": "I want to refund my payment - It deducted from my account and order didn;t get confirmed",
    "intent": "",
    "answer": ""

})


print(response["answer"])