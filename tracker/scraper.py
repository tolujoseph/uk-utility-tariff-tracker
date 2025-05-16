import requests
from bs4 import BeautifulSoup

def get_edf_tariffs():
    url = "https://www.edfenergy.com/energy/electricity-tariffs"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching EDF tariffs: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    tariffs = []

    # Note: selectors might change, this is a simple example scraping titles & prices
    for block in soup.select("div.tariff-block"):
        name_el = block.select_one("h3")
        unit_rate_el = block.select_one(".unit-rate")
        standing_charge_el = block.select_one(".standing-charge")

        if not (name_el and unit_rate_el and standing_charge_el):
            continue

        name = name_el.get_text(strip=True)
        unit_rate = unit_rate_el.get_text(strip=True)
        standing_charge = standing_charge_el.get_text(strip=True)

        tariffs.append({
            "provider": "EDF",
            "name": name,
            "unit_rate": unit_rate,
            "standing_charge": standing_charge
        })

    return tariffs


def get_britishgas_tariffs():
    url = "https://www.britishgas.co.uk/electricity-tariffs"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching British Gas tariffs: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    tariffs = []

    for block in soup.select("div.tariff-info"):
        name_el = block.select_one("h2")
        unit_rate_el = block.select_one(".unit-cost")
        standing_charge_el = block.select_one(".standing-charge")

        if not (name_el and unit_rate_el and standing_charge_el):
            continue

        name = name_el.get_text(strip=True)
        unit_rate = unit_rate_el.get_text(strip=True)
        standing_charge = standing_charge_el.get_text(strip=True)

        tariffs.append({
            "provider": "British Gas",
            "name": name,
            "unit_rate": unit_rate,
            "standing_charge": standing_charge
        })

    return tariffs
