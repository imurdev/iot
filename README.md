# Telegram IoT Бот для автоматизації виробництва

## 📦 Функціонал:
- 📈 Графіки для 6 дільниць
- ⚙️ Задання порогів для кожної дільниці
- 📁 Вивантаження логів (.txt)
- 🛠️ Налаштування (мова, частота оновлення)
- 👑 Адмін-панель: додавання користувачів, перегляд логів
- ⬅️ Кнопка "Назад" у всіх підменю

## ⚙️ Стек:
- Python
- Telegram Bot API
- HiveMQ MQTT Broker
- Node-RED (опціонально для розширення)
- ESP32 (на рівні пристроїв)

## ▶️ Запуск:
1. Встановити залежності:
    ```
    pip install -r requirements.txt
    ```

2. Запустити MQTT симулятор:
    ```
    python mqtt_simulator.py
    ```

3. Запустити бота:
    ```
    python main.py
    ```

## 📡 MQTT топіки:
- windowbot/rozkr/temp
- windowbot/arm/temp
- windowbot/zvar/temp
- windowbot/zach/temp
- windowbot/sklo/temp
- windowbot/kontrol/temp

## 🧠 Автор: Семен Сичов
