def palidrome(word: str) -> bool:
    word = (
        word.lower()
        .replace(' ', '')
        .replace('á', 'a')
        .replace('é', 'e')
        .replace('í', 'i')
        .replace('ó', 'o')
        .replace('ú', 'u')
        .replace(',', '')
    )

    if word == word[::-1]:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} not is a palindrome')


if __name__ == '__main__':
    word = input('write a word: ')
    palidrome(word)
