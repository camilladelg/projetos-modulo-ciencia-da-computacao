def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "" or word[low_index] != word[high_index]:
        return False
    elif high_index - low_index == 0 or high_index - low_index == 1:
        return True
    low_index += 1
    high_index -= 1
    return is_palindrome_recursive(word, low_index, high_index)
