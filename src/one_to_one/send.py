import pika
import sys

# credentials = pika.PlainCredentials('sp86', 'sp86$12345')
credentials = pika.PlainCredentials('guest', 'guest')
# parameters = pika.ConnectionParameters('192.168.31.155',
parameters = pika.ConnectionParameters('192.168.0.113',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True, exclusive=False, auto_delete=False)

message = ' '.join(sys.argv[1:]) or "Hi, I'm Shahriar Parvez. This is a simple msg for testing!"
channel.basic_publish(exchange='',
                  routing_key='task_queue',
                  body= message,
                  properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ))
print("[x] msg is sent!")
connection.close()