# studious-broccoli

Python virtual environment for the studious-broccoli project.

## Setup the project
create a python environment with the following command:<br>
> python3 -m venv venv

activate the environment with the following command:
> source venv/bin/activate

install the requirements with the following command:
> pip install -r requirements.txt

## How to run
Run the project with the following command:
> python3 main.py

## Testing manually
You can modify to test on different inputs by adding new nums variable in `main.py` calling `DataCapture.add(num: int)`.<br>

## How to run the tests
> pytest

## How to run type checking
> mypy main.py

## Requirements
- Python 3.x
- pytest
- mypy
- venv

## CI pipeline
The CI pipeline is configured to run the tests and type checking on every push to the master branch.
