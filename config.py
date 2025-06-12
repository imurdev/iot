
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8146345784:AAEkrCY9wKygOnS7NAmwtCgxwG1-KnXenjA"
AUTHORIZED_USER_ID = 307247876

MQTT_BROKER = os.environ.get("MQTT_BROKER") or "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPICS = [
    "windowbot/rozkr/temp",
    "windowbot/arm/temp",
    "windowbot/zvar/temp",
    "windowbot/zach/temp",
    "windowbot/sklo/temp",
    "windowbot/kontrol/temp"
]
