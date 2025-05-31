from flask import Flask, render_template, request
from db.redis_client import get_redis_connection
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    projects = []
    searched = False
    if request.method == "POST":
        pincode = request.form.get("pincode")
        r = get_redis_connection()
        key = f"projects:{pincode}"
        data = r.get(key)
        if data:
            projects = json.loads(data)
        searched = True
    return render_template("index.html", projects=projects, searched=searched)

if __name__ == "__main__":
    app.run(debug=True)