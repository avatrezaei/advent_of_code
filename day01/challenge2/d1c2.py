def count_increases_sliding_window(depths, window_size=3):
    previous_sum = sum(depths[:window_size])
    increase_count = 0
    
    for i in range(1, len(depths) - window_size + 1):
        current_sum = sum(depths[i:i + window_size])
        if current_sum > previous_sum:
            increase_count += 1
        previous_sum = current_sum

    return increase_count
