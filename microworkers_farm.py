import json
import random
from datetime import datetime

ACCOUNTS_FILE = "microworkers_accounts.json"
LOG_FILE = "microworkers_earnings_log.json"

def load_accounts():
    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def perform_tasks(account):
    email = account.get("email")
    proxy = account.get("proxy")
    print(f"[+] Виконано завдання для {email} через {proxy}")
    earned = round(random.uniform(0.1, 1.5), 2)  # Мокаємо заробіток
    log_earning(email, earned)
    return earned

def log_earning(email, amount):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "account": email,
        "earned_usd": amount
    }
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print(f"[ERROR] Не вдалося записати лог: {e}")

def main():
    print("--- MICROWORKERS FARM STARTED ---")
    accounts = load_accounts()
    total = 0.0
    for i, acc in enumerate(accounts):
        try:
            earned = perform_tasks(acc)
            print(f"[{i}] {acc['email']} → +{earned} USD")
            total += earned
        except Exception as e:
            print(f"[{i}] {acc['email']} → ERROR: {e}")
    print(f"[OK] Загальний заробіток: {round(total, 2)} USD")

if __name__ == "__main__":
    main()
