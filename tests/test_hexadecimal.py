from src.utils import return_hexadecimal

def test_return_hexadecimal():
    
    """Test decimal-to-hex conversion for multiple inputs."""
    # Arrange
    test_cases = [
        (0, "0"),
        (10, "A"),
        (255, "FF"),
        (4096, "1000"),
        (16, "10"),
    ]
    # Act
    for decimal_number, expected_hexadecimal in test_cases:
        result = return_hexadecimal(decimal_number)
        # Assert
        assert result == expected_hexadecimal, (
            f"Failed for {decimal_number}: Expected '{expected_hexadecimal}', got '{result}'"
        )