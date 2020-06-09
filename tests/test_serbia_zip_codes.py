import serbia_zip_codes

def test_find_by_city():
    result = serbia_zip_codes.find_by_city("Loznica")
    assert result['city'] == "Loznica"
