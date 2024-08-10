def test_dot_is_string():
    assert '.' == '.'

def test_dot_matches_regex():
    import re
    assert re.match(r'\.', '.') is not None
