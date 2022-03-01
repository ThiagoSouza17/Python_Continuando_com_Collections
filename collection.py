
#CONJUNTOS (SET)

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(len(assistiram))

print(set(assistiram))

print(set([1,2,3,1]))

print(type({1, 2, 3}))

for usuario in set(assistiram):
    print(usuario)

#OPERAÇÕES
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning) #UNIÃO
print(usuarios_data_science & usuarios_machine_learning) #INTERSECÇÃO
print(usuarios_data_science - usuarios_machine_learning) #DIFERENÇA

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml) #Pertence
print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))
print(usuarios)

usuarios = frozenset(usuarios)
print(type(usuarios))

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito do meu cachorro"
print(meu_texto.split())
print(set(meu_texto.split()))

#DICIONÁRIO (DICT)

aparicoes = {
    "Guilherme" : 1,
    "cachorro" : 2,
    "nome" : 2,
    "vindo" : 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"])
print(aparicoes["cachorro"])

print(aparicoes.get("xpto", 0))

# aparicoes = dict(Guilherme = 2, cachorro = 1), seria outra forma de instanciar dicionários.

aparicoes["carlos"] = 1
print(aparicoes)
aparicoes["carlos"] = 2
print(aparicoes)
del aparicoes["carlos"]
print(aparicoes)

print("cachorro" in aparicoes)
print("carlos" in aparicoes)

for elemento in aparicoes: #passa pelas chaves do dicionário.
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

print(["palavra {}". format(chave) for chave in aparicoes.keys()])

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito do meu cachorro"
print(meu_texto.lower())

meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

#DEFAULTDICT

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

dicionario = defaultdict(int)
print(dicionario['guilherme'])

dicionario['guilherme'] = 15
print(dicionario['guilherme'])

aparicoes = defaultdict(int)
print(aparicoes)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

class Conta:
    def __init__(self):
        print("Imprimindo umma conta")

contas = defaultdict(Conta)
print(contas[15])
print(contas[17])

#COUNTER
from collections import Counter

aparicoes = Counter()
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

aparicoes = Counter(meu_texto.split())
print(aparicoes)

#PRÁTICA: TESTANDO O USO DE DIVERSAS COLEÇÕES

texto1 = """
Imagine que você foi contratado para criar uma aplicação que tem a responsabilidade de agendar consultas em uma clínica médica. Você completou o desafio mas se deparou com um problema: as datas em JavaScript estão aparecendo com o mês invertido! E agora, o que fazer? Sentar e chorar?! Calma “pequeno gafanhoto”, primeiro precisamos compreender o porquê disso acontecer...
Afinal, como funciona o principal objeto JavaScript responsável por esse mecanismo?
O primeiro passo é instanciar uma data. A linguagem JavaScript possui nativamente uma forma para executar essa ação. Para criar datas em JavaScript utilizamos o construtor Date. Os objetos Date criados a partir desse construtor representam um momento único no tempo no calendário ocidental (as datas) e possuem como base o valor em milissegundos (significa um milésimo de segundo e você pode calcular $segundos x 1.000$ para obter o resultado em milissegundos).
Tudo certo! Conseguimos criar nossa Data e seu formato padrão é completo, com texto em inglês e fuso horário GMT, que é o tempo médio de Greenwich e de forma simples representa as nossas 24 horas do dia. No entanto, sabemos que esse não é o único formato de data e precisamos ter bastante cuidado ao instanciar um objeto Date, pois a data computada pode variar de acordo com o fuso horário do seu navegador por padrão
"""

texto2 = """
Nunca é tarde para incluir um blog corporativo na estratégia digital de sua empresa. Os blogs são excelentes fontes de tráfego e um dos canais mais usadas pelos negócios digitais para atrair  “e-mails quentes” (os leads) através do inbound marketing.

Tudo bem, concordo que blogar soa bem menos atraente do que o Medium “Mulheres que Escrevem”, as novas máscaras de Pokémon no Snapchat ou a popularidade da Gabriela Pugliesi no Instagram.

Mas sabia que um blog conversa com todas essas redes sociais, cabendo perfeitamente em estratégias crossmedia? Além de ser o tipo de canal completo o suficiente para se tornar um ponto de encontro com seus clientes, agregar diversos formatos de conteúdo, nichar sua audiência, interagir com públicos específicos e propagar os valores da sua marca.

Um blog responde às perguntas dos clientes rapidamente, atende a vários usuários com a mesma dúvida ao mesmo tempo e apresenta os benefícios do seu negócio em conteúdos diversos.

Ponto de encontro, o meu blog ? É. Já viu o tamanho da comunidade do Jovem Nerd? E a longevidade do Bored Panda e do Techtudo? Imagine que cerca de 1.440 posts estão sendo escritos e publicados a cada minuto (só) na plataforma WordPress. Se um dia tem 1.440 minutos, isso são 2.073.600 milhões de posts por dia. Todos os dias. E se você prefere checar se o que digo é verdade, é só conferir o Worldometers.
"""

aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
print(total_de_caracteres)

print([(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()])

proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))

print(proporcoes)

print(proporcoes.most_common(10))

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

print(analisa_frequencia_de_letras(texto1))

print(analisa_frequencia_de_letras(texto2))


