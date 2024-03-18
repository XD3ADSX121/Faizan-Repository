import paho.mqtt.client as mqtt
broker_address = "mqtt.eclipseprojects.io"

port = 1883 

topic = "wave_tracker/frequency"

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to MQTT Broker")

        client.subscribe(topic)

    else:

        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):

    print("Received wave frequency:", msg.payload.decode(), "Hz")


client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message

client.connect(broker_address, port)

client.loop_forever()