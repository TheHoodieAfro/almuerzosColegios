# Seguimiento de asistencia al almuerzo escolar

Aplicacion web para el seguimiento diario de los estudiantes al almuerzo escolar.

## Tecnologias utilizadas

- **Frontend:** Vue 3 + Vite + Tailwind CSS
- **Backend:** Python + FastAPI
- **Base de datos:** SQLite
- **Despliegue:** Docker + Docker Compose

## Instalacion

### Ambiente esperado

Preferably linux, be it x86 or ARM (raspberry PI)

### Prerrequisitos

- Docker
- Docker Compose

### Guia

1. Clone the repository:
git clone https://github.com/TheHoodieAfro/almuerzosColegios.git

2. Start the application:
cd almuerzosColegios
docker compose up

uvicorn main:app --reload
npm run dev

## Variables de ambiente

Create a `.env` file in the project root with the following:
DB_PATH= # path to the SQLite file, e.g. ./data/school.db

## Licencia

Este projecto se publica bajo [GNU GENERAL PUBLIC LICENSE, Version 3](https://github.com/TheHoodieAfro/almuerzosColegios/blob/main/LICENSE.txt).
