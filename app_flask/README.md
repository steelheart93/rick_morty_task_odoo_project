# Rick & Morty Task App

App desarrollada en Flask para crear tareas con personajes de Rick and Morty, integradas con Odoo vía XML-RPC.

## 🔧 Requisitos

- Python 3.10+
- PostgreSQL
- Odoo 18 (con módulo personalizado instalado)

## ⚙️ Instalación

```bash
git clone https://github.com/steelheart93/rick_morty_task_odoo_project.git
cd rick_morty_task_project/app_flask

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## ⚙️ Configuración

Crea un archivo `.env` basado en `.env.example`:

```
SECRET_KEY=clave-secreta
DATABASE_URL=postgresql://odoo:odoo@localhost:5432/odoo
```

## 🧱 Inicializar la base de datos

```bash
psql -U odoo -d odoo -f init_db.sql
```

## 🚀 Ejecutar la app Flask

```bash
python run.py
```

Abre: [http://localhost:5000](http://localhost:5000)

---

## 🧩 Módulo de Odoo

1. Copia la carpeta `modules/odoo_rick_tasks` en tu ruta de addons
2. Asegúrate de que `addons_path` incluye `modules` en `odoo.conf`
3. Ejecuta:

```bash
python odoo-bin -c odoo.conf -u odoo_rick_tasks
```

4. Entra a Odoo > Apps > Actualizar lista
5. Instala el módulo **Rick Tasks**
6. Menú: `Rick & Morty > Tareas`

---

## 👤 Usuario de prueba

- Email: `admin@example.com`
- Password: `123456`

---

## 📌 Enviar tarea a Odoo

Crea una tarea desde Flask, asígnale un personaje, y haz clic en **“Enviar a Odoo”**.

Verifica luego en el menú de Odoo → `Rick & Morty > Tareas`.
