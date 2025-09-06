# 🛡️ Proyecto Honeypot Simple

Este es un **honeypot educativo** desarrollado en Python.  
Simula servicios comunes (HTTP, SSH y FTP) para detectar y registrar intentos de conexión sospechosos.

⚠️ **Nota:** Este proyecto es únicamente con fines educativos y de práctica en ciberseguridad.  
No debe usarse en entornos de producción ni como reemplazo de soluciones profesionales.

---

## 🚀 Características

- Simulación de 3 servicios:
  - 🌐 HTTP en el puerto **8080**
  - 🔑 SSH en el puerto **2222**
  - 📂 FTP en el puerto **2121**
- Registro de intentos de conexión mediante `logger` (se muestran en consola).
- Código simple y entendible para estudiantes de ciberseguridad.

---

## 📂 Estructura del Proyecto
ProyectoHoneypot/
│── main.py # Arranca los 3 servidores en paralelo
│── servers.py # Contiene la lógica de los servidores falsos
│── logger.py # Configuración del logger
│── config.yml # Configuración general (host, puertos, etc.)
│── .gitignore # Archivos a ignorar en Git

## ⚙️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/honeypot-project.git
   cd honeypot-project

   python3 -m venv .venv
source .venv/bin/activate   # En Linux/WSL
.venv\Scripts\activate      # En Windows

pip install -r requirements.txt

python main.py
