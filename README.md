# Advent of Code Solutions

This repository contains solutions for the Advent of Code challenges using the Test-Driven Development (TDD) approach. Each day and its corresponding challenges are organized into separate directories.


Each day has its challenges separated into different folders, and each folder contains:

- `main.py`: Contains the logic and functions to solve the challenge.
- `input.txt`: The puzzle input provided by Advent of Code.
- `test_main.py`: Contains tests written using the pytest framework.

## Setup and Running

### Prerequisites

- Python (Version 3.10 recommended)
- pytest (for running tests)

### Installation

1. Clone this repository:

```bash
git clone <repository-url>
```

Navigate to the repository's root directory:

```bash
cd <repository-directory>
```

Install the necessary Python packages:
```bash
pip install pytest
```

Running Tests
From the root directory, run:
```bash
pytest
```
This will run all the tests present in the repository.

#Coverage
To ensure the quality and correctness of the solutions, test coverage is being tracked. Coverage reports can be generated using the following command:
```bash
pytest --cov-report term --cov=.

```