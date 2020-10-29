from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame
from tkinter import filedialog
import os


def browser_init(driver_path, headless=True):
    print('Configurando acesso à Internet ...')
    options = Options()

    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    return browser


def get_link(browser, link):
    print('Conectando e acessando o Link ...')
    browser.get(link)

    return browser


def save_xlsx(dataframe, file_name):
    print('Escolha um lugar para salvar sua Planilha:')

    while True:
        try:
            save_path = filedialog.askdirectory()

            df = DataFrame(data=dataframe)
            df.to_excel(
                excel_writer=f'{save_path}/{file_name}.xlsx',
                sheet_name='Scrape Result',
                index=False,
                na_rep='-',
            )

            input('Sucesso! Aperte "Enter" para finalizar o Programa ...')

            os.startfile(f'{save_path}/{file_name}.xlsx')

            break
        except:
            print('Você precisa escolher um diretório para salvar a planilha ...')

