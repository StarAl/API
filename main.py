from inf import get_translation



def main(text, lang):
    with open('output.txt', 'w', encoding='utf-8') as f:
        print('Выбери язык перевода: 1 - Английский, 2 - Русский, 3 - Немецкий, 4 - Китайский, 5 - Японский, 6 - Украинский, 7 - Французский, 8 - Латышский ')
        a = input()
        if '1' in a:
            print(*get_translation(input('=>'), 'en')['text'], file=f)
        elif '2' in a:
            print(*get_translation(input('=>'), 'ru')['text'], file=f)
        elif '3' in a:
            print(*get_translation(input('=>'), 'de')['text'], file=f)
        elif '4' in a:
            print(*get_translation(input('=>'), 'zh')['text'], file=f)
        elif '5' in a:
            print(*get_translation(input('=>'), 'zh')['text'], file=f)
        elif '6' in a:
            print(*get_translation(input('=>'), 'uk')['text'], file=f)
        elif '7' in a:
            print(*get_translation(input('=>'), 'fr')['text'], file=f)
        elif '8' in a:
            print(*get_translation(input('=>'), 'lv')['text'], file=f)






if __name__ == '__main__':
    main(open('input.txt', encoding='utf-8').read().strip(), 'ru')
