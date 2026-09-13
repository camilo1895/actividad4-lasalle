# Pruebas del proyecto

## Objetivo

Verificar el funcionamiento del formulario de contacto después de integrar los cambios.

## Casos de prueba

Los siguientes casos de prueba permiten verificar el funcionamiento
general del Formulario de Contacto La Salle y comprobar que sus
principales funcionalidades respondan correctamente.

| ID    | Caso de prueba                    | Procedimiento                                                                                 | Resultado esperado                                                                          |
| ----- | --------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| CP-01 | Carga del formulario              | Ingresar a la página del formulario de contacto.                                              | El formulario se muestra correctamente y todos sus campos están disponibles.                |
| CP-02 | Envío con datos válidos           | Completar todos los campos obligatorios con información válida y presionar el botón de envío. | El formulario procesa la información y muestra una confirmación de envío exitoso.           |
| CP-03 | Campos obligatorios vacíos        | Intentar enviar el formulario dejando uno o más campos obligatorios sin completar.            | El sistema impide el envío e informa que los campos requeridos deben completarse.           |
| CP-04 | Validación del correo electrónico | Ingresar un correo con formato incorrecto e intentar enviar el formulario.                    | El sistema identifica que el correo no tiene un formato válido e impide el envío.           |
| CP-05 | Comunicación con el backend       | Realizar un envío válido desde el formulario.                                                 | El frontend envía la solicitud al backend y se obtiene una respuesta correcta del servicio. |

## Procedimiento de validación final

La validación final debe realizarse después de integrar todos los cambios
en la rama principal `main`, con el objetivo de comprobar que la aplicación
continúa funcionando correctamente después del proceso de integración.

### Pasos para realizar la validación

1. Actualizar la rama principal del repositorio:

   ```bash
   git checkout main
   git pull origin main

   ```

2. Verificar que las variables de entorno necesarias estén configuradas
   correctamente utilizando como referencia los archivos .env.example.

3. Instalar las dependencias del backend y del frontend siguiendo las
   instrucciones descritas en el archivo README.md.

4. Iniciar el backend de la aplicación y verificar que el servicio se
   ejecute sin errores.

5. Iniciar el frontend y acceder al Formulario de Contacto La Salle desde
   el navegador.

6. Ejecutar los casos de prueba CP-01, CP-02, CP-03, CP-04 y CP-05
   definidos en la sección anterior.

7. Comparar el resultado obtenido en cada prueba con el resultado esperado.

8. Registrar los resultados obtenidos en la sección de resultados de la
   validación final.

### Criterio de aprobación

La validación final se considera satisfactoria cuando la aplicación inicia
correctamente, existe comunicación entre el frontend y el backend y los
casos de prueba definidos obtienen el resultado esperado.

## Resultados de la validación final

| ID    | Resultado obtenido                                          | Estado   |
| ----- | ----------------------------------------------------------- | -------- |
| CP-01 | El formulario cargó correctamente.                          | Aprobado |
| CP-02 | El formulario procesó correctamente los datos válidos.      | Aprobado |
| CP-03 | El sistema impidió el envío con campos obligatorios vacíos. | Aprobado |
| CP-04 | El sistema rechazó el correo con formato inválido.          | Aprobado |
| CP-05 | El frontend se comunicó correctamente con el backend.       | Aprobado |
