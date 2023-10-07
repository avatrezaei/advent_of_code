import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from d2c1 import calculate_final_position 

def test_calculate_final_position_sample():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "../input.txt")
    with open(file_path, "r") as file:
        commands = [line.strip() for line in file.readlines()] 
    horizontal, depth = calculate_final_position(commands)
    assert horizontal == 1815
    assert depth == 908
    assert horizontal * depth == (1815 * 908)

 


