try:
    import fizzbuzz
    print("Successfully imported fizzbuzz module")
    result = fizzbuzz.fizzbuzz(15)
    print("fizzbuzz(15) =", result)
    print("Type of result:", type(result))
    print("Is list?", isinstance(result, list))
except Exception as e:
    print(f"Error: {e}")
