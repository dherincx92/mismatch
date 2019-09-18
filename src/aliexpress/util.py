import argparse
import json
import logging
import os
import pickle
import requests

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup
from selenium import webdriver

from src.constants import (
    ALI_BASE,
    ALI_SEARCH
)



def run(args_dict):

    cookies_fp = args_dict['cookies']
    driver = webdriver.Chrome(os.path.realpath('chromedriver'))
    driver.get("https://aliexpress.com")
    cookies = pickle.load(open(cookies_fp, "rb"))
    for cookie in cookies:
        try: del cookie['expiry']
        except KeyError: pass
        driver.add_cookie(cookie)

    logger.info(f'ADDED LOGIN COOKIES TO SELENIUM:')

    product = args_dict['query']
    url = f"{ALI_BASE}{ALI_SEARCH}{product}"

    logger.info(f'CREATED URL: {url}')

    driver.get(url)

    content = driver.page_source

    # logger.info(f'REQUEST STATUS: {req.status_code}')

    soup = BeautifulSoup(content, 'html.parser')

    import ipdb; ipdb.set_trace()


    logger.info(f'{len(product_data)} listings for {product.upper()} found.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find prices for product based on metropolitan area'
    )
    parser.add_argument(
        '-q', '--query',
        required=True,
        type=str,
        help='Product query to find prices for.'
    )
    parser.add_argument(
        '-c', '--cookies',
        required=True,
        type=str,
        help='Path to AliExpress login pickle. See cookies.py.'
    )

    args_dict = vars(parser.parse_args())

    run(args_dict)
