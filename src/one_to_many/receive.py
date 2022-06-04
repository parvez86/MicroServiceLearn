import pika

connection = pika.BlockingConnection(
    pika.URLParameters('amqp://sp86:sp86$12345@192.168.31.155:5672/%2F'))
channel = connection.channel()

channel.exchange_declare(exchange='amqp', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()