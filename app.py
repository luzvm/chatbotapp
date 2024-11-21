from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Soy tu bot de atención al cliente. ¿En qué puedo ayudarte?")

# Función para manejar mensajes
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    if "horario" in user_message.lower():
        await update.message.reply_text("Nuestro horario es de 9:00 AM a 6:00 PM, de lunes a viernes.")
    elif "contacto" in user_message.lower():
        await update.message.reply_text("Puedes contactarnos en soporte@empresa.com.")
    else:
        await update.message.reply_text("Gracias por tu mensaje. Un asesor se pondrá en contacto contigo pronto.")

# Función principal
def main():
    TOKEN = os.getenv("TOKEN")  # Cargar el token como variable de entorno

    # Crear la aplicación
    app = ApplicationBuilder().token(TOKEN).build()

    # Configurar comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar el bot
    print("El bot está en funcionamiento...")
    app.run_polling()

if __name__ == "__main__":
    main()
