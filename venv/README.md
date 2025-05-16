# UK Utility Tariff Tracker 🔌🇬🇧

A Python CLI tool that scrapes real-time utility tariff prices (e.g. from EDF, British Gas), compares them, and shows the cheapest provider.

## Features
- Live scraping of UK electricity/gas tariffs
- Compares unit rate + standing charge
- Alerts for cheapest provider

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/uk-utility-tariff-tracker.git
cd uk-utility-tariff-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python tracker/main.py


uk-utility-tariff-tracker/
├── data/
│   └── sample_tariffs.html       # Optional saved HTML for tests
├── tracker/
│   ├── __init__.py
│   ├── main.py                   # Main CLI entry point
│   ├── scraper.py                # Scraping logic
│   ├── analyzer.py               # Comparison logic
│   ├── utils.py                  # Helper functions
├── tests/
│   ├── test_scraper.py
│   ├── test_analyzer.py
├── requirements.txt
├── README.md
└── .gitignore
