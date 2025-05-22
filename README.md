# Steam Website Test Suite

This project contains various types of automated tests for the Steam website using Python and Selenium.

## Project Structure

```
steam_tests/
├── tests/
│   ├── performance/         # Load, stress, and endurance tests
│   ├── functional/          # Functional test cases
│   ├── ui/                  # UI test cases
│   └── api/                 # API test cases
├── utils/                   # Utility functions and helpers
├── config/                  # Configuration files
└── reports/                 # Test reports
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env` file:
```
STEAM_URL=https://store.steampowered.com
```

## Running Tests

### Performance Tests
```bash
# Run Locust load tests
locust -f tests/performance/locustfile.py

# Run stress tests
pytest tests/performance/test_stress.py
```

### Functional Tests
```bash
pytest tests/functional/
```

### UI Tests
```bash
pytest tests/ui/
```

### API Tests
```bash
pytest tests/api/
```

## Test Reports

Test reports are generated in the `reports` directory after test execution. 