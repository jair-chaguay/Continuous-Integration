# Gym Membership Management System

Sistema de gestión de membresías de gimnasio desarrollado como parte del Workshop de Continuous Integration.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar Tests

```bash
pytest tests/test_membership.py -v
pytest tests/test_membership.py --junitxml=test-results.xml
```

## Ejecutar Linting

```bash
pylint src/
```
