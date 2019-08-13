caminho = "FEITO - Documentacao Comprobatoria de Despesas - SIM/"
listaNomes = ["notas_empenhos.csv"]

for nomeArquivoEntrada in listaNomes:
	arquivoEntrada = open(caminho+nomeArquivoEntrada)

	arquivoSaida = open(nomeArquivoEntrada+"Limpo",'w')

	quantidadeColunas = len(arquivoEntrada.readline().split(";"))-1

	for linha in arquivoEntrada :
		if len(linha.split(";")) == quantidadeColunas:
			arquivoSaida.write(linha)

	arquivoEntrada.close()
	arquivoSaida.close()