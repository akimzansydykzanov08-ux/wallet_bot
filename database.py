import sqlite3

DB_NAME = "wallet.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount INTEGER,
    type TEXT,
    date TEXT DEFAULT  CURRENT_DATE
    )
    """)
    conn.commit()
    conn.close()
    print("База данных успешно инициализирована!")

def get_today_expenses(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = "expense" AND date = CURRENT_DATE', 
        (user_id,))
    spent = cursor.fetchone()[0] or 0
    conn.close()
    return spent

def add_transaction(user_id, amount, trans_type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions (user_id, amount, type) VALUES (?, ?, ?)
    """, (user_id, amount, trans_type))
    conn.commit()
    conn.close()
    print("транзакция добавлена")


def get_balance(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = "income"', (user_id,)
        )
    income = cursor.fetchone()[0] or 0

    cursor.execute(
        'SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = "expense"', (user_id,)
        )
    expense = cursor.fetchone()[0] or 0
    conn.close()
    return income , expense

