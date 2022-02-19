def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    open_bracket = "("
    closed_bracket = ")"
    if brackets_row == "":
        return True
    elif brackets_row[0] == open_bracket and brackets_row[-1] == closed_bracket\
            and brackets_row.count(open_bracket) == brackets_row.count(closed_bracket):
        return True
    else:
        return False
