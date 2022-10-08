import requests
from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/bot',methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body','').strip()
    print(incoming_msg)
    
if __name__ == '__main__':
    pass
