import pandas as pd

from app.controllers.scraper import WollPlatzScraper


def handler():
    output_df = pd.DataFrame()
    df = pd.read_csv('Wolldaten.csv', sep=';')
    for index, row in df.iterrows():
        product_name = row['Marke'] + ' ' + row['Bezeichnung']
        scraper = WollPlatzScraper(search_bar_id="searchSooqrTop")
        product_df = scraper.get_product_data(product_name=product_name)
        if not product_df.empty:
            if output_df.empty:
                output_df = product_df
            else:
                output_df = pd.concat([product_df, output_df], ignore_index=True)
    output_df.to_csv('scraped_data.csv')


if __name__ == "__main__":
    handler()
