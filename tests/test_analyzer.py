from tracker.analyzer import compare_tariffs

def test_compare_tariffs():
    tariffs = [
        {"provider": "A", "name": "Test1", "unit_rate": "15p/kWh", "standing_charge": "20p"},
        {"provider": "B", "name": "Test2", "unit_rate": "14p/kWh", "standing_charge": "22p"},
    ]
    cheapest = compare_tariffs(tariffs)
    assert cheapest["provider"] == "B"
