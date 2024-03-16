from flask import Flask, render_template, request
from totp.gen import gen_url, verify_totp
from dotenv import load_dotenv

app = Flask(__name__)

# Load .env variables
load_dotenv()

@app.route("/")
def index():
    totp_url = gen_url()

    return render_template("index.html", totp_url=totp_url)

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    totp_val = data.get("totp")

    is_valid = verify_totp(totp_val)

    return {
        "is_valid": is_valid
    }

if __name__ == "__main__":
    app.run(debug=True)