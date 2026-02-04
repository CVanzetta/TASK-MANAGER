# Dockerfile Quality & Testing

Ce dossier contient les Dockerfiles optimisés avec tests de qualité intégrés.

## Améliorations apportées

### Backend Dockerfile
- ✅ Utilisation de `python:3.12-slim` pour réduire la taille de l'image
- ✅ Copie séparée de `requirements.txt` pour optimiser le cache Docker
- ✅ Utilisation de `--no-cache-dir` pour pip
- ✅ Création et utilisation d'un utilisateur non-root (`appuser`)
- ✅ Mise à jour des dépendances avec vulnérabilités (jinja2, PyYAML)

### Frontend Dockerfile
- ✅ Utilisation de nginx:alpine pour un serveur web léger
- ✅ Configuration nginx avec en-têtes de sécurité
- ✅ Exécution en tant qu'utilisateur non-root
- ✅ Support SPA (Single Page Application)

## Tests de qualité

### Hadolint
Linting des Dockerfiles selon les meilleures pratiques Docker.

### Build Test
Vérification que les images se construisent correctement.

### Trivy
Scan de sécurité pour détecter les vulnérabilités dans les images.

## CI/CD

Le workflow GitHub Actions [.github/workflows/dockerfile-tests.yml](../.github/workflows/dockerfile-tests.yml) exécute :
1. **Lint** : Hadolint sur les deux Dockerfiles
2. **Build** : Construction des images avec cache
3. **Scan** : Analyse de sécurité avec Trivy

Les résultats sont automatiquement uploadés dans l'onglet Security de GitHub.

## Utilisation locale

```bash
# Tester avec Hadolint
docker run --rm -i hadolint/hadolint < backend/Dockerfile
docker run --rm -i hadolint/hadolint < frontend/Dockerfile

# Construire les images
docker build -t task-manager-backend ./backend
docker build -t task-manager-frontend ./frontend

# Scanner avec Trivy
trivy image task-manager-backend
trivy image task-manager-frontend
```
