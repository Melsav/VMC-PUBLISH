import time
import paho.mqtt.client as paho
broker="192.168.1.38"

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001")

client.on_message=on_message

print("connecting to broker ",broker)
client.connect(broker)
client.loop_start()

print("publishing ")
client.publish("sol","1ère mesure temp = 26C°")
client.publish("sol", "2ème mesure temp = 25C°")
time.sleep(4)
client.disconnect()
client.loop_stop()