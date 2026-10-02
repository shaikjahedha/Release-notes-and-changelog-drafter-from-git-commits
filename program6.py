state = {
    "done": False,
    "steps": [],
    "success": [],
    "failure": []
}

def process(state, step, success):
    state["steps"].append(step)

    if success:
        state["success"].append(step)
        return "Success"
    else:
        state["failure"].append(step)
        return "Failure"


result = process(state, "Login", True)
print(result)

result = process(state, "Data validation", False)
print(result)

print(state)