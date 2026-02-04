# Swag Labs AQA

Автоматизированные UI-тесты для [Swag Labs](https://www.saucedemo.com/) — демо-сайта интернет-магазина от Sauce Labs.

## Технологии

- **Python 3.x**
- **Selenium WebDriver** — автоматизация браузера
- **Pytest** — тестовый фреймворк
- **Page Object Model** — паттерн проектирования тестов
- **webdriver-manager** — автоматическое управление драйверами

## Структура проекта

```
swag-labs-aqa/
├── pages/                  # Page Object классы
│   ├── base_page.py        # Базовый класс страницы
│   ├── login_page.py       # Страница авторизации
│   ├── main_page.py        # Главная страница (каталог)
│   ├── card_page.py        # Страница карточки товара
│   ├── nav_bar_page.py     # Навигационная панель
│   ├── footer_page.py      # Футер
│   └── locators.py         # Локаторы элементов
├── test_login_page.py      # Тесты авторизации
├── test_main_page.py       # Тесты главной страницы
├── test_card_page.py       # Тесты карточки товара
├── test_nav_bar.py         # Тесты навигации
├── test_footer.py          # Тесты футера
├── config.py               # Конфигурация (URL, credentials, timeouts)
├── conftest.py             # Pytest фикстуры
├── pytest.ini              # Настройки pytest
└── requirements.txt        # Зависимости
```

## Установка

```bash
# Клонировать репозиторий
git clone <repository-url>
cd swag-labs-aqa

# Создать виртуальное окружение
python -m venv .venv

# Активировать виртуальное окружение
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

## Запуск тестов

```bash
# Запустить все тесты
pytest

# Запустить с подробным выводом
pytest -v

# Запустить smoke-тесты
pytest -m smoke

# Запустить тесты авторизации
pytest -m login

# Запустить тесты навигации
pytest -m navigation

# Запустить конкретный тестовый файл
pytest test_login_page.py
```

## Маркеры тестов

| Маркер | Описание |
|--------|----------|
| `smoke` | Smoke-тесты |
| `regression` | Регрессионные тесты |
| `login` | Тесты авторизации |
| `navigation` | Тесты навигации |
