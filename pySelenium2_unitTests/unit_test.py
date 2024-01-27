
from car import Car

def test_gastype_not_diesel():
    # Arrange
    volvo_s90 = Car("Volvo", "S90", 2)

    # Act
    result = volvo_s90.convert_gas()

    # Assert
    assert result == "Regular"
    #assert result != "Regular", "Gas Type is wrong"
