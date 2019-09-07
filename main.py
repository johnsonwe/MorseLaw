import requests
from urllib.parse import quote


def main():
    search_phrase = input("what would you like to search?")

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
        ('searchPhrase', search_phrase),
        ('statuteRange', 'on'),
        ('startRange', '1'),
        ('endRange', '999'),
        ('X-Requested-With', 'XMLHttpRequest'),
    )


    response = requests.get('https://apps.legislature.ky.gov/LRCSearch/Home/getStatuteJSON', headers=headers,
                            params=params, cookies=cookies)
    print(response.text)


if __name__ == '__main__':
    main()
