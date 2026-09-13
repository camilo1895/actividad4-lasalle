# Formulario de Contacto La Salle

Actividad 4 - Ambientes en el desarrollo de producto de ingeniería de software.

## Stack

- Next.js
- FastAPI
- PostgreSQL

## Ambientes

- Development
- Test
- Production

## Estructura

- frontend/: aplicación Next.js
- backend/: API FastAPI
- docs/: documentación técnica

## Equipo

| Integrante                        | Usuario de GitHub  |
| --------------------------------- | ------------------ |
| Esteban Alejandro Hernandez Lopez | estebanhernandez04 |
| Andres Felipe Rodríguez Martinez  | AndresFRM17        |
| Ivan Camilo Guarnizo Cala         | camilo1895         |

## Requisitos previos

- Git
- Node.js
- Python 3
- PostgreSQL

## Instalación del backend

El backend del proyecto está desarrollado con FastAPI. Para preparar el
entorno local, siga los siguientes pasos.

### 1. Ingresar al directorio del backend

```bash

cd backend

```

### 2. Crear el entorno virtual

```bash

python -m venv venv

```

### 3. Activar el entorno virtual

En Windows:

```bash

.\.venv\Scripts\activate.ps1

```

En Linux o macOS:

```bash

source venv/bin/activate

```

### 4. Instalar las dependencias

```bash

python -m pip install -r requirements.txt

```

### 5. Ejecutar el backend

uvicorn main:app --reload

## Variables de entorno

El backend requiere variables de entorno para su configuración (conexión
a la base de datos, entre otras). Estas variables no se incluyen en el
repositorio por motivos de seguridad.

### 1. Copiar el archivo de ejemplo

```bash

cp backend/.env.example backend/.env

```

### 2. Configurar los valores

Editar `backend/.env` y completar los valores correspondientes al
ambiente local (host, puerto, nombre de la base de datos, usuario y
contraseña).

> Nunca subir el archivo `backend/.env` con credenciales reales al
> repositorio. El archivo `backend/.env.example` solo contiene valores
> de ejemplo.

## Instalación del frontend

El frontend del proyecto está desarrollado con Next.js. Para instalar sus
dependencias y ejecutar la aplicación en un entorno local, siga los
siguientes pasos.

### 1. Ingresar al directorio del frontend

Desde la raíz del proyecto:

```bash

cd frontend

```

### 2. Instalar las dependencias

Ejecute el siguiente comando para instalar las dependencias definidas
en el archivo `package.json`

```bash

npm install

```

### 3. Ejecutar el frontend

Para iniciar el servidor de desarrollo:

```bash

npm run dev

```

### 4. Acceder a la aplicación

Una vez iniciado el servidor, abra en el navegador la dirección indicada
por Next.js en la terminal. Por defecto, normalmente corresponde a:

http://localhost:3000

Si el puerto configurado es diferente, utilice la dirección mostrada
por la aplicación al iniciar.

### 5. Verificar la ejecución

Compruebe que el Formulario de Contacto La Salle cargue correctamente
y que el frontend pueda comunicarse con el backend.

## Pruebas

La validación del Formulario de Contacto La Salle se realiza mediante
casos de prueba funcionales que permiten comprobar el correcto
funcionamiento del frontend y su comunicación con el backend.

El equipo realizará la validación final utilizando los casos de prueba
definidos para verificar el funcionamiento general de la aplicación.

Los casos de prueba, resultados esperados y el procedimiento de
validación se encuentran documentados en:

`docs/PRUEBAS.md`
