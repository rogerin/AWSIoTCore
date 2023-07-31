import os
from dotenv import load_dotenv
from time import sleep
import AWSIoTPythonSDK.MQTTLib as AWSIoTMQTT

load_dotenv()

endpoint = os.getenv("ENDPOINT")
client_id = 'pub'
path_certificate = './certificados/esp32.pem.crt'
path_privatekey = './certificados/esp32-private.pem.key'
path_rootca1 = './certificados/AmazonRootCA1.pem'


my_awsmqtt_client = AWSIoTMQTT.AWSIoTMQTTClient(client_id)
my_awsmqtt_client.configureEndpoint(endpoint, 8883)
my_awsmqtt_client.configureCredentials(path_rootca1, path_privatekey, path_certificate)

my_awsmqtt_client.connect()

topic = 'test/status'
msg = 'Hello World'
print('Inicio publicação')

for i in range(5):
    my_awsmqtt_client.publish(topic,f' {i} {msg} ',1)
    print(f'publicacao 0{i+1}: {msg} ao topico {topic}')
    sleep(0.5)

print('fim publicacao')

my_awsmqtt_client.disconnect()