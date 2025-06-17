
import requests
from telegram.ext import Updater, CommandHandler
import os

def get_match_probabilities(team1, team2):
    return {
        "team1": 45,
        "draw": 30,
        "team2": 25
    }

def analisar(update, context):
    if len(context.args) < 3:
        update.message.reply_text("Uso correto: /analisar Time1 vs Time2")
        return

    try:
        vs_index = context.args.index('vs')
        team1 = " ".join(context.args[:vs_index])
        team2 = " ".join(context.args[vs_index+1:])

        probs = get_match_probabilities(team1, team2)

        message = f"Probabilidades para {team1} vs {team2}:
"
        message += f"🏆 Vitória {team1}: {probs['team1']}%
"
        message += f"⚖️ Empate: {probs['draw']}%
"
        message += f"🥇 Vitória {team2}: {probs['team2']}%"
        update.message.reply_text(message)
    except Exception as e:
        update.message.reply_text(f"Erro: {str(e)}")

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("analisar", analisar))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
