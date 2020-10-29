import lib.utils as util

scrap_dict = {
    'Product': [],
    'Price': [],
}

driver = './driver/chromedriver.exe'
browser = util.browser_init(driver_path=driver, headless=True)
browser = util.get_link(browser=browser, link='https://www.amazon.com.br')

search_input = browser.find_element_by_class_name('nav-input')
search_value = 'iPhone'

search_input.send_keys(search_value)
search_input.submit()

result_container = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]')
actual_product = ''

try:
    print('Obtendo dados ...')
    products_names = result_container.find_elements_by_css_selector('div span div div div h2 a span')

    for product_name in products_names:
        scrap_dict['Product'].append(product_name.get_attribute('innerHTML'))
        actual_product = result_container.find_element_by_css_selector(f'div[data-index="{products_names.index(product_name)}"]')
        try:
            product_price = actual_product.find_element_by_css_selector('div span.a-offscreen').get_attribute('innerHTML')
        except:
            product_price = 'R$ -'

        scrap_dict['Price'].append(product_price)
except:
    print('Erro!')
    pass

util.save_xlsx(dataframe=scrap_dict, file_name=f'Amazon {search_value} Scrape Result')

browser.quit()
