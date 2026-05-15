import smtplib
import csv
from email.message import EmailMessage

sender_email="your_email@gmail.com"
app_password="your_app_password"

def send_email(receiver_email, receiver_name):
    msg = EmailMessage()
    msg["Subject"]="Pyhton Email Sender Bot"
    msg["From"]=sender_email
    msg["To"]=receiver_email
    msg.set_content(f"Hello {receiver_name}, this email was sent using python")

    with open("sample.txt","r") as file:
        file_data=file.read()
        file_name=file.name
    
    msg.add_attachment(file_data, filename=file_name)

    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email,app_password)
        server.send_message(msg)
        print(f"Email sent to {receiver_name}")
        server.quit()
    except Exception as e:
        print("Error:",e)

with open("emails.csv","r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        name = row[0]
        email = row[1]
        send_email(email, name)
