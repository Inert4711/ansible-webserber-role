from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Настройки из переменных окружения
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'app_db')
DB_USER = os.getenv('DB_USER', 'app_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'super_secret_password')

@app.route('/')
def index():
    return "Flask Backend is running!"

@app.route('/api/status')
def status():
    try:
        # Проверяем подключение к БД
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return jsonify({
        "status": "running",
        "backend": "Flask",
        "database": db_status,
        "message": "Full stack is working!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)