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
pagina = navegador.new_page()

ttl_ft = int(0)
ttl_ft_sucesso = int(0)
ttl_ft_erro = int(0)


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

		pagina.goto(f'https://www.google.com/search?q={linha}&tbm=isch&hl=pt-BR&tbs=isz:l&rlz=1C1GCEB_enBR1083BR1083&sa=X&ved=0CAIQpwVqFwoTCLjXnpz434QDFQAAAAAdAAAAABAC&biw=1519&bih=761')
		time.sleep(1)

		pagina.locator('xpath=/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img').click()
		time.sleep(2.5)

		try:
			metodo_ft_direto = 'xpath=/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]'
			metodo_gt_grid = 'xpath=/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/c-wiz/c-wiz/c-wiz/c-wiz[2]/c-wiz/div/scrolling-carousel/div[1]/span/div[1]/div/img[1]'

			if pagina.query_selector(metodo_ft_direto) is not None:
				metodo = metodo_ft_direto

			elif pagina.query_selector(metodo_gt_grid) is not None:
				metodo = metodo_gt_grid

			else:
				return(False)

			url_img = pagina.locator(metodo).get_attribute('src')

			pagina.goto(url_img)
			pagina.locator('xpath=/html/body/img').screenshot(path = f'{linha}.png')
			print(f'{linha} - foto do produto baixada com sucesso pelo servifor da GOOGLE!')
			time.sleep(1)
			return(True)

		except PlaywrightTimeoutError:
			print(f'{linha} - nenhuma foto encontrada para o produto no servidor da GOOGLE!')
			time.sleep(1)
			return(False)

	except TypeError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da GOOGLE!')
		time.sleep(1)
		return(False)

	except PlaywrightTimeoutError:
		print(f'{linha} - nenhuma foto encontrada para o produto no servidor da GOOGLE!')
		time.sleep(1)
		return(False)


for linha in arquivo:
	
	if marsil(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)
	
	elif cosmos(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)

	elif google(linha) is True:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_sucesso = (ttl_ft_sucesso + 1)

	else:
		ttl_ft = (ttl_ft + 1)
		ttl_ft_erro = (ttl_ft_erro + 1)

arquivo.close()

print(f'\nBusca finalizada! {ttl_ft_sucesso} fotos foram baixadas do total de {ttl_ft} fotos solicitadas!\n')
