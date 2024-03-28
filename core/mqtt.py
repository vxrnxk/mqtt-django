import requests
import paho.mqtt.client as mqtt
from django.conf import settings

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('MQTT Connected')
        mqtt_client.subscribe('mqtt/test')


def on_message(mqtt_client, userdata, msg):
    print(f'New message received on topic: {msg.topic}, payload: {msg.payload}')

    url = f"http://localhost:8000/transaction/{(msg.payload).decode()}/"
    transaction = {
        "id": (msg.payload).decode(),
        "status": "COMPLETED"
    }
    req = requests.put(url, transaction)
    print(req.text)  


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)