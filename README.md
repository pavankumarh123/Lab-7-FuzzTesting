
# Lab 7 - Fuzz Testing

## Project Title
Fuzzing for Input Validation Bugs using Python and Hypothesis.

## Objective
To identify and fix input validation bugs using
property-based fuzz testing.

## Technologies Used
- Python
- Pytest
- Hypothesis

## Functions Tested
1. parse_int_list()
2. sanitize_string()
3. safe_average()

## Testing Methodology
- Generate random inputs using Hypothesis.
- Test unexpected and invalid inputs.
- Identify input validation problems.
- Fix the application functions.
- Run tests again to verify the fixes.

## Installation

pip install -r requirements.txt

## Run Application

python processor.py

## Run Tests

python -m pytest test_processor.py -v

## Expected Result
All tests should pass after fixing the application.

## Deliverables
- processor.py
- test_processor.py
- README.md
- requirements.txt
- Screenshots of execution and test results
