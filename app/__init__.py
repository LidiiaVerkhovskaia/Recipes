from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Инициализация расширения для работы с базой данных
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)

    # Загрузка конфигурации из класса Config
    app.config.from_object(config_class)

    db.init_app(app)

    # Импорт и регистрация блупринтов
    from app.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
