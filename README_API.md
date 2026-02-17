# Quantum Intelligence API

## Endpoints
- `GET /` – welcome message
- `POST /predict/overpotential` – predict overpotential and current density for a given catalyst composition
- `GET /health` – health check

## Run
```bash
pip install -r requirements_api.txt
uvicorn main:app --reload
npm install node-fetch@2
node test_client.js
go run client.go
