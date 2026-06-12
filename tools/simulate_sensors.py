import json, time, random, os, signal, sys
import paho.mqtt.client as mqtt

BROKER = os.getenv('MQTT_BROKER', 'localhost')
PORT = int(os.getenv('MQTT_PORT', '1883'))

SENSORS = [
    {'id': 'capteur-01', 'location': 'salle-serveurs'},
    {'id': 'capteur-02', 'location': 'atelier-A'},
    {'id': 'capteur-03', 'location': 'entrepot-B'},
]

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

def stop(*_):
    print('\nArret du simulateur...')
    client.loop_stop()
    client.disconnect()
    sys.exit(0)

signal.signal(signal.SIGINT, stop)

print(f'Publication vers {BROKER}:{PORT} (Ctrl+C pour arreter)')
while True:
    for s in SENSORS:
        payload = {
            'temperature': round(random.uniform(18.0, 45.0), 2),
            'pression': round(random.uniform(980.0, 1050.0), 2),
            'vibration': round(random.uniform(0.0, 5.0), 3),
            'batterie': round(random.uniform(20.0, 100.0), 1),
            'device_id': s['id'],
            'location': s['location'],
        }
        topic = f"sensors/{s['id']}/telemetry"
        client.publish(topic, json.dumps(payload), qos=0)
        print(f'[OK] {topic} -> {payload}')
    time.sleep(5)
