from pyswip import Prolog


prolog = Prolog()
prolog.consult("data.pl")  

# Lista de sintomas possíveis
sintomas = [
    "febre",
    "tosse",
    "dor_cabeca",
    "espirro",
    "coriza",
    "falta_de_ar",
    "perda_olfato",
    "coceira_nariz",
    "olhos_lacrimejando"
]

print("responda com 's' para sim e 'n' para não:")

# Pergunta ao usuário sobre cada sintoma
for sintoma in sintomas:
    resposta = input(f"você tem {sintoma.replace('_', ' ')}? (s/n): ").strip().lower()
    if resposta == "s":
        prolog.assertz(f"sintoma({sintoma})")

# Tenta encontrar a doença
doencas = list(prolog.query("doenca(Doenca)"))

if doencas:
    print("\nPossível diagnóstico(s):")
    for d in doencas:
        print(f"- {d['Doenca']}")
else:
    print("\nNão foi possível identificar a doença com os sintomas fornecidos.")
