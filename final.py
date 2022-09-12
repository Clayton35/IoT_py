# Import necessary modules/tools
import smbus
from time import sleep
import time
from datetime import datetime
import RPi.GPIO as GPIO
import dht11_library as dht11
import paho.mqtt.client as mqtt

# Initialize global variables/objects
moist = 0
Volt_light = 0
temp = 0
humid = 0

bus = smbus.SMBus(1)
timer = time.time()

# Initialize GPIO for Temp/Humidity Sensor
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(12)

# Initialize values for ThingSpeak channel
MQTT_CLIENT_ID = "KgIIDQAtFDwILCgsDBQrKRs" # This is for your own client identification. Can be anything
MQTT_USERNAME = "KgIIDQAtFDwILCgsDBQrKRs" #This is the ThingsSpeak's Author
MQTT_PASSWD = "GmQz8qbL6CIZqDBD+AjyG07K" #This is the MQTT API Key found under My Profile in ThingSpeak
MQTT_HOST = "mqtt3.thingspeak.com" #This is the ThingSpeak hostname
MQTT_PORT = 1883 #Typical port # for MQTT protocol. If using TLS -> 8883
CHANNEL_ID = "1709556" #Channel ID found on ThingSpeak website
MQTT_WRITE_APIKEY = "52XVALGD8ASON9SZ" # Write API Key found under ThingSpeak Channel Settings
MQTT_PUBLISH_TOPIC = "channels/" + CHANNEL_ID + "/publish" #+ MQTT_WRITE_APIKEY

# Define moisture sensor write function
def moist_write():
        bus.write_byte(0x4b, 0x8f)
        sleep(0.1)
        moist_read()

# Define function for moisture read
def moist_read():
        global moist
        data = bus.read_byte(0x4b)
        moist = ((data / 140) * 100)

# Define function for luminosity write
def lumin_write():
        bus.write_byte(0x4b, 0xcf)
        sleep(0.1)
        lumin_read()

# Define function for luminosity read
def lumin_read():
        global Volt_light
        raw = bus.read_byte(0x4b)
        Volt_light = ((raw / 255) * 100)

# Define function for temperature/humidity
def temp_humid():
        global temp
        global humid
        global instance
        result = instance.read()
        temp = result.temperature
        humid = result.humidity

# Define Pushlish function
def publish():
        global Volt_light
        global temp
        global humid
        global moist
        global daytime

        daytime = datetime.now().strftime("%H:M%")

        temp_humid()
        moist_write()

        if((daytime > "06:00") and (daytime < "20:30")):
                lumin_write()

        try:
                # create client instance
                client = mqtt.Client(client_id=MQTT_CLIENT_ID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
                # standard callback bindings

                client.on_connect = on_connect
                client.on_publish = on_publish

                # Set the conneciton authentication.
                client.username_pw_set(MQTT_USERNAME, password=MQTT_PASSWD)
                # Connect client
                client.connect(MQTT_HOST, port=MQTT_PORT, keepalive=60)
                # start the looping of client connection. This needs to be done otherwise the connection will only happen once and expire """
                client.loop_start()
        except KeyboardInterrupt:
                client.disconnect()


        sleep(1)
        if not client.is_connected:
                print("Client disconnected. Trying to reconnect.")
                client.reconnect()
        pub_topic = "field1=" + str(humid) + "&field2=" + str(temp) + "&field3=" + str(moist) + "&field4=" + str(Volt_light)
        client.publish(MQTT_PUBLISH_TOPIC, pub_topic)

# Define on connect function
def on_connect(client, userdata, flags, rc):
        print("Connected ", rc)

# Define on publish function
def on_publish(client, userdata, results):
        print("Published ", rc)

# Keeps program running
while True:
        if (time.time() >= timer + 30):
                publish()
                timer = time.time()
        else:
                pass