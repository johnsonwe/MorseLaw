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
    print(' '.join(new_text))


def search(phrase):
    cookies = {
        'ASP.NET_SessionId': 'ervja3vcyqg51q503aewmm1d',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'RequestVerificationToken': 'M8E3A_g8oafHJ1cmxaTPVbM2m5qsCNtkc6OqMCGXlt1DXK7uxHXwmAis0ZEQYqAN4VrhReW-CpCbLOgGSvzoZj3AaQoCaHJ7b1MQLTTRR_bZVV2XFWJEyooDzKyExtmQLCWS1gXsi5sTzUnOpYKbIw2:ef3Oog4yVN00vSXZHI3-3uNveVNQ3NV8m22SwoAbX0CVvyTyddHSknuscbwEYJoS-tcuW-97J3XkAprS-9bNjy41vl66bsWralNaQfdekVgS2ikfMiLHdfUV5zTyXhyvhIwToO91WDD_XOd5mMabJ7oPqb4vnxsyWpH-MJOHZQs1',
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
    return response.json()[0]


def main():
    # search_phrase = input("what would you like to search?")
    search_phrase = "funeral interference"
    results = search(search_phrase)
    print(results)
    response = requests.get(results["RSN"])
    open('pdf.pdf', 'wb').write(response.content)
    text = textract.process(join(getcwd(), "pdf.pdf"))
    print(text)


if __name__ == '__main__':
    # convertToMorseCode('yo momma!')
    main()
