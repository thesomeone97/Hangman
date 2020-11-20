# -*- coding: utf-8 -*-
"""Algoritmos e Programação de Computadores
 Projeto  AP2
Nomes: Leon Goldner - 1531717520219
       Leonardo Alfradique Diniz - 1911533963
       Luis Vitor - 1721533883
       Ana Carolina Ramos - 1531717110034
"""

def exercicio_117(nome_arq = 'lista_de_palavras.txt'):
	"""Cria um jogo da forca com uma palavra escolhida aleatoriamente de
	um arquivo de texto (.txt). Opcionalmente, o usuário pode colocar seu próprio
	arquivo-fonte de palavras (uma espécie de dicionário sem definições)."""
    #Primeiro, precisamos abrir o arquivo-fonte de palavras e armazenar
    #a palavra correspondente à linha escolhida numa variável, em seguida
    #fechando o arquivo.
	import random
	#Para obter o número de linhas do arquivo, somamos 1 para cada linha dele.
	with open(nome_arq) as f:
		num_linhas = sum(1 for linha in f)
	linha_escolhida = random.randint(1,num_linhas)
	arq = open(nome_arq)
	linha = 1
	while linha < linha_escolhida:
		arq.readline()
		linha += 1
	palavra = arq.readline().upper()
	arq.close()
	#Agora, escolhida a palavra, vamos montar o jogo propriamente dito.
	#REPL - READ-EVAL-PRINT-LOOP
	palavra_escondida = '_ ' * (len(palavra) - 1)
	palavra_escondida = palavra_escondida[:-1]
	palavra_escondida_lista = list(palavra_escondida)
	palavra_lista = list(palavra)
	numero_de_erros = 0
	letras_encontradas = 0
	letras_ja_tentadas = []
	#Os zeros da lista criada a seguir representam que a letra nessa posição
	#da palavra ainda não foi encontrada. Ao ser encontrada, seu valor muda para 1.
	posicoes_letras_encontradas = [0]*(len(palavra)-1)
	#A seguir definimos uma função auxiliar para ser utilizada no REPL abaixo.
	exibe_palavra = lambda lista : "".join(lista)
	#Iniciando modo REPL (interativo)
	while True:
		letra = input("Digite uma letra: ").upper()
		acerto = False
		from string import ascii_uppercase as letras_maiusculas
		if letra not in letras_maiusculas:
			print("Caractere inválido digitado. Por favor, tente novamente.")
			continue
		if letra in letras_ja_tentadas:
			print("Você já tentou esta letra. Tente outra.")
			continue
		else:
			letras_ja_tentadas.append(letra)
		#CÓDIGO REPENSADO
		#código antigo comentado
		indice = 0
		outro_indice = 0
		ainda_outro_indice = 0
		for letra_palavra in palavra_lista:
			if letra_palavra == letra:
				acerto = True
				letras_encontradas += 1
				posicoes_letras_encontradas[indice] = 1
			indice += 1
		if not acerto:
			numero_de_erros += 1
			print(f"-> Você errou pela {numero_de_erros}ª vez. Tente de novo!")
			print(f"A palavra é: {exibe_palavra(palavra_escondida_lista)}")
			print(f"Letras já tentadas: {letras_ja_tentadas}")
		else:
			while outro_indice < len(palavra_escondida_lista):
				if posicoes_letras_encontradas[ainda_outro_indice] == 1:
					palavra_escondida_lista[outro_indice] = palavra[ainda_outro_indice]
				ainda_outro_indice += 1
				outro_indice += 2
			print(f"A palavra é: {exibe_palavra(palavra_escondida_lista)}")
			print(f"Letras já tentadas: {letras_ja_tentadas}")
		#primeira_pos = palavra.find(letra)
		#if primeira_pos == -1:
			#numero_de_erros += 1
			#print(f"Você errou pela {numero_de_erros}ª vez. Tente de novo!")
		#else:
			#Vamos considerar a princípio apenas palavras com 1 exemplar de cada letra
			#(o que restringe muito nosso espaço de palavras, mas tudo bem)
			#palavra_escondida_lista[primeira_pos] = letra
			#palavra_escondida = "".join(palavra_escondida_lista)
			#print(f"A palavra é: {palavra_escondida}")
		#if letra in palavra:
			#primeira_pos = palavra.find(letra)
			#print("Parabéns! Você acertou.")
		#else:
			#print(f"Você errou pela {numero_de_erros}ª vez. Tente de novo!")
		if all(posicoes_letras_encontradas):
			print(f"Parabéns! Você ganhou\nA palavra era: {palavra}")
			break
		if numero_de_erros == 6:
			print(f"Você perdeu! A palavra era: {palavra}")
			break
		
if __name__ == '__main__':
	exercicio_117()
