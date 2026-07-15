# Gestor de Usuarios con SQLite

Aplicación de consola en Python que gestiona usuarios usando una base de datos SQLite real, con operaciones CRUD completas (Crear, Leer, Buscar, Eliminar) y menú interactivo.

## 📋 Funcionalidades

- **Registrar usuario**: valida nombre (mínimo 3 caracteres), edad (mayor a 0) y correo (formato básico válido) antes de guardarlo en la base de datos.
- **Ver todos los usuarios**: muestra una tabla con todos los usuarios registrados.
- **Buscar usuario por nombre**: búsqueda parcial, no distingue mayúsculas/minúsculas.
- **Eliminar usuario**: pide confirmación antes de borrar el registro.

## 🗄️ Base de datos

El programa crea automáticamente un archivo `usuarios.db` (SQLite) la primera vez que se ejecuta, con una tabla `usuarios`:

| Campo   | Tipo    | Restricción         |
|---------|---------|---------------------|
| id      | INTEGER | Primary Key, Auto   |
| nombre  | TEXT    | No nulo             |
| edad    | INTEGER | No nulo             |
| correo  | TEXT    | No nulo, único      |

## 🚀 Cómo ejecutarlo

```bash
python gestor_usuarios_sqlite.py
```

## 🎯 Objetivo del proyecto

Practicar el uso de bases de datos relacionales desde Python (`sqlite3`), operaciones CRUD, validación de datos, manejo de excepciones (`sqlite3.IntegrityError`, `ValueError`) y prevención de inyección SQL mediante consultas parametrizadas.

## 🛡️ Buenas prácticas aplicadas

- Uso de parámetros `?` en las consultas SQL en lugar de f-strings, para prevenir inyección SQL.
- Restricción `UNIQUE` en el correo para evitar registros duplicados.
- Confirmación antes de eliminar un registro.

## 🚀 Posibles mejoras futuras

- Agregar edición de usuarios existentes (Update del CRUD).
- Exportar los datos a CSV.
- Migrar la interfaz a una API con Flask o FastAPI.

## 🛠️ Tecnologías

- Python 3
- SQLite (módulo `sqlite3`, incluido en Python)

## 👤 Autor

Dilan Eduardo Martínez Castro — [github.com/k1618](https://github.com/k1618)
