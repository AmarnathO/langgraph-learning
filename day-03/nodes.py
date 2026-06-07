from state import AgentState


def query(state: AgentState) -> AgentState:
    return {
        "query":state["query"]
    }


def intent(state: AgentState) -> AgentState:
     if "refund" in state["query"] :
        return {
            "intent": "refund"
        }
     elif "order status" in state["query"]:
        return {
            "intent": "order_status"
        }
     else:
        return {
            "intent": "general"
        }

def  answer(state:AgentState) -> AgentState:
    if state["intent"] == "refund":
        return {
            "answer": "Your refund has been processed"
        }
    elif state["intent"] == "order_status":
        return {
            "answer": "Your order has been shipped"
        }
    else:
        return {
            "answer": "Please can you connect us on +9187829293829"}

