# Chatbot con Gemini

Ejemplo de chatbot de consola en Python para practicar el uso de la API de Gemini. Conserva el contexto de la conversación mientras el programa permanece abierto; al cerrarlo, el historial se pierde.

## Requisitos

- Python 3.10 o posterior y conexión a Internet.
- Una clave de la API de Gemini. Puedes crearla en [Google AI Studio](https://aistudio.google.com/apikey).
- Acceso al modelo `gemini-3.1-flash-lite` desde tu cuenta. El uso de la API está sujeto a disponibilidad, cuotas y posibles cargos según tu cuenta y plan.

## Preparación en Windows

Abre PowerShell en la carpeta `chatbot_gemini` y crea un entorno virtual:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si tienes otra versión compatible, puedes usar `py -m venv .venv`. Si PowerShell bloquea la activación, abre **Símbolo del sistema** y ejecuta `.venv\Scripts\activate.bat`, o consulta la documentación de Python sobre [entornos virtuales](https://docs.python.org/es/3/library/venv.html).

Con el entorno activado, instala las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Copia el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

En Símbolo del sistema puedes usar `copy .env.example .env`. Abre `.env` en un editor y coloca tu clave después del signo `=`:

```dotenv
GEMINI_API_KEY=tu_clave_aqui
```

Guarda el archivo. No compartas tu clave ni subas `.env` a Git; ya está incluido en `.gitignore`. Si ya existe una variable de entorno `GEMINI_API_KEY`, esa variable tiene prioridad sobre el archivo `.env`.

## Ejecución

Con el entorno virtual activado y desde esta carpeta, ejecuta:

```powershell
python main.py
```

Escribe un mensaje y presiona Enter. El chatbot recordará los mensajes anteriores de esa sesión. Escribe `salir` para terminar; también puedes usar Ctrl+C.

Si aparece un error, verifica la clave, la conexión, la cuota y que tu cuenta tenga acceso al modelo. El nombre del modelo se puede cambiar en la constante `MODEL` de `main.py` por otro modelo de texto disponible para tu cuenta.

El SDK oficial y su ejemplo de chat están documentados en [Google AI for Developers](https://ai.google.dev/api/generate-content#chat).
