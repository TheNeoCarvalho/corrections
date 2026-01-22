import json
import os

ARQUIVO = "data/votos.json"

ESTADO_INICIAL = {
    "por_aluno": {},
    "totais": {"A": 0, "B": 0, "C": 0, "D": 0},
    "reset_id": 0
}

def salvar(dados):
    os.makedirs("data", exist_ok=True)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def carregar():
    if not os.path.exists(ARQUIVO):
        salvar(ESTADO_INICIAL)
        return ESTADO_INICIAL.copy()

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def resetar():
    dados = carregar()
    dados["por_aluno"] = {}
    dados["totais"] = {"A": 0, "B": 0, "C": 0, "D": 0}
    dados["reset_id"] += 1  # identifica nova pergunta
    salvar(dados)
