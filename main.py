"""Chat de consola con la API de Gemini."""

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# El historial se conserva en memoria mientras el programa está abierto.
MODEL = "gemini-3.5-flash-lite"


def main():
    # Busca .env junto a este archivo, aunque se ejecute desde otra carpeta.
    load_dotenv(Path(__file__).resolve().parent / ".env")
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("Falta GEMINI_API_KEY. Agrégala al archivo .env y vuelve a ejecutar.")
        return

    print("Chatbot con Gemini. Escribe 'salir' para terminar.\n")
    try:
        with genai.Client(api_key=api_key) as client:
            chat = client.chats.create(model=MODEL)
            while True:
                try:
                    mensaje = input("Tú: ").strip()
                except (EOFError, KeyboardInterrupt):
                    print("\nHasta luego.")
                    break

                if mensaje.lower() == "salir":
                    print("Hasta luego.")
                    break
                if not mensaje:
                    continue

                try:
                    respuesta = chat.send_message(mensaje)
                    print(f"Gemini: {respuesta.text or 'No se recibió una respuesta de texto.'}\n")
                except errors.APIError as error:
                    if error.code == 503:
                        print("El servicio no está disponible temporalmente. Inténtalo de nuevo.\n")
                    else:
                        print(f"Error de la API (código {error.code}). Revisa tu clave, acceso al modelo y cuota.\n")
                except Exception:
                    print("No fue posible obtener una respuesta. Revisa tu conexión e inténtalo de nuevo.\n")
    except Exception:
        print("No fue posible iniciar el cliente de Gemini. Revisa la configuración e inténtalo de nuevo.")


if __name__ == "__main__":
    main()
