
# Projeto MVP AC – Dashboard + APIs

Este repositório contém a estrutura completa do meu MVP Backend, com frontend em React e duas APIs em Flask (API principal e API externa de cotação).

---

## Estrutura do Projeto


projeto-mvp/
│
├── api-cotacao/            # API externa para cotação do dólar
│   ├── app.py
│   ├── requirements.txt
│
├── api-vendas/             # API principal (clientes)
│   ├── app.py
│   ├── requirements.txt
│
├── dashboard-frontend/     # Frontend React
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│
├── docker-compose.yml
├── README.md
└── mysql/                  # Dump do banco de dados
    └── init.sql
```

---

## Como Executar o Projeto (com Docker Compose)

1. Ter o Docker e Docker Compose instalados
2. Navegue até a raiz do projeto e execute:

```bash
docker compose up --build
```

3. Acesse:
- Frontend: http://localhost:5173
- API de Clientes: http://localhost:5000/clientes
- API de Cotação: http://localhost:5001/cotacao

---

## Instalação Manual (sem Docker)

### API de Cotação (Flask)
```bash
cd api-cotacao
pip install -r requirements.txt
python app.py
```

### API de Clientes (Flask)
```bash
cd api-vendas
pip install -r requirements.txt
python app.py
```

### Frontend (React)
```bash
cd dashboard-frontend
npm install
npm run dev
```

---

## 📄 Rotas das APIs

### API Principal – Vendas

| Método | Rota                   | Descrição                     |
|--------|------------------------|-------------------------------|
| GET    | /clientes              | Lista os clientes             |
| POST   | /clientes              | Cria um novo cliente          |
| PUT    | /clientes/<id>         | Edita um cliente              |
| DELETE | /clientes/<id>         | Deleta um cliente             |
| GET    | /cotacao-dolar         | Busca cotação via API externa |

### API Externa – Cotação

| Método | Rota      | Descrição                    |
|--------|-----------|------------------------------|
| GET    | /cotacao  | Retorna a cotação do dólar   |

---

## Banco de Dados

O banco de dados `vendas_db` é restaurado automaticamente no container MySQL via arquivo `init.sql`, que contém a estrutura e os dados iniciais.



