import pika
import sys

credentials = pika.PlainCredentials('sp86', 'sp86$12345')
parameters = pika.ConnectionParameters('192.168.31.155',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='amqp', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hi, I'm Shahriar Parvez. This is a simple msg for testing!"

channel.basic_publish(exchange='logs',
                  routing_key='',
                  body=message)
print("[x] msg is sent!")
connection.close()