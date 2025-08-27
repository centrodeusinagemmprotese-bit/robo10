from dataclasses import dataclass

@dataclass
class RegraLance:
    decremento_min: float
    tipo_decremento: str
    preco_minimo: float
    passo_minimo: float
    janela_final_min: int
    agressividade: float

def proximo_lance(melhor_atual, minha_oferta_atual, regra: RegraLance, minutos_restantes):
    if regra.tipo_decremento == "percentual":
        alvo = melhor_atual * (1 - max(regra.decremento_min, 0.0001))
    else:
        alvo = melhor_atual - max(regra.decremento_min, regra.passo_minimo)

    if minutos_restantes <= regra.janela_final_min:
        delta = (alvo - regra.preco_minimo) * regra.agressividade
        alvo = max(regra.preco_minimo, alvo - abs(delta))

    alvo = max(alvo, regra.preco_minimo)

    if minha_oferta_atual and alvo >= minha_oferta_atual:
        alvo = max(regra.preco_minimo, minha_oferta_atual - max(regra.passo_minimo, 0.01))

    arred = lambda x: round(x / regra.passo_minimo) * regra.passo_minimo
    candidato = arred(alvo)
    candidato = round(candidato, 2)

    if minha_oferta_atual and abs(minha_oferta_atual - candidato) < regra.passo_minimo:
        return None
    return candidato
