def calculate_final_position_v2(commands):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        action, value = command.split()
        value = int(value)

        if action == "forward":
            horizontal_position += value
            depth += aim * value
        elif action == "down":
            aim += value
        elif action == "up":
            aim -= value

    return horizontal_position, depth
