from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    return Response("""
    <Response>
        <Start>
            <Stream url="wss://your-websocket-server.onrender.com/audio" />
        </Start>
        <Say voice="Polly.Mia" language="sv-SE">
            Hej! Du pratar med Mohammed från Theos höbalar AB.
        </Say>
    </Response>
    """, mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
