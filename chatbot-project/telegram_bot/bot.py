import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import openai
from dotenv import load_dotenv

# Load API key dari file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Token Telegram Bot dari BotFather
TOKEN = "7698017188:AAHtXw-so8rjBEJ4NmZqAYMhqQZ86SfGJRA"

# Fungsi untuk perintah /start
async def start(update: Update, context):
    await update.message.reply_text("Hi! Saya adalah bot AI. Tanyakan apa saja, dan saya akan mencoba membantu!")

# Fungsi untuk menangani pesan teks dan memberikan respons AI
async def handle_message(update: Update, context):
    user_message = update.message.text

    try:
        # Kirim permintaan ke OpenAI untuk menghasilkan respons
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Balas percakapan berikut: {user_message}",
            max_tokens=100,
            temperature=0.7
        )
        # Ambil respons dari OpenAI
        ai_response = response["choices"][0]["text"].strip()
    except Exception as e:
        ai_response = "Maaf, ada kesalahan saat mencoba memahami pesan Anda."

    # Kirimkan respons ke pengguna
    await update.message.reply_text(ai_response)


# Fungsi utama untuk menjalankan bot
def main():
    # Buat aplikasi bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Tambahkan handler untuk perintah /start
    app.add_handler(CommandHandler("start", start))

    # Tambahkan handler untuk pesan teks
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    app.run_polling()

if __name__ == "__main__":
    main()

import psutil
# Fungsi untuk memeriksa status sistem
async def status(update: Update, context):
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    status_message = (
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory}%\n"
        f"Disk Usage: {disk}%"
    )
    await update.message.reply_text(status_message)

# Tambahkan handler untuk perintah /status
app.add_handler(CommandHandler("status", status))

# Fungsi untuk deploy aplikasi ke server
async def deploy(update: Update, context):
    try:
        # Konfigurasi SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('your_server_ip', username='your_username', password='your_password')

        # Jalankan perintah deploy, misalnya git pull
        stdin, stdout, stderr = ssh.exec_command('cd /path/to/your/app && git pull')
        result = stdout.read().decode('utf-8')

        await update.message.reply_text(f"Deploy Sukses: {result}")
        ssh.close()
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan saat deploy: {str(e)}")

# Tambahkan handler untuk perintah /deploy
app.add_handler(CommandHandler("deploy", deploy))

# Fungsi untuk memantau status dan mengirim peringatan
async def monitor_resources(update: Update, context):
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    if cpu_usage > 80 or memory > 80:
        warning_message = (
            f"Warning: CPU Usage is {cpu_usage}%\n"
            f"Warning: Memory Usage is {memory}%"
        )
        await update.message.reply_text(warning_message)
    else:
        await update.message.reply_text("System is healthy.")

# Tambahkan handler untuk perintah /monitor
app.add_handler(CommandHandler("monitor", monitor_resources))


# Fungsi untuk mengirimkan log aplikasi
async def logs(update: Update, context):
    try:
        with open('/path/to/your/log/file.log', 'r') as f:
            logs = f.readlines()
            recent_logs = "".join(logs[-10:])  # Mengambil 10 baris log terbaru
        await update.message.reply_text(recent_logs)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Tambahkan handler untuk perintah /logs
app.add_handler(CommandHandler("logs", logs))
