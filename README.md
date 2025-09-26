# 🎭 Python Test Automation Framework

A comprehensive test automation framework using Python, Pytest, and Playwright for web testing and API testing.

## 📁 Project Structure
```
python-playwright-demo/
├── configs/              # Configuration management
│   ├── configs.py       # Configuration classes
│   └── .env.dev         # Environment variables
├── constants/           # Constant definitions
├── core/               # Core framework components
│   ├── api/            # Base API functionality
│   ├── db/             # Database functionality
│   ├── page/           # Base page functionality
│   └── utils/          # Core utilities
├── data/               # Test data files
│   ├── endpoints/      # API endpoint definitions
│   └── test_data/      # Test data files
├── pages/              # Page Objects
│   ├── locators/       # Page element locators
│   └── pages/          # Page object implementations
├── services/            # Business logic and data access
│   ├── api/            # API services
│   │   ├── clients/    # API client implementations
│   │   ├── endpoints/  # API endpoint definitions
│   │   └── models/     # API data models
│   ├── controllers/    # Business logic controllers
│   └── db/             # Database services
│       ├── entites/    # Database entities
│       └── mock_data/  # Mock data clients
├── tests/              # Test suites
│   ├── api/            # API tests
│   └── ui/             # UI tests
├── reports/            # Test reports
│   ├── allure/         # Allure reports
│   ├── html/           # HTML reports
│   ├── screenshots/    # Test failure screenshots
│   └── videos/         # Test execution videos
├── venv311/            # Virtual environment
├── conftest.py         # Pytest configuration
├── pytest.ini         # Pytest settings
├── docker-compose.yml  # Docker configuration
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## 🧰 Requirements

- Python 3.11+ (do **not** use Python 3.13 — `greenlet` won't compile)
- macOS or Linux or window
- Playwright with browser binaries

## 🚀 Setup Instructions

1. Create and activate virtual environment:
```bash
python3.11 -m venv venv311
source venv311/bin/activate  # On Windows: venv311\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

## 🎮 Running Tests

### Basic Test Execution
```bash
# Run all tests
pytest

# Run UI tests
pytest tests/test_saucedemo.py

# Run API tests
pytest tests/api/

# Run with verbose output
pytest -v
```

### Test Configuration Options
```bash
# Run tests in headed mode (visible browser)
pytest --headed

# Run tests with specific browser
pytest --browser firefox

# Run tests with specific environment
pytest --env staging
```

## 📊 HTML Reports
Tests automatically generate HTML reports in the `reports` directory, including:
- Test execution summary
- Environment information
- Test case details and execution time
- Screenshots of failed tests

## ⚙️ Environment Configuration

Environment variables are stored in `configs/.env.[environment]` files:
```bash
BASE_URL=https://www.saucedemo.com/
HEADLESS=false
RECORD_VIDEO=false
```

## 🎯 Testing Patterns

### Page Object Model
The framework follows the Page Object Model pattern for UI testing:

```python
def test_login(self):
    self.login_page.goto(Configs.get().BASE_URL)
    self.login_page.login()
    self.home_page.verify_home_page_displays()
```

### API Client Pattern
API testing uses a structured client pattern with response models:

```python
def test_ip_lookup(self):
    response = self.ip_client.get_basic_standard_ip_lookup("134.201.250.155")
    ip_response = IPResponse.from_dict(response.json())
    
    assert ip_response.country_name == "United States"
    assert ip_response.city == "Huntington Beach"
```

## ✨ Features

- ✅ Page Object Model architecture
- ✅ Multi-environment support
- ✅ HTML reporting with screenshots
- ✅ Cross-browser testing support
- ✅ Configuration management
- ✅ Automatic screenshot capture on failure
- ✅ Clean and maintainable test structure
- ✅ API testing with request/response models
- ✅ Structured API client architecture


## 🔧 Troubleshooting

- If you get build errors with `greenlet`, make sure you're not using Python 3.13
- For Mac M1/M2 users, use native ARM64 Python:
  ```bash
  brew install python@3.11
  ```

## 📚 References

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model](https://playwright.dev/python/docs/pom)
- [Requests Library](https://requests.readthedocs.io/)
- [Python Data Classes](https://docs.python.org/3/library/dataclasses.html)

---

Happy Testing! 🚀
