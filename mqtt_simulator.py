
import time
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)

stages = ["rozkr", "arm", "zvar", "zach", "sklo", "kontrol"]

while True:
    for stage in stages:
        temp = random.randint(30, 90)
        topic = f"windowbot/{stage}/temp"
        client.publish(topic, temp)
        print(f"[MQTT] {topic} => {temp}")
    time.sleep(5)
