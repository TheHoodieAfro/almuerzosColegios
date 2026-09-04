# Seguimiento de asistencia al almuerzo escolar

Aplicacion web para el seguimiento diario de los estudiantes al almuerzo escolar.

## Tecnologias utilizadas

- **Frontend:** Vue 3 + Vite + Tailwind CSS
- **Backend:** Python + FastAPI
- **Base de datos:** SQLite
- **Despliegue:** Docker

## Instalación

### Ambiente esperado
Pensado para correr en Linux (x86 o ARM, como Raspberry Pi). También se puede correr en Windows usando Docker Desktop, únicamente para fines de presentación/demo.

### Prerrequisitos
- Docker
- Docker Compose
- (Solo para desarrollo local) Node.js y Python 3.12+

### Guía: correr con Docker (Linux)
1. Abir powershell y utilizar el comando:
```bash
   cd Documentos
```
2. Clonar el repositorio:
```bash
   git clone https://github.com/TheHoodieAfro/almuerzosColegios.git
   cd almuerzosColegios
```
3. Copiar los archivos excel de los estudiantes a la carpeta "data" encontrada en la carpeta del proyecto (Documentos/almuerzosColegios/data)
4. Levantar los contenedores:
```bash
   docker compose up --build
```
5. Abrir `http://localhost` en el navegador.

### Guía: correr con Docker (Windows, solo para presentaciones)
1. Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/) y asegurarse de que esté corriendo.
2. Clonar el repositorio (con Git Bash, PowerShell o la terminal de tu preferencia):
```powershell
   git clone https://github.com/TheHoodieAfro/almuerzosColegios.git
   cd almuerzosColegios
```
3. Levantar los contenedores:
```powershell
   docker compose up --build
```
4. Abrir `http://localhost` en el navegador.

### Guía: correr localmente (para desarrollo y pruebas)
Backend:
```bash
cd backend
uvicorn main:app --reload
```
El backend queda disponible en `http://127.0.0.1:8000`.

Frontend:
```bash
cd frontend
npm install
npm run dev
```
El frontend queda disponible en `http://localhost:5173`.

## Licencia

Este projecto se publica bajo [GNU GENERAL PUBLIC LICENSE, Version 3](https://github.com/TheHoodieAfro/almuerzosColegios/blob/main/LICENSE.txt).
