def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        raise TypeError("Input must be a dictionary")
    
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")
    
    dct[key] = value
    return dct


# Task 2

# Scenario 1: Empty dictionary, adding a new key-value pair
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Output: {'name': 'Alice'}

# Scenario 2: Key already exists, should print original value and then update
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)  # Output: Original value for key 'age': 25
               #         {'age': 26}

