import os
import argparse

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_url(headers, long_link):
    full_link = "https://api-ssl.bitly.com/v4/shorten"
    params ={
        "long_url": long_link
    }
    
    responce = requests.post(full_link, headers=headers, json=params)
    responce.raise_for_status()
    return responce.json()["link"]


def count_clicks(headers, abbreviated_link):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{abbreviated_link}/clicks/summary"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, abbreviated_link):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{abbreviated_link}"
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="write your link here")
    args = parser.parse_args()
    bitly_token = os.environ["BITLY_TOKEN"]
    headers = {"Authorization" : f"{bitly_token}"}
    url_parts = urlparse(args.link)
    netloc_link = url_parts.netloc
    path_link = url_parts.path
    abbreviated_link = f"{netloc_link}{path_link}"

    if is_bitlink(headers, abbreviated_link):
        try:
            clicks = count_clicks(headers, abbreviated_link)
            print("Кол-во кликов по этой ссылке:", clicks)
        except requests.exceptions.HTTPError as error:
            print(error)
    else:
        try:
            bitlink = shorten_url(headers, args.link)
            print(bitlink)
        except requests.exceptions.HTTPError as error:
            print(error)


if __name__ == '__main__':
    main()
