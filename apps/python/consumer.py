from kafka import KafkaConsumer
import json,sys

# get the confit file as input paremeter
argv = sys.argv[1]

# load the config file 
with open(argv) as json_data_file:
    data = json.load(json_data_file)

# Create the consumer 
consumer = KafkaConsumer(data['topic'], 
                         bootstrap_servers=data['bootstrap.servers'], 
                         ssl_cafile=data['ssl.ca.location'], 
                         security_protocol=data['security.protocol'],
                         sasl_mechanism=data['sasl.mechanisms'],
                         sasl_plain_username=data['sasl.username'],
                         sasl_plain_password=data['sasl.password'],
                         auto_offset_reset=data['offset'], 
                         enable_auto_commit=data['auto.commit'])

# Read the message from Topic 
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`©
    print ("%s:%d:%d: value=%s" % (message.topic, message.partition,message.offset,message.value))