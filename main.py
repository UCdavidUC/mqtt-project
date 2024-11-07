import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = 'Equipo36'
client_id = f'publish-{random.randint(0,1000)}'
username = ''
password = ''

def main():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

    print('Hello')

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('CONNECTED TO MQTT BROKER')
        else:
            print('Failed to connect, return code %d\n'. rc)

    client = mqtt_client.Client(client_id)
    client.on_connet = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages from rpi: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 100:
            break

if __name__ == "__main__":
    main()
