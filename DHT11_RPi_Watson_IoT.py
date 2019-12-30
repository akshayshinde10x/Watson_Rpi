from time import sleep
import Adafruit_DHT
import paho.mqtt.client as mqtt

gpio=17
sensor=Adafruit_DHT.DHT11
ORG = "*******"
DEVICE_TYPE = "RPi" 
TOKEN = "***********"
DEVICE_ID = "********"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/temperature/fmt/json";
pubTopic2 = "iot-2/evt/humidity/fmt/json";
subTopic = "iot-2/type/+/id/+/evt/+/fmt/+";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)


while True:
    mqttc.publish(pubTopic1, temperature)
    mqttc.publish(pubTopic2, humidity)
    print ("Published")
    sleep(5);


mqttc.loop_forever()
