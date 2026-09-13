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
