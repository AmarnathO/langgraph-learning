state = {
    "name": "Amar",
    "Profile": "TPM"
}

# updating state 
def update_skill(state):
    state["skill"] = ["python", "java", "c++"]
    return state


updated_state = update_skill(state)
print(updated_state)


# Chain mutiple update 
state = {
    "Topic":"AI"
}

state = update_skill(state)
print(state)
