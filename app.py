from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load planes.json safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "planes.json")) as f:
    planes = json.load(f)


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Ask GoAI
@app.route("/ask", methods=["POST"])
def ask():

    question = request.json["question"].lower()

    # plane comparison
    if "vs" in question:

        parts = question.split("vs")
        p1 = parts[0].strip()
        p2 = parts[1].strip()

        for plane1 in planes:
            for plane2 in planes:
                if plane1.lower() in p1 and plane2.lower() in p2:

                    return jsonify({
                        "answer":
                        f"{plane1} vs {plane2}\n\n"
                        f"{plane1} speed: {planes[plane1]['speed']}\n"
                        f"{plane2} speed: {planes[plane2]['speed']}\n\n"
                        f"{plane1} weapons: {planes[plane1]['weapons']}\n"
                        f"{plane2} weapons: {planes[plane2]['weapons']}"
                    })

    # smarter plane search
    for plane in planes:

        if plane.lower() in question or any(word in plane.lower() for word in question.split()):

            data = planes[plane]

            return jsonify({
                "answer":
                f"{plane}\n\n"
                f"Nation: {data['nation']}\n"
                f"Speed: {data['speed']}\n"
                f"Climb: {data['climb']}\n"
                f"Weapons: {data['weapons']}\n\n"
                f"Tip: {data['tip']}",
                "image": data["image"]
            })

    return jsonify({
        "answer": "Plane not found. Try MiG-3, Su-27, F-16, F-22 or Bf 109."
    })


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
