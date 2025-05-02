<!-- badges -->
[![Build Status](https://img.shields.io/github/actions/workflow/status/RubenZeni/AuthGuard-CLI/ci.yml?branch=main)](https://github.com/RubenZeni/AuthGuard-CLI/actions)
[![Coverage Status](https://img.shields.io/codecov/c/gh/RubenZeni/AuthGuard-CLI)](https://codecov.io/gh/RubenZeni/AuthGuard-CLI)
[![PyPI version](https://img.shields.io/pypi/v/authguard-cli)](https://pypi.org/project/authguard-cli)
[![License](https://img.shields.io/github/license/RubenZeni/AuthGuard-CLI)](LICENSE.md)

# AuthGuard CLI

**AuthGuard CLI** es una herramienta de línea de comandos para gestionar usuarios y tareas con autenticación segura.
Desarrollada paso a paso con la mentoría de ChatGPT, sigue buenas prácticas de Python, seguridad y control de versiones.

---

## 📖 Tabla de Contenidos

1. [Características](#-características)
2. [Requisitos](#-requisitos)
3. [Estructura del proyecto](#-estructura-del-proyecto)
4. [Instalación](#-instalación)
5. [Uso Básico](#-uso-básico)
6. [Comandos disponibles](#-comandos-disponibles)
7. [Flujo de Trabajo (Git & GitHub)](#-flujo-de-trabajo-git--github)
8. [Testing y Calidad](#-testing-y-calidad)
9. [Contribuir](#-contribuir)
10. [Roadmap](#-roadmap)
11. [Apoyo y contribución tecnológica](#-apoyo-y-contribución-tecnológica)
12. [Licencia](#-licencia)

---

## 🔒 Características

- **Autenticación segura** con bcrypt y exit codes semánticos.
- **CLI intuitiva** construida con Click.
- **Persistencia ligera** en JSON para usuarios y tareas.
- **Código modulable**: capas de servicios, repositorio y utils.
- **Test suite** completa con pytest (>80 % coverage).
- **Linting & formato** automático: black, isort, pylint integrado via pre-commit.

---

## ⚙️ Requisitos

- Python 3.11+
- Git
- [GitHub CLI](https://cli.github.com/) (opcional, para gestión de PRs)
- pip

---

## ⚙️ Estructura del proyecto

```bash
AuthGuard-CLI/
├── cli/
│   ├── __init__.py
│   ├── auth_cli.py
│   └── commands.py
├── data/
│   └── users.json
├── repository/
│   ├── __init__.py
│   └── json_repository.py
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   └── task_service.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_sanity.py
│   └── test_tasks.py
├── utils/
│   ├── __init__.py
│   ├── crypto.py
│   └── validators.py
├── .env/
├── .gitignore
├── LICENSE.md
├── pyproject.toml
└── README.md
```

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/RubenZeni/AuthGuard-CLI.git
cd AuthGuard-CLI

# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .\.venv\Scripts\activate  # Windows PowerShell

# Instalar en modo editable
pip install -e .

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

---

## 💻 Uso Básico

Una vez instalado, podés usar el comando principal, actualmente `python -m cli.commands`, en el futuro `authguard`:

```bash
# Ver ayuda general
authguard --help

# Registrar un nuevo usuario
authguard signup <username> <password>

# Iniciar sesión
authguard login <username> <password>
```

> **Tip:** Se puede usar el alias `agc="python -m cli.commands"` (**A**uth**G**uard**C**LI).

---

## 📋 Comandos Disponibles

| Comando | Descripción |
|---|---|
| `signup <user> <pw>` | Crea un usuario nuevo. |
| `login <user> <pw>` | Inicia sesión y devuelve exit code / mensaje. |
| `add <task>` | (Próximamente) Agrega una tarea para el usuario. |
| `list` | (Próximamente) Lista todas las tareas. |
| `done <id>` | (Próximamente) Marca tarea como completada. |
| `delete <id>` | (Próximamente) Elimina una tarea. |

---

## 🌿 Flujo de Trabajo (Git & GitHub)

- **main**: código siempre estable, protegido.
- **dev**: integraciones de features aprobadas.
- **feature/…**: ramas temporales para cada bloque (p.ej. `feature/signup-login`, `feature/task-manager`).
- **bugfix/…**: correcciones puntuales.
- **release/…**: preparaciones de versión.

1. Trabajá siempre en `feature/...` a partir de `dev`.
2. Commits cortos y descriptivos (`git add … && git commit -m "…”`).
3. Push y abrí un PR hacia `dev` para revisión.
4. Merge y eliminar la rama feature.
5. Cuando `dev` cumpla la entrega, mergear a `main` y etiquetar (v0.1.0, v0.2.0, …).

---

## 🧪 Testing y Calidad

- Ejecutar tests:
  ```bash
  pytest -q
  ```
- Lint y formateo con pre-commit:
  ```bash
  pre-commit run --all-files
  ```
- Pylint score > 9.5:
  ```bash
  pylint services/auth_service.py cli/*.py
  ```

---

## 🤝 Contribuir

1. Fork del repositorio.
2. Crear rama de feature o bugfix:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Hacer commits atómicos y respetar convenciones.
4. Actualizar tests si corresponde.
5. Push y Pull Request hacia `dev`.
6. Responder code reviews y ajustar según feedback.

---

## 📈 Roadmap

- 🔜 **Bloque 3**: sistema completo de gestión de tareas.
- 🔜 **Bloque 4**: migración a SQLite/PostgreSQL con SQLAlchemy.
- 🔜 **Despliegue**: empaquetar como CLI instalable en PyPI y Docker.
- 🔜 **API REST**: exponer endpoints con FastAPI.

---

## 👨‍💻 Apoyo y contribución tecnológica

Este proyecto fue desarrollado bajo la mentoría experta de **ChatGPT**, quien aportó estructura, buenas prácticas y revisión continua, permitiendo un proceso de aprendizaje ágil y de alta calidad.

---

## 📜 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE.md).
