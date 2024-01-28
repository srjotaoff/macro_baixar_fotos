from tkinter import Tk
from tkinter.filedialog import askopenfilename

import time
from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

input ('Selecione o arquivo .txt com a lista de codigos de barra: ')
Tk().withdraw()
local = askopenfilename()
print(f'\n{local}\n')
arquivo = open(local,'r')

playwright = sync_playwright().start()
navegador = playwright.chromium.launch(headless = False)

print('\nIniciando instancia web - - - BLUESOFT\n')
pagina_bluesoft = navegador.new_page()

ttl_ft = int(0)
ttl_ft_sucesso = int(0)
ttl_ft_erro = int(0)

for linha in arquivo:
	try:
		linha = linha.rstrip()
		pagina_bluesoft.goto(f'https://cdn-cosmos.bluesoft.com.br/products/{linha}')
		time.sleep(1)

		if pagina_bluesoft.locator('xpath=/html/head/title').text_content() == '404 Not Found':
			print(f'{linha} - nenhuma foto encontrada para o produto!')
			ttl_ft = (ttl_ft + 1)
			ttl_ft_erro = (ttl_ft_erro + 1)
			time.sleep(1)

		else:
			pagina_bluesoft.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			ttl_ft = (ttl_ft + 1)
			ttl_ft_sucesso = (ttl_ft_sucesso + 1)
			print(f'{linha} - foto do produto baixada com sucesso!')
			time.sleep(1)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto!')
		ttl_ft = (ttl_ft + 1)
		ttl_ft_erro = (ttl_ft_erro + 1)
		time.sleep(1)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto!')
		ttl_ft = (ttl_ft + 1)
		ttl_ft_erro = (ttl_ft_erro + 1)
		time.sleep(1)

arquivo.close()

print(f'\nBusca finalizada! {ttl_ft_sucesso} fotos foram baixadas do total de {ttl_ft} fotos solicitadas!\n')






