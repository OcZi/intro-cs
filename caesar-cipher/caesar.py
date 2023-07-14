# Salvador Donayre - Introd. CS


def E(m, k):
    return apply_caeser(m, k)


def D(m, k):
    return apply_caeser(m, -k)


def apply_caeser(m, k):
    """
    Apply Caeser cipher to the message parameter with k jumps
    :param m: string message
    :param k: k jumps
    :return: output of caeser cipher
    """
    new_m = ""
    for letter in m:
        # Apply k jumps to letter and concatenate it
        new_m += move_ascii(letter, k)
    return new_m


def move_ascii(letter, num):
    """
    Move letter around ascii table
    :param letter: letter to move
    :param num: number of jumps to move
    :return: new letter
    """

    # Ignore non-alphabet characters
    if not letter.isalpha():
        return letter

    # Get code letter
    code_letter = ord(letter)
    # Check if letter is in upper letter range
    upper = code_letter > 90

    # Calculate diff of code letter to be 0
    diff = 65 + (upper * 32)
    # Remove diff to calculate lower and upper letters as the same
    code_letter -= diff

    # Calculate new letter inside the alphabet
    index = (code_letter + num) % 26
    # Add diff to return his upper/lower state
    index += diff
    return chr(index)
