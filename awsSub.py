import os
from dotenv import load_dotenv
from time import sleep
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT

load_dotenv()

endpoint = os.getenv("ENDPOINT")
client_id = 'sub'
path_certificate = './certificados/esp32.pem.crt'
path_privatekey = './certificados/esp32-private.pem.key'
path_rootca1 = './certificados/AmazonRootCA1.pem'


my_awsmqtt_client = AWSIoTMQTT.AWSIoTMQTTClient(client_id)
my_awsmqtt_client.configureEndpoint(endpoint, 8883)
my_awsmqtt_client.configureCredentials(path_rootca1, path_privatekey, path_certificate)


print('-' * 100)
print('MQTT Subscriber'.center(100))
topic = input('\nInscrever-se no tópico: ')

my_awsmqtt_client.connect()


def customCallback(client, userdata, message):
    print(message.payload.decode("utf-8"))

my_awsmqtt_client.subscribe(topic, 1, customCallback)
print(f'\nInscrito com sucesso no tópico [{topic}]! Pressione Enter para sair...\n')
x = input()

my_awsmqtt_client.unsubscribe(topic)
print("Cliente não mais inscrito...") 

my_awsmqtt_client.disconnect()
print("Cliente desconectado!")