# Pasos para terminar la entrega

El código ya está listo y probado. Faltan 3 cosas que necesitan tus cuentas.
Cambia `TU_USUARIO_GITHUB`, `TU_REPOSITORIO` y `TU_USUARIO_PA` por los tuyos.

---

## 1. Crear tu usuario del administrador (en tu PC)

Abre PowerShell en esta carpeta y ejecuta:

```
.\venv\Scripts\python.exe manage.py createsuperuser
```

Te pide usuario, correo (puede ir vacío) y contraseña. Luego guarda la base de datos con ese usuario:

```
git add db.sqlite3
git commit -m "Superusuario del administrador"
```

## 2. Subir a GitHub

1. En github.com: **New repository** → nombre (ej. `parcial-final-django`) → **Public** → sin README → **Create repository**.
2. En PowerShell, en esta carpeta:

```
git remote set-url origin https://github.com/TU_USUARIO_GITHUB/TU_REPOSITORIO.git
git push -u origin main
```

3. Revisa en GitHub que aparezca el archivo `db.sqlite3`.

## 3. Desplegar en PythonAnywhere (consola **$ Bash**)

```
git clone https://github.com/TU_USUARIO_GITHUB/TU_REPOSITORIO.git
python3 -m venv venv
source venv/bin/activate
cd TU_REPOSITORIO
pip install -r requirements.txt
python manage.py collectstatic --noinput
pwd
```

Luego en la pestaña **Web**:

1. **Add a new web app** → Next → **Manual configuration** → **Python 3.13** → Next.
2. **Virtualenv:** `/home/TU_USUARIO_PA/venv`
3. **WSGI configuration file:** borra todo y deja:

```python
import os
import sys

path = '/home/TU_USUARIO_PA/TU_REPOSITORIO'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. **Static files:** URL `/static/` → Directory `/home/TU_USUARIO_PA/TU_REPOSITORIO/static_publico`
5. Botón verde **Reload**.

> `settings.py` ya tiene `DEBUG = False`, `ALLOWED_HOSTS` con `.pythonanywhere.com` y `STATIC_ROOT`.
> No hace falta editarlo en el servidor.

## 4. Verificar y entregar

- `https://TU_USUARIO_PA.pythonanywhere.com/programas/crear/` → formulario con 6 programas.
- `https://TU_USUARIO_PA.pythonanywhere.com/admin/` → admin con estilos (entra con el usuario del paso 1).

En la plataforma pega:

- `https://github.com/TU_USUARIO_GITHUB/TU_REPOSITORIO`
- `https://TU_USUARIO_PA.pythonanywhere.com/programas/crear/`

### Si algo falla
Pestaña **Web → Error log**. Los errores más comunes están en el paso 21 de la guía del profesor.
