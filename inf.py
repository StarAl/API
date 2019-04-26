import requests

def get_html(url):
    return requests.get(url).text


def save_file(url, name):
    r = requests.get(url, stream=True)
    with open(name, 'bw') as f:
        f.write(r.content)

def get_translation(text: object, lang: object) -> object:
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    KEY = 'trnsl.1.1.20190419T134100Z.390c252a6b66a6e9.0118dceadf388c22142e01c241a6385e0b7b17a2'
    TEXT = text
    LANG = lang

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return eval(r.text)