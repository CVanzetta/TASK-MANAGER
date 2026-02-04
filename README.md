# Task Manager

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=CVanzetta_TASK-MANAGER&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=CVanzetta_TASK-MANAGER)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=CVanzetta_TASK-MANAGER&metric=coverage)](https://sonarcloud.io/summary/new_code?id=CVanzetta_TASK-MANAGER)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=CVanzetta_TASK-MANAGER&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=CVanzetta_TASK-MANAGER)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=CVanzetta_TASK-MANAGER&metric=bugs)](https://sonarcloud.io/summary/new_code?id=CVanzetta_TASK-MANAGER)

Application de gestion de tâches avec backend FastAPI et frontend vanilla JS.

## Installation & usage

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Frontend

```bash
cd frontend
python3 -m http.server 5173
```

## Quelques commandes `curl`

### Créer une tâche
```bash
curl -s -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Écrire tests API","description":"Ajouter des assertions sur /tasks"}' | jq
```

### Lister les tâches
```bash
curl -s http://127.0.0.1:8000/tasks | jq
```

### Mettre à jour une tâche
```bash
curl -s -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"DONE"}' | jq
```

### Supprimer une tâche
```bash
curl -i -X DELETE http://127.0.0.1:8000/tasks/1
```

## Tests

### Exécuter les tests unitaires

```bash
cd backend
pip install pytest pytest-cov
pytest --cov=app --cov-report=html
```

Le rapport de couverture est disponible dans `backend/htmlcov/index.html`

### Analyse de qualité

```bash
cd backend
pip install pylint
pylint app
```

## Documentation

- [DEPLOYMENT.md](DEPLOYMENT.md) - Guide de déploiement Docker Compose
- [SONARCLOUD.md](SONARCLOUD.md) - Configuration et utilisation de SonarCloud
- [DOCKERFILE_QUALITY.md](DOCKERFILE_QUALITY.md) - Qualité et sécurité des Dockerfiles

## CI/CD

Le projet utilise GitHub Actions pour :
- ✅ Build et push des images Docker
- ✅ Scan de vulnérabilités (Trivy, Grype)
- ✅ Tests et analyse de code (SonarCloud)
- ✅ Validation des Dockerfiles (Hadolint)
- ✅ Analyse des fichiers Docker Compose
- ✅ Pre-commit hooks (trailing whitespace, YAML, etc.)

