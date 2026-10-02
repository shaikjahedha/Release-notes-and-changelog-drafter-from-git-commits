def perform_action(action):
    valid_actions = ["start", "stop"]

    if action not in valid_actions:
        return {"error": "Invalid action"}

    return {"status": action}


print(perform_action("pause"))