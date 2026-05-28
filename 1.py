"""
NIVEL 1 — Ejercicios completos
Esquema: Estudiantes / Cursos

Antes de empezar, crea la DB ejecutando el setup al final de este archivo.
Cada función tiene un ejercicio. Completa las líneas con "pass".

Para ver las soluciones, ejecuta:
    python 03_ejercicios.py --soluciones
"""

import sqlite3
import sys

DB_PATH = "academia.db"


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def select_01():
    """Mostrar todos los datos de todos los estudiantes."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("select * from estudiantes")
    print('select 01')
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_02():
    """Mostrar nombre, apellido y email de estudiantes nacidos después del 2001."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        select nombre, apellido, email
        from estudiantes
        where fecha_nacimiento > '2001-12-31'
    """)
    print('select 02')
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_03():
    """Mostrar nombre y créditos de los cursos ordenados por créditos descendente."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        select nombre, creditos
        from cursos
        order by creditos desc
    """)
    print('select 03')
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_04():
    """Mostrar nombre del estudiante, nombre del curso y nota (JOIN)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        select e.nombre as estudiante,
               c.nombre as curso,
               i.nota
        from inscripciones i
        join estudiantes e on i.estudiante_id = e.id
        join cursos c on i.curso_id = c.id
    """)
    print('select 04')
    for r in cursor.fetchall():
        print(dict(r))
    conn.close()


def select_05():
    """Mostrar cuántos estudiantes hay (columna: total)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        select count(*) as total
        from estudiantes
    """)
    print('select 05')
    print(dict(cursor.fetchone()))
    conn.close()


def insert_01():
    """Insertar estudiante: María Torres, maria.torres@email.com, 2004-08-12."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        insert into estudiantes (nombre, apellido, email, fecha_nacimiento)
        values ('María', 'Torres', 'maria.torres@email.com', '2004-08-12')
    """)
    conn.commit()
    print('insert 01')
    print("[OK] Estudiante insertado.")
    conn.close()


def insert_02():
    """Insertar curso: Historia del Arte, créditos 3."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        insert into cursos (nombre, descripcion, creditos)
        values ('Historia del Arte', 'Arte e historia', 3)
    """)
    conn.commit()
    print('insert 02')
    print("[OK] Curso insertado.")
    conn.close()


def insert_03():
    """Inscribir a Ana López (id=1) en Bases de Datos (id=3)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        insert into inscripciones (estudiante_id, curso_id)
        values (1, 3)
    """)
    conn.commit()
    print('insert 03')
    print("[OK] Inscripcion insertada.")
    conn.close()


def insert_04():
    """Insertar dos estudiantes a la vez: Valentina Ruiz y Mateo Torres."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        insert into estudiantes (nombre, apellido, email, fecha_nacimiento)
        values 
        ('Valentina', 'Ruiz', 'valentina.ruiz@email.com', '2003-05-14'),
        ('Mateo', 'Torres', 'mateo.torres@email.com', '2002-10-20')
    """)
    conn.commit()
    print('insert 04')
    print("[OK] Estudiantes insertados.")
    conn.close()


def update_01():
    """Actualizar email de Carlos Mendoza (id=2) a carlos.m@email.com."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        update estudiantes
        set email = 'carlos.m@email.com'
        where id = 2
    """)
    conn.commit()
    print('update 01')
    print("[OK] Email actualizado.")
    conn.close()


def update_02():
    """Cambiar créditos de Inglés Técnico (id=4) a 3."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        update cursos
        set creditos = 3
        where id = 4
    """)
    conn.commit()
    print('update 02')
    print("[OK] Creditos actualizados.")
    conn.close()


def update_03():
    """Poner nota 14.5 a Sofía Ramírez (id=5) en Programación Python (curso_id=2)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        update inscripciones
        set nota = 14.5
        where estudiante_id = 5 and curso_id = 2
    """)
    conn.commit()
    print('update 03')
    print("[OK] Nota actualizada.")
    conn.close()


def delete_01():
    """Eliminar la inscripción con id=5."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        delete from inscripciones
        where id = 5
    """)
    conn.commit()
    print('delete 01')
    print("[OK] Inscripcion eliminada.")
    conn.close()


def delete_02():
    """Eliminar inscripciones con nota NULL."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        delete from inscripciones
        where nota is null
    """)
    conn.commit()
    print('delete 02')
    print(f"[OK] {cursor.rowcount} inscripcion(es) eliminada(s).")
    conn.close()


def delete_03():
    """Eliminar cursos sin estudiantes inscritos (usar NOT IN)."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        delete from cursos
        where id not in (
            select curso_id
            from inscripciones
        )
    """)
    conn.commit()
    print('delete 03')
    print(f"[OK] {cursor.rowcount} curso(s) eliminado(s).")
    conn.close()






# =========================================================
# SETUP: crear DB con datos
# =========================================================

def crear_db():
    import os
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            fecha_inscripcion DATE DEFAULT CURRENT_DATE
        );
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            creditos INTEGER NOT NULL CHECK(creditos > 0)
        );
        CREATE TABLE inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            curso_id INTEGER NOT NULL,
            fecha_inscripcion DATE DEFAULT CURRENT_DATE,
            nota REAL CHECK(nota >= 0 AND nota <= 20),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES
            (1, 'Ana', 'López', 'ana.lopez@email.com', '2002-03-15', '2024-03-01'),
            (2, 'Carlos', 'Mendoza', 'carlos.mendoza@email.com', '2001-07-22', '2024-03-01'),
            (3, 'Lucía', 'Fernández', 'lucia.fernandez@email.com', '2003-01-10', '2024-03-01'),
            (4, 'Pedro', 'García', 'pedro.garcia@email.com', '2000-11-05', '2024-03-01'),
            (5, 'Sofía', 'Ramírez', 'sofia.ramirez@email.com', '2002-09-18', '2024-03-01');
        INSERT INTO cursos VALUES
            (1, 'Matemáticas I', 'Álgebra y cálculo', 5),
            (2, 'Programación en Python', 'Introducción con Python', 4),
            (3, 'Bases de Datos', 'Bases relacionales', 4),
            (4, 'Inglés Técnico', 'Inglés aplicado a tecnología', 2);
        INSERT INTO inscripciones (id, estudiante_id, curso_id, fecha_inscripcion, nota) VALUES
            (1, 1, 1, '2024-03-05', 18.5),
            (2, 1, 2, '2024-03-05', 16.0),
            (3, 2, 1, '2024-03-06', 14.0),
            (4, 2, 3, '2024-03-06', 17.5),
            (5, 3, 2, '2024-03-07', 19.0),
            (6, 3, 3, '2024-03-07', 15.5),
            (7, 4, 1, '2024-03-08', 12.0),
            (8, 4, 4, '2024-03-08', 18.0),
            (9, 5, 2, '2024-03-09', NULL),
            (10, 5, 3, '2024-03-09', NULL);
    """)
    conn.commit()
    conn.close()
    print(f"[OK] Base de datos '{DB_PATH}' creada.\n")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    if "--soluciones" in sys.argv:
        crear_db()
        print("Soluciones creadas.")
    else:
        crear_db()
        print("Ejercicios creados.")
        select_01()
        select_02()
        select_03()
        select_04()
        select_05()

        insert_01()
        insert_02()
        insert_03()
        insert_04()

        update_01()
        update_02()
        update_03()

        delete_01()
        delete_02()
        delete_03()
