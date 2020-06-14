
import bs4
import time
import pandas as pd
from bs4 import BeautifulSoup
import selenium 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

entrada = (input("Digite a Ação: "))
tag = entrada.upper()


url = "https://br.tradingview.com/symbols/BMFBOVESPA-"+str(tag)+"/technicals/"

chrome_options = Options() 
chrome_options.headless = True 
driver = webdriver.Chrome(options=chrome_options) #
driver.get(url)
time.sleep(3)


# 1 dia
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 
table_dia = soup.find(class_ = 'table-1YbYSTk8')
table2_dia = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_dia = pd.read_html(str(table_dia))
medias_moveis_dia = pd.read_html(str(table2_dia))
sinal_dia = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_dia = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()

# 1 semana
semana = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[1]/div/div/div[1]/div/div/div[7]').click()
time.sleep(1)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 
table_semana = soup.find(class_ = 'table-1YbYSTk8')
table2_semana = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_semana = pd.read_html(str(table_semana))
medias_moveis_semana = pd.read_html(str(table2_semana))
sinal_semana = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_semana = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()

# 1 mes
mes = driver.find_element_by_xpath('//*[@id="technicals-root"]/div/div/div[1]/div/div/div[1]/div/div/div[8]').click()
time.sleep(1)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser')
table_mes = soup.find(class_ = 'table-1YbYSTk8')
table2_mes = soup.findAll(class_ = 'table-1YbYSTk8')[1]
osciladores_mes = pd.read_html(str(table_mes))
medias_moveis_mes = pd.read_html(str(table2_mes))
sinal_mes = soup.find('div', class_ = 'speedometerWrapper-1SNrYKXY summary-72Hk5lHE').find('span', class_ = 'speedometerSignal-pyzN--tL buyColor-4BaoBngr').get_text()
placar_mes = soup.findAll('div', class_ = 'countersWrapper-1TsBXTyc')[1].get_text()

time.sleep(1)
move_fund = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[5]/div/div[1]/div/a[1]').click()
time.sleep(5)
element = driver.find_element_by_xpath("/html/body")
html = element.get_attribute('outerHTML')
soup = BeautifulSoup(html, 'html.parser') 


financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[0]
valoracao = []
i = 0
for k in range(0, 10):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    valoracao.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[1]
historico_precos = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    historico_precos.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[2]
bp = []
i = 0
for k in range(0, 6):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    bp.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[3]
dividendos = []
i = 0
for k in range(0, 3):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    dividendos.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[4]
operacionais = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    operacionais.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[5]
margens = []
i = 0
for k in range(0, 4):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    margens.append(card)
    i = i + 1

financas = soup.find_all('div', class_ = 'tv-widget-fundamentals__item')[6]
renda = []
i = 0
for k in range(0, 10):
    card = {}
    card['nome'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__label apply-overflow-tooltip')[int(i)].get_text()[7:-7]
    card['valor'] = financas.find_all('span', class_ = 'tv-widget-fundamentals__value apply-overflow-tooltip')[int(i)].get_text()[7:-6]
    renda.append(card)
    i = i + 1



dataset1 = pd.DataFrame(valoracao)
dataset2 = pd.DataFrame(historico_precos)
dataset3 = pd.DataFrame(bp)
dataset4 = pd.DataFrame(dividendos)
dataset5 = pd.DataFrame(operacionais)
dataset6 = pd.DataFrame(margens)
dataset7 = pd.DataFrame(renda)


driver.quit()






