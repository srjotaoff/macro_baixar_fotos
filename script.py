from tkinter import Tk
from tkinter.filedialog import askopenfilename

import time
from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


ttl_ls = int(0)
ttl_ft = int(0)
ttl_ft_sucesso = int(0)
ttl_ft_erro = int(0)


input ('Selecione o arquivo .txt com a lista de codigos de barra: ')
Tk().withdraw()
local = askopenfilename()
print(f'\n{local}\n')

arquivo = open(local,'r')
for linha in arquivo:
	ttl_ls = (ttl_ls + 1)
arquivo.close()


playwright = sync_playwright().start()
navegador = playwright.chromium.launch(headless = False)

print('\nIniciando instancia web - - - BLUESOFT\n')
pagina = navegador.new_page()


def eanpictures(linha):
	try:
		linha = linha.rstrip()
		pagina.goto(f'http://www.eanpictures.com.br:9000/api/gtin/{linha}')
		time.sleep(1)

		if pagina.query_selector('xpath=/html/body/b') is not None:
			print(f'{linha} - nenhuma foto encontrada para o produto no servidor da EAN PICTURES!')
			time.sleep(1)
			return(False)
		
		else:
			pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			print(f'{linha} - foto do produto baixada com sucesso pelo servifor da EAN PICTURES!')
			time.sleep(1)
			return(True)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da EAN PICTURES!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da EAN PICTURES!')
		time.sleep(1)
		return(False)
	

def marsil(linha):
	try:
		linha = linha.rstrip()
		pagina.goto(f'https://catalogo.marsil.com.br/uploads/catalogos/produtos/{linha}.jpg')
		time.sleep(1)

		if pagina.locator('xpath=/html/head/title').text_content() == 'Oppsss, nada encontrado! - Marsil Atacadista' :
			print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MARSIL!')
			time.sleep(1)
			return(False)
		
		else:
			pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			print(f'{linha} - foto do produto baixada com sucesso pelo servifor da MARSIL!')
			time.sleep(1)
			return(True)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MARSIL!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MARSIL!')
		time.sleep(1)
		return(False)
	

def maxxi(linha):
	try:
		linha = linha.rstrip()
		pagina.goto(f'https://maxxieconomica.com/storage/photos/1/Products/ean/{linha}.jpg')
		time.sleep(1)

		if pagina.locator('xpath=/html/head/title').text_content() == 'Maxxi Econômica || DASHBOARD' :
			print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MAXXI!')
			time.sleep(1)
			return(False)
		
		else:
			pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			print(f'{linha} - foto do produto baixada com sucesso pelo servifor da MAXXI!')
			time.sleep(1)
			return(True)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MAXXI!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da MAXXI!')
		time.sleep(1)
		return(False)


def cosmos(linha):
	try:
		linha = linha.rstrip()
		pagina.goto(f'https://cdn-cosmos.bluesoft.com.br/products/{linha}')
		time.sleep(1)

		if pagina.locator('xpath=/html/head/title').text_content() == '404 Not Found':
			print(f'{linha} - nenhuma foto encontrada para o produto no servidor da BLUESOFT!')
			time.sleep(1)
			return(False)

		else:
			pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			print(f'{linha} - foto do produto baixada com sucesso pelo servifor da BLUESOFT!')
			time.sleep(1)
			return(True)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da BLUESOFT!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da BLUESOFT!')
		time.sleep(1)
		return(False)
	
def google(linha):
	try:
		linha = linha.rstrip()
		pagina.goto(f'https://www.google.com.br/search?q={linha}&tbm=isch')
		pagina.locator('xpath=/html/body/div[3]/div/div[15]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/div[2]/h3/a/div/div/div/g-img/img').click()
		pagina.goto(pagina.locator('xpath=/html/body/div[5]/div/div/div/div/div/div/c-wiz/div/div[2]/div[2]/div/div[2]/c-wiz/div/div[3]//img').first.get_attribute('src'))
		pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')

		print(f'{linha} - foto do produto baixada com sucesso pelo servifor da GOOGLE!')

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da GOOGLE!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da GOOGLE!')
		time.sleep(1)
		return(False)

arquivo = open(local,'r')

for linha in arquivo:
	if eanpictures(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

	elif marsil(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

	elif maxxi(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

	elif cosmos(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

	elif google(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

	else:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_erro = (ttl_ft_erro + 1)
		print(f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRESSO : {ttl_ft} de {ttl_ls} / {round(((ttl_ft / ttl_ls) * 100),2)} %')

arquivo.close()


print(f'\nBusca finalizada! {ttl_ft_sucesso} fotos foram baixadas do total de {ttl_ft} fotos solicitadas!\n')
