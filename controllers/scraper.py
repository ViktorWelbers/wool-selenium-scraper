import time
from abc import ABC, abstractmethod

import pandas as pd
from fastapi.encoders import jsonable_encoder
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from models.models import Product


class ProductScraper(ABC):

    def __init__(self, search_bar_id: str, product_name: str):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
        self.search_bar_id = search_bar_id
        self.product_name = product_name

    @abstractmethod
    def get_product_data(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def url(self):
        raise NotImplementedError


class WollPlatzScraper(ProductScraper):
    url = 'https://www.wollplatz.de/'

    def get_product_data(self):
        products = []

        self.driver.get(self.url)
        search_bar = self.driver.find_element(by=By.ID, value=self.search_bar_id)
        search_bar.send_keys(self.product_name)
        time.sleep(1)
        search_bar.send_keys(Keys.RETURN)

        webelements = self.driver.find_elements(By.XPATH, f"//*[contains(text(),'{self.product_name}')]")
        hrefs = [product.get_attribute('href') for product in webelements]
        names = [product.get_attribute('title') for product in webelements]
        for idx, href in enumerate(hrefs):
            self.driver.get(href)
            nadel_str = self.driver.find_element(By.XPATH,
                                                 "//td[normalize-space() = 'Nadelstärke']/following-sibling::td").text
            zusammenstellung = self.driver.find_element(By.XPATH,
                                                        "//td[normalize-space() = 'Zusammenstellung']/following-sibling::td").text
            preis = float(self.driver.find_element(By.CLASS_NAME, "product-price-amount").text)
            products.append(
                Product(name=names[idx], nadel_str=nadel_str, href=href, zusammenstellung=zusammenstellung,
                        preis=preis))
        product_df = pd.DataFrame(jsonable_encoder(products))
        if product_df:
            product_df.to_sql()
