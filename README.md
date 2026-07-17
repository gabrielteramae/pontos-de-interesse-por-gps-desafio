# Points of Interest API

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

Solução para o desafio [`backend-br/desafios/points-of-interest`](https://github.com/backend-br/desafios/blob/master/points-of-interest/PROBLEM.md): cadastrar pontos de interesse (POIs) e listá-los por proximidade a partir de uma coordenada GPS de referência.

## Como funciona

```
POST /pois {"name": "Lanchonete", "x": 27, "y": 12} -> cadastra um POI

GET /pois -> lista todos os POIs cadastrados

GET /pois/nearby?x=20&y=10&max_distance=10
    -> calcula a distancia euclidiana de cada POI ate o ponto de referencia
    -> retorna apenas os POIs com distancia <= max_distance
```

Distância euclidiana: `sqrt((x1-x2)² + (y1-y2)²)`. Verificado manualmente contra o exemplo do `PROBLEM.md` (ponto de referência `(20,10)`, `d-max=10`): dos 7 POIs de exemplo, exatamente os 4 esperados (Lanchonete, Joalheria, Pub, Supermercado) ficam dentro do raio, e os outros 3 (Posto, Floricultura, Churrascaria) ficam de fora — validado tanto matematicamente quanto rodando a API de ponta a ponta.

## Stack

- **FastAPI** para a API REST
- **SQLAlchemy 2.0** + SQLite para persistência
- Cálculo de distância isolado em `proximity.py`, puro e testável, sem dependência de framework

## Estrutura

```
app/
├── main.py         # endpoints POST /pois, GET /pois, GET /pois/nearby
├── models.py         # entidade PointOfInterest
├── schemas.py          # request/response (Pydantic)
├── database.py           # conexao SQLAlchemy
└── proximity.py             # calculo de distancia euclidiana e filtro
```

## Como rodar

```bash
git clone <seu-repo>
cd points-of-interest-api
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8005
```

## Exemplo

```bash
curl -X POST http://localhost:8005/pois \
  -H "Content-Type: application/json" \
  -d '{"name":"Lanchonete","x":27,"y":12}'
```

```bash
curl "http://localhost:8005/pois/nearby?x=20&y=10&max_distance=10"
```
```json
[
  {"id": 1, "name": "Lanchonete", "x": 27, "y": 12},
  {"id": 3, "name": "Joalheria", "x": 15, "y": 12},
  {"id": 5, "name": "Pub", "x": 12, "y": 8},
  {"id": 6, "name": "Supermercado", "x": 23, "y": 6}
]
```

## Deploy

Pronto para subir no [Railway](https://railway.app): start command `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.

---

© 2026 Gabriel Teramae Chan
