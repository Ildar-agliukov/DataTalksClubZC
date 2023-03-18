from json import dumps
from kafka import KafkaProducer
import random
from time import sleep
import gzip
import csv


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         key_serializer=lambda x: dumps(x).encode('utf-8'),
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

with gzip.open('green_tripdata_2019-01.csv.gz', 'rt') as f:
    csvreader = csv.reader(f)
    header = [s.lower() for  s in next(csvreader)]
    counter = 1
    all_ = set()
    for row in csvreader:
        row = dict(zip(header, row))
        producer.send('green_taxi', key='green', value=row)
        print(row)
        sleep(random.random())
