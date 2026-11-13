import requests
import time
from datetime import datetime

# БОТ-И ТИЛЛО - XAU/USD
def get_gold_price():
    try:
        # Нархи тилло аз API
        url = "https://api.gold-api.com/price/XAU"
        r = requests.get(url, timeout=10)
        data = r.json()
        price = data.get('price', 0)
        return price
    except:
        return 0

def check_signal(price):
    # Сигнали оддӣ барои тилло
    if price == 0:
        return "❌ Хатои пайвастшавӣ"
    
    now = datetime.now().strftime("%H:%M:%S")
    signal = f"""
🏆 GOLD BOT - XAU/USD 🏆
💰 Нарх: ${price}
⏰ Вақт: {now}

📊 ТАҲЛИЛ:
"""
    # Сигнали оддӣ
    if price > 2000:
        signal += "🔥 Тилло қимат! SELL фикр кунед!\n"
    else:
        signal += "💎 Тилло арзон! BUY фикр кунед!\n"
    
    signal += "\n✅ Бот кор мекунад!"
    return signal

print("Бот оғоз шуд...")
while True:
    price = get_gold_price()
    msg = check_signal(price)
    print(msg)
    time.sleep(60) # ҳар 1 дақиқа
