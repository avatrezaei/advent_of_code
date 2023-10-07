import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import count_increases 

def test_count_increases_from_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "input.txt")
    with open(file_path, "r") as file:
        depths = [int(line.strip()) for line in file.readlines()]
    result = count_increases(depths) 
    assert result == 1709

