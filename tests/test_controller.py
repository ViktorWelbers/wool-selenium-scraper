from unittest import TestCase


class Test_Woll_Scraper(TestCase):

    def setUp(self):
        """ Hier koennten MagicMocks stehen, die den Driver nachahmen"""
        pass

    def test_empty_products_returns_empty_dataframe(self):
        """ Hier koennte ein Unittest stehen, der kontrolliert, dass ein leeres Produkt auch ein Empty dataframe returned"""
        pass

    def test_product_found_return_filled_dataframe(self):
        """Hier koennte ein Unittest stehen, der mit Hilfe eines/mehrer Mocks kontrolliert, ob wir bei einem gefunden Produkt auch ein dataframe kriegen"""
        pass

    def test_no_hrefs_found_returns_empty_dataframe(self):
        """ Hier koennte ein Unittest stehen, der kontrolliert, dass bei einem nicht gefundenen Href auch ein leeres Dataframe returned wird"""
        pass

    def test_find_element_empty(self):
        """ Hier koennte ein test stehen, der bei nicht gefundenen elementen (Zusammenstellung etc.) kontrolliert, dass wir trotzdem ein funktionierendes Produkt haben"""
