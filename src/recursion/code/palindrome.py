def palindrome(text):
    if len(text) in [0, 1]:
        return True
    if text[0] == ' ':
        return palindrome(text[1:])
    if text[-1] == ' ':
        return palindrome(text[:-1])
    if text[0].lower() == text[-1].lower():
        return palindrome(text[1:-1])
    return False


print(palindrome('Maciek'))  # False
print(palindrome('Wół utył i ma miły tułów'))  # True
print(palindrome('Rats live on no evil star'))  # True
