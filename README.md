Trabalhando no setor de negocios ( comercial de distribuição ), criou-se uma necessidade de atualização em massa do portifolio de produtos. Considerando o grande volume, e mão de obra necessaria, a ideia desta MACRO é agilizar esse trabalho.

Ela tem uma mecanica bem simples, construida em python, faz a verificação no servidor da BLUESOFT ( parceira da GS1, que domina a padronização global de informações de produtos ).

Para utiliza-la, instale os seguintes quisitos no computador:

Windows:
-Python: obtido no site oficial do Python
-PIP: execute no terminal o seguinte comando: pip install --upgrade pip
-Bibliotecas: execute no terminal o seguinte comando: pip install playwrigth
-Dependencias do Playwright: execute no terminal o seguinte comando: python -m playwright install

Com tudo instalado, adicione em um arquivo ".txt", todos os codigos EAN dos produtos que deseja buscar fotos.

Assim que executar o codigo, ele solicitara o arquivo ".txt" com os codigos, e ja iniciara a instancia, baixando todas as fotos encontradas nomeando-as com o EAN do proprio produto.
