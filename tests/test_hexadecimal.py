from src.utils import return_hexadecimal

def test_return_hexadecimal():
    """Test decimal-to-hex conversion (with '0x' prefix)."""
    test_cases = [
        (0, "0x0"),
        (10, "0xa"),
        (255, "0xff"),
        (4096, "0x1000"),
        (16, "0x10"),
    ]
    for decimal_number, expected_hexadecimal in test_cases:
        result = return_hexadecimal(decimal_number)
        assert result == expected_hexadecimal, (
            f"Failed for {decimal_number}: Expected '{expected_hexadecimal}', got '{result}'"
        )