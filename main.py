import requests

import textract
from collections import defaultdict
from os import getcwd
from os.path import join


def convertToMorseCode(text):
    # clean it, convert it, return it
    MORSE_CODE_DICT = defaultdict(str)
    MORSE_CODE_DICT.update({'A': '.-', 'B': '-...',
                            'C': '-.-.', 'D': '-..', 'E': '.',
                            'F': '..-.', 'G': '--.', 'H': '....',
                            'I': '..', 'J': '.---', 'K': '-.-',
                            'L': '.-..', 'M': '--', 'N': '-.',
                            'O': '---', 'P': '.--.', 'Q': '--.-',
                            'R': '.-.', 'S': '...', 'T': '-',
                            'U': '..-', 'V': '...-', 'W': '.--',
                            'X': '-..-', 'Y': '-.--', 'Z': '--..',
                            '1': '.----', '2': '..---', '3': '...--',
                            '4': '....-', '5': '.....', '6': '-....',
                            '7': '--...', '8': '---..', '9': '----.',
                            '0': '-----', ', ': '--..--', '.': '.-.-.-',
                            '?': '..--..', '/': '-..-.', '-': '-....-',
                            '(': '-.--.', ')': '-.--.-'})
    text = text.upper()
    new_text = []
    for char in text:
        new_text.append(MORSE_CODE_DICT[char])
    return ' '.join(new_text)


def search(phrase):
    cookies = {
        'ASP.NET_SessionId': 'ervja3vcyqg51q503aewmm1d',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'RequestVerificationToken': 'CUXTJLtT-FuTCeb8F_UfKGkn_4wH6MY5Ox6LBPR-a4WWB7s42cN7Se4X5-_5A7m98AtppitxWH58-HtRzSz_08PQPNZJ6-JZGzcWuL9SFUujZQAxe2R_YnD9A4vT3dCCi49Gxc37JjHsuTDS5JSg0Q2:CMp9KAFlIfFYoSScfKPzQwHxJm2ERi7uCRL3n48OsR-xQiw2PznWxCt504SnS1ttZxZRjs_X3uLJJrapB_slqi0JtGftCt4Z3BjdrIJJAhhJTjPDfR2I04GvfuP8latwmXPlPibLR8lxNiAGI1QPPtr55LdwFtm-qfNWRAoaStg1',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://apps.legislature.ky.gov/lrcsearch',
        'TE': 'Trailers',
    }

    params = (
        ('searchPhrase', phrase),
        ('statuteRange', 'on'),
        ('startRange', '1'),
        ('endRange', '999'),
        ('X-Requested-With', 'XMLHttpRequest'),
    )

    response = requests.get('https://apps.legislature.ky.gov/LRCSearch/Home/getStatuteJSON', headers=headers,
                            params=params, cookies=cookies)
    pdf_response = requests.get(response.json()[0]["RSN"])
    with open('results.pdf', 'wb') as fileobj:
        fileobj.write(pdf_response.content)
    text = textract.process(join(getcwd(), 'results.pdf'))
    text = text.decode("utf-8")
    return text


def main():
    # search_phrase = input("what would you like to search?")
    search_phrase = "funeral interference"
    text = search(search_phrase)
    print(text)


if __name__ == '__main__':
    main()
