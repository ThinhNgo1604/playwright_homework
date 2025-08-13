import warnings

def test_warning():
    warnings.warn("Cảnh báo demo", UserWarning)
    assert True
