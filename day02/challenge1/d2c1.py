def calculate_final_position(commands):
    horizontal_position = 0
    depth = 0

    for command in commands:
        action, value = command.split()
        value = int(value)

        if action == "forward":
            horizontal_position += value
        elif action == "down":
            depth += value
        elif action == "up":
            depth -= value

    return horizontal_position, depth
