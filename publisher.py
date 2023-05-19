import paho.mqtt.client as mqtt

broker_address = "localhost"
broker_port = 1883
topic = "Task"

# Create a MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish a message to the topic
message = "Hello, Its me Intern!"
client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()
