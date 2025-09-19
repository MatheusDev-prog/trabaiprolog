:- dynamic sintoma/1.

doenca(gripe) :-
    sintoma(febre),
    sintoma(tosse),
    sintoma(dor_cabeca).

doenca(resfriado) :-
    sintoma(espirro),
    sintoma(coriza),
    sintoma(tosse).

doenca(corona) :-
    sintoma(febre),
    sintoma(tosse),
    sintoma(falta_de_ar),
    sintoma(perda_olfato).

doenca(alergia) :-
    sintoma(espirro),
    sintoma(coceira_nariz),
    sintoma(olhos_lacrimejando).
