import time
from abc import ABC, abstractmethod

import pandas as pd
from fastapi.encoders import jsonable_encoder
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from app.models.models import Product


class ProductScraper(ABC):
    def __init__(self, search_bar_id: str):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
        self.search_bar_id = search_bar_id

    @abstractmethod
    def get_product_data(self, **args) -> DataFrame | None:
        raise NotImplementedError

    @property
    @abstractmethod
    def url(self):
        raise NotImplementedError


class WollPlatzScraper(ProductScraper):
    url = 'https://www.wollplatz.de/'

    def get_product_data(self, product_name: str) -> DataFrame:
        products = []

        self.driver.get(self.url)
        search_bar = self.driver.find_element(by=By.ID, value=self.search_bar_id)
        search_bar.send_keys(product_name)
        time.sleep(1)
        search_bar.send_keys(Keys.RETURN)

        webelements = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{product_name}')]")
        if len(webelements) == 0:
            return pd.DataFrame()
        hrefs = [product.get_attribute('href') for product in webelements]


        for elem in hrefs:
            if elem is None:
                continue
            self.driver.get(elem)
            nadel_str = self.driver.find_element(By.XPATH,
                                                 "//td[normalize-space() = 'Nadelstärke']/following-sibling::td").text
            zusammenstellung = self.driver.find_element(By.XPATH,
                                                        "//td[normalize-space() = 'Zusammenstellung']"
                                                        "/following-sibling::td").text
            preis = float(self.driver.find_element(By.CLASS_NAME, "product-price-amount").text.replace(',', '.'))

            products.append(
                Product(name=product_name, nadel_str=nadel_str, href=elem, zusammenstellung=zusammenstellung,
                        preis=preis))
        if len(products) == 0:
            return pd.DataFrame()
        return pd.DataFrame(jsonable_encoder(products))
