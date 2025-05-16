import re

def parse_price(text):
    """Extract numeric value from price string e.g. '15.5p/kWh' or '£0.155'."""
    match = re.search(r"(\d+\.?\d*)", text)
    return float(match.group(1)) if match else None


def compare_tariffs(tariffs, monthly_kwh=300):
    """
    Compare tariffs based on monthly usage (default 300 kWh).
    Returns the cheapest tariff dictionary.
    """
    cheapest = None
    for t in tariffs:
        unit_rate = parse_price(t["unit_rate"])
        standing_charge = parse_price(t["standing_charge"])
        if unit_rate is None or standing_charge is None:
            continue

        monthly_cost = (unit_rate * monthly_kwh / 100) + (standing_charge * 30)
        # Unit rate might be in pence, convert pence to pounds by dividing by 100

        if cheapest is None or monthly_cost < cheapest["cost"]:
            cheapest = {
                "provider": t["provider"],
                "name": t["name"],
                "cost": monthly_cost
            }
    return cheapest
