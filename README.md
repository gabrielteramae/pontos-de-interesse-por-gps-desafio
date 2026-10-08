# Pontos de interesse — proximidade num plano, não em lat/lon

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.35-D71F00)

Cadastra pontos com nome e coordenadas inteiras `x` e `y` (as duas `>= 0`) e lista os que estão dentro de uma distância máxima. A conta é euclidiana, em memória, sobre todas as linhas da tabela.

## Por que distância euclidiana

| Escolha | Efeito |
| --- | --- |
| `sqrt((x1-x2)² + (y1-y2)²)` depois de um `SELECT` completo | Bate com o plano do modelo (`x`/`y` inteiros). Não usa índice espacial. |
| Haversine ou PostGIS | Serve para latitude e longitude. Este modelo não tem lat/lon. |

`GET /pois/nearby` carrega todos os POIs e filtra em Python. Serve para a tabela pequena do exercício; não é busca geográfica.

## Stack

- Python (sem versão pinada no repositório)
- FastAPI 0.115.0 e Uvicorn 0.30.6
- SQLAlchemy 2.0.35
- SQLite em `sqlite:///./pois.db` (`DATABASE_URL` troca o banco)
- `unittest` da biblioteca padrão

## Estrutura

```
app/
├── main.py        # /pois e /pois/nearby
├── proximity.py   # distância e filtro
├── models.py
├── schemas.py
└── database.py
tests/
└── test_proximity.py
requirements.txt
```

## Como rodar

```bash
git clone https://github.com/gabrielteramae/pontos-de-interesse-por-gps-desafio.git
cd pontos-de-interesse-por-gps-desafio
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

| Método | Rota | Resposta |
| --- | --- | --- |
| POST | `/pois` | 201. Corpo: `name`, `x`, `y` |
| GET | `/pois` | todos os pontos |
| GET | `/pois/nearby` | query `x` (>= 0), `y` (>= 0), `max_distance` (> 0) |

## Testes realizados

`tests/test_proximity.py` não sobe a API. Confere o triângulo 3-4-5 (`euclidean_distance(0, 0, 3, 4) == 5`) e que o filtro com `max_distance` 5 mantém o ponto `(1, 1)` e descarta `(100, 100)`.

```bash
python -m unittest tests.test_proximity
```

---

© 2026 Gabriel Teramae Chan
