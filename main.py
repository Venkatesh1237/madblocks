#subscriber
import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect('broker.hivemq.com',1883)
print('Broker connected')

client.subscribe('kits/ml')

def notification(client,userdata,msg):
  print(msg.payload)

client.on_message = notification
client.loop_forever()