import json
import os

ARQUIVO = "data/votos.json"

def salvar(dados):
    os.makedirs("data", exist_ok=True)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def carregar():
    if not os.path.exists(ARQUIVO):
        return {"por_aluno": {}, "totais": {"A": 0, "B": 0, "C": 0, "D": 0}}

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)
