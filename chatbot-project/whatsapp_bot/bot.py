from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    msg = request.form.get("Body")
    response = MessagingResponse()
    response.message(f"Hi! You said: {msg}")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
