""" Convert String numbers to int. """
from typing import Union
def convert_to_int(integer_string_with_commas: str) -> Union[int, None]:
    """ Converts numerical strings to become int. It handles various cases with punctuation.
        Returns None when something unusual happens. """
    assert isinstance(integer_string_with_commas, str)

    comma_separated_parts: list = integer_string_with_commas.split(",")
    for part in comma_separated_parts:
        print(comma_separated_parts)
        # Number of special cases
        if len(part) > 3:
            return None
        if part != 0 and len(part) != 3: # Skip over the 1st part since it could have 1 or 2
            return None

        # Create a single string by combining the parts
        integer_string_without_commas = "".join(comma_separated_parts)

        # Try, it will not work if you have a decimal still in the string
        try:
            return int(integer_string_without_commas)
        except ValueError:
            return None
