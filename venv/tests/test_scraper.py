from tracker.scraper import get_edf_tariffs, get_britishgas_tariffs

def test_edf_scraper():
    data = get_edf_tariffs()
    assert isinstance(data, list)

def test_bg_scraper():
    data = get_britishgas_tariffs()
    assert isinstance(data, list)
