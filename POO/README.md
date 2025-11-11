# 🐍 Python Orientado a Objetos


Curso de programación orientada a objetos utilizando el lenguaje de programación Python.

## **Proyecto del curso**

### 📚 Sistema de Gestión Bibliotecaria

Sistema modular desarrollado en Python implementando programación oriendada a objetos (POO). Diseñado para gestionar **libros**, **usuarios** (estudiantes y profesores), operaciones de prestamos y devoluciones dentro de una biblioteca. <br>
Inlcuye persistencia de datos mediante archivos JSON, lo que permite guardar y restaurar el estado completo de la biblioteca.

### Características principales
- **Arquitectura modular**: Las funcionalidades estan organizadas en clases y archivos independientes.
- **Gestión de usuarios**: Permite registrar estudiantes y profesores con atributos personalizados.
- **Gestión de libros**: Incluye registro, búsqueda, verificación de disponibilidad y detección de popularidad.
- **Persistencia de datos**: guarda y carga el estado completo del sistema (libros, usuarios, préstamos) en un archivo JSON.
- **Manejo de excepciones**: control robusto de errores mediante clases personalizadas (`BookNotAvailableError`, `NotFoundUserError`, etc.).

### Estructura del proyecto
```bash
📁 library_system/
│
├── book.py              # Define la clase Book y sus métodos
├── users.py             # Define las clases Student y Professor
├── library.py           # Clase principal Library: gestiona libros y usuarios
├── persistence.py       # Clase Persistence: guarda y carga la biblioteca desde JSON
├── exeptions.py         # Define excepciones personalizadas
├── data.json            # Archivo generado para guardar la información persistente
├── main.py              # Inicialización del sistema en terminal
├── data.py              # Definición de las instancias de libros y usuarios (Cuando no existe data.json).
└── README.md            # Documentación general del sistema
```

### Clases principales

**`Library`** <br>
Administra toda la lógica central:
  - Registro de usuarios (register_user)
  - Registro y búsqueda de libros (add_book, search_book)
  - Filtrado de libros disponibles o populares
  - Manejo de errores personalizados

**`Book`** <br>
Representa un libro con atributos como:
  - `title`, `author`, `isbn`
  - `is_available` (estado de préstamo)
  - Métodos utilitarios como `is_popular()` y `from_dict()` (para reconstrucción desde JSON).


**`Student`** y **`Professor`** <br>
Modelos de usuario con características específicas:
- Almacenan libros prestados.
- Implementan métodos from_dict() para reconstrucción desde persistencia.

**`Persistence`** <br>
Encargada de guardar y reconstruir la biblioteca completa:
  - `save(library: Library)` → Serializa y guarda todos los datos en data.json.
  - `load()` → Restaura una instancia completa de Library con sus libros y usuarios.


## Antes de empezar

### Requisitos
- Python 3.10 o superior
- Librerías estándar: json, datetime, typing
- Crea un entorno virtual **con  venv**:

  ```bash
  python3 -m venv python_poo
  source python_poo/bin/activate

  pip3 install -r requirements.txt
  ```


<p style="text-align: center">
  <b>Made with 💜 by Paho</b>
</p>