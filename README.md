# GameLoft Test - Matching players with campaigns

This is my take on the technical test aiming to match a player with active campaigns based on their profile.
I have use mocked data to simulate retrieving a player's profile and a list of campaigns.
I have added unit tests to handle several use cases and error handling.

## Features

- Retrieve a player's profile from a mocked database.
- Fetch active campaigns from a mocked service.
- Check matching criteria (level, country, inventory).
- Update player's profile once a match campaign is found.
- Handle errors if player ID is not found
- Unit tests to validate several use cases

## Installation

Install dependancies :
I have Python 3.12 installed. Make sure you have Python, then run:

```bash
   pip install -r requirements.txt
```

## Usage

To run the script and simulate matchmaking:
```bash
   python src\profile_matcher.py
```

## Tests

This project uses pytest for unit testing.

1. Run tests:
   ```bash
   pytest
   ```
2. Run tests with coverage:
   ```bash
   pytest --cov=src --cov-report=term
   ```
3. Generate a detailed coverage report:
   ```bash
   pytest --cov=src --cov-report=html
   ```
Then open htmlcov/index.html in your browser to view the detailed coverage report.
