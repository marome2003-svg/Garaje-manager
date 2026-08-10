# Changelog

## [0.1.0] - 2026-07-31

### Añadido

- Creación del repositorio.
- README inicial.
- Configuración de GitHub.

## [0.2.0] - 2026-07-31

### Añadido
- Menú principal funcional.
- Navegación entre los distintos menús.
- Estructura inicial del proyecto.

## [0.3.0] - 2026-08-06

### Mejorado

- Refactorizada la estructura de navegación de la aplicación.
- Simplificado main.py, dejándolo únicamente como punto de entrada del programa.
- Reorganizada la lógica de los menús para que cada uno gestione su propio flujo de ejecución.
- Renombradas variables para mejorar la legibilidad y mantener una nomenclatura más clara y consistente.

### Corregido

- Evitado el cierre inesperado del programa al volver desde los submenús.
- Añadida validación al eliminar vehículos para impedir errores cuando el vehículo indicado no existe.

## [0.4.0] - 2026-08-07

### Añadido

- Persistencia de datos para los vehículos.
- Carga automática de los vehículos al iniciar la aplicación.
- Guardado automático de los vehículos al cerrar la aplicación.
- Nuevo menú de configuración.
- Opción para restablecer la memoria de vehículos.

### Mejorado

- Reorganizada la estructura del proyecto para separar la lógica de la interfaz y la gestión de datos.
- Mejorada la organización del flujo principal de la aplicación.

## [0.5.0] - 2026-08-10

### Añadido

- Los vehículos pasan a almacenarse como diccionarios.
- Añadidos los datos de marca, modelo y kilómetros para cada vehículo.
- Añadida la visualización detallada de la información de cada vehículo.
- Añadida la posibilidad de modificar los datos de un vehículo.
- Actualizada la memoria para guardar y cargar los vehículos con sus nuevos datos.

### Mejorado

- Rediseñado el menú de gestión de vehículos.
- Mejorada la selección de vehículos mediante índices.
- Añadidas validaciones para evitar entradas incorrectas.
- Los kilómetros se gestionan como valores numéricos.
- Mejorada la gestión de errores al seleccionar, modificar y eliminar vehículos.

### Corregido

- Evitados errores al introducir índices de vehículos inexistentes.
- Evitados índices negativos al seleccionar vehículos.
- Corregida la conversión de kilómetros al guardar y cargar los datos.