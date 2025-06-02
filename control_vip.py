import telebot
import json
import datetime

TOKEN = "7914065123:AAHCuA8DS8Cv7_2bE9vkfIXLucI9y9b1yG4"
DATA_FILE = "saas_core/licencias.json"

bot = telebot.TeleBot(TOKEN)

def guardar(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def cargar():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@bot.message_handler(commands=['start', 'ayuda'])
def ayuda(m):
    texto = ("🎯 GROWTH MASTER PRO VIP\n\n"
             "Comandos disponibles:\n"
             "/activar ID DÍAS\n"
             "/licencias\n"
             "/exportar\n"
             "/eliminar ID\n"
             "/ayuda")
    bot.send_message(m.chat.id, texto)

@bot.message_handler(commands=['activar'])
def activar(m):
    try:
        args = m.text.split()
        user_id = args[1]
        dias = int(args[2])
        data = cargar()
        fecha_exp = (datetime.datetime.now() + datetime.timedelta(days=dias)).strftime("%Y-%m-%d")
        data[user_id] = fecha_exp
        guardar(data)
        bot.send_message(m.chat.id, f"✅ Licencia activada para {user_id} por {dias} días.")
    except:
        bot.send_message(m.chat.id, "❌ Formato incorrecto. Usa: /activar ID DÍAS")

@bot.message_handler(commands=['licencias'])
def licencias(m):
    data = cargar()
    if not data:
        bot.send_message(m.chat.id, "📋 No hay licencias activas.")
        return
    mensaje = "📋 Licencias activas:\n"
    for user, fecha in data.items():
        mensaje += f"{user}: vence el {fecha}\n"
    bot.send_message(m.chat.id, mensaje)

@bot.message_handler(commands=['exportar'])
def exportar(m):
    data = cargar()
    export = json.dumps(data, indent=2)
    bot.send_message(m.chat.id, f"📦 Exportación de datos:\n{export}")

@bot.message_handler(commands=['eliminar'])
def eliminar(m):
    try:
        user_id = m.text.split()[1]
        data = cargar()
        if user_id in data:
            del data[user_id]
            guardar(data)
            bot.send_message(m.chat.id, f"✅ Licencia eliminada para {user_id}.")
        else:
            bot.send_message(m.chat.id, f"❌ ID {user_id} no encontrado.")
    except:
        bot.send_message(m.chat.id, "❌ Formato: /eliminar ID")

# Inicia el bot
bot.send_message(TOKEN.split(":")[0], "✅ Bot GrowthMaster VIP iniciado correctamente.")
bot.infinity_polling()
