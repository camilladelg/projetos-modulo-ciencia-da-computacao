def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string_lower = first_string.lower()
    second_string_lower = second_string.lower()

    if (
        len(first_string_lower) != len(second_string_lower)
        or first_string_lower == ""
        or second_string_lower == ""
    ):
        return False
    else:
        for string in first_string_lower:
            if first_string_lower.count(string) != second_string_lower.count(
                string
            ):
                return False
        return True
