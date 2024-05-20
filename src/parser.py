import requests

from bs4 import BeautifulSoup


# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Origin': 'https://www.banki.ru',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.banki.ru/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'no-cors',
#     'Sec-Fetch-Site': 'cross-site',
#     # 'Content-Length': '0',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
# }

# response = requests.post(
#     'https://www.banki.ru/products/currency/cb/',
#     headers=headers,
# )


response = requests.get("https://www.banki.ru/products/currency/cb/")
soup = BeautifulSoup(response.text, "lxml")

def get_currencies():
    res = []

    for entry in soup.find_all("section", {"class": "Panel__sc-1g68tnu-1 JpzER currencyCbListItemstyled__StyledPanel-sc-12ajhcx-0 dhonLt"}):
        res.append(entry)
    
    return res


def get_currency_soup(currency_name: str):
    for currency in get_currencies():
        if currency.find("div", {"class": "Text__sc-j452t5-0 hDxmZl"}).text == currency_name:
            return currency
    
    return None


def get_currencies_name() -> list[str]:
    result = []

    for currency in get_currencies():
        result.append(currency.find("div", {"class": "Text__sc-j452t5-0 hDxmZl"}).text)
    
    return result


def load_currency(currency_soup) -> str:
    name = currency_soup.find("div", {"class": "Text__sc-j452t5-0 hDxmZl"}).text
    exchange_rate = currency_soup.find("div", {"class": "Text__sc-j452t5-0 jxxlPG"}).text
    change = currency_soup.find("div", {"class": "Text__sc-j452t5-0 jxxlPG currencyCbListItemstyled__StyledDifference-sc-12ajhcx-3 cLursz"})
    if change is None: change = currency_soup.find("div", {"class": "Text__sc-j452t5-0 jxxlPG currencyCbListItemstyled__StyledDifference-sc-12ajhcx-3 cqwmvW"})

    return f"{name}: {exchange_rate} {change.text}"


def get_all_currency_data() -> list[str]:
    result = []

    for currency in get_currencies():
        result.append(load_currency(currency))
    
    return result
       
