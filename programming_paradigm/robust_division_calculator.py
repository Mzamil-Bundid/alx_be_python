def safe_divide(numerator, denominator):
    """Perform division with error handling for non-numeric inputs and division by zero."""
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."