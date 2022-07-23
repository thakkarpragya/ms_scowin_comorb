import json
import pika
import django
from sys import path
from os import environ

#path.append('E:\BIT-FSE-Projects\C2-Assignment2\C4 MS\ms_scowin_comorb\ms_scowin_comorb\settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'ms_scowin_comorb.settings') 
django.setup()
from student_comorb.models import Student_reaction

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='studentcomorb')

def callback(ch, method, properties, body):
    print("Received in vacdrive...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'student_created':
        if not isinstance(data,list):
            data = [data]
        for d in data:
            student = Student_reaction.objects.create(id=d['id'], studentName=d['studentName'], existingComorbidites=d['existingComorbidites'])
            student.save()
            print("student created")
        
    elif properties.content_type == 'student_updated':       
        student = Student_reaction.objects.get(id=data['id'])
        student.studentName = data['studentName']       
        student.existingComorbidites = data['existingComorbidites']
        student.save()
        print("student updated")    
  
channel.basic_consume(queue='studentcomorb', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()



