def check_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        print(True)
    else:
        print(False)
    return text


print(check_palindrome('Кит на море не романтик'))
print(check_palindrome('test'))
