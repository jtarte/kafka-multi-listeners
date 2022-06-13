from kafka import KafkaProducer
import json,sys,time

# get the confit file as input paremeter
argv = sys.argv[1]

# load the config file 
with open(argv) as json_data_file:
    data = json.load(json_data_file)

# Create the kafka producer
producer = KafkaProducer(bootstrap_servers=data['bootstrap.servers'], 
                         ssl_cafile=data['ssl.ca.location'], 
                         security_protocol=data['security.protocol'],
                         sasl_mechanism=data['sasl.mechanisms'],
                         sasl_plain_username=data['sasl.username'],
                         sasl_plain_password=data['sasl.password'])

# Send 100 message to the target topic 
for i in range(100):
    t = time.ctime(time.time())
    message = {'value': i,'time': t}
    producer.send(data['topic'], json.dumps(message).encode('utf_8'))
# Flush the messages to the topic 
producer.flush()

