 import json
import random

ACCOUNTS_FILE = "microworkers_accounts.json"

def load_accounts():
    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def perform_tasks(account):
    email = account.get("email")
    proxy = account.get("proxy")
    # Тут буде логіка підключення до Microworkers через проксі
    # та автоматичного виконання завдань.
    print(f"[+] Виконано завдання для {email} через {proxy}")
    return round(random.uniform(0.1, 1.5), 2)  # Мокаємо заробіток

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
