import pika
import time

connection = pika.BlockingConnection(
    # pika.URLParameters('amqp://sp86:sp86$12345@192.168.31.155:5672/%2F'))
    pika.URLParameters('amqp://guest:guest@192.168.0.113:5672/%2F'))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()