from controllers.scraper import WollPlatzScraper



def main():
    scraper = WollPlatzScraper(search_bar_id="searchSooqrTop", product_name="DMC Natura")
    scraper.get_product_data()

if __name__ == "__main__":
    main()