from application import create_app, db
from flask_migrate import Migrate

# Создаем приложение и подключаем миграции
app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Запуск сервера
    app.run(host='0.0.0.0', port=7345)