from flask import Flask, render_template, request, jsonify
import json
import os
from rapidfuzz import process

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "planes.json")) as f:
    planes = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


def find_plane(user_input):
    plane_names = list(planes.keys())
    match = process.extractOne(user_input, plane_names)

    if match and match[1] > 60:
        return match[0]

    return None


@app.route("/ask", methods=["POST"])
def ask():

    question = request.json["question"].lower()

    # --- plane comparison ---
    if "vs" in question:

        p1, p2 = question.split("vs")

        plane1 = find_plane(p1.strip())
        plane2 = find_plane(p2.strip())

        if plane1 and plane2:

            return jsonify({
                "answer":
                f"{plane1} vs {plane2}\n\n"
                f"{plane1} Nation: {planes[plane1]['nation']}\n"
                f"{plane2} Nation: {planes[plane2]['nation']}\n\n"
                f"{plane1} Speed: {planes[plane1]['speed']}\n"
                f"{plane2} Speed: {planes[plane2]['speed']}\n\n"
                f"{plane1} BR: {planes[plane1]['br']}\n"
                f"{plane2} BR: {planes[plane2]['br']}"
            })

    # --- nation search ---
    for plane, data in planes.items():

        if data["nation"].lower() in question:
            results = [p for p in planes if planes[p]["nation"].lower() in question]

            return jsonify({
                "answer": f"Planes from {data['nation']}:\n\n" + "\n".join(results[:10])
            })

    # --- fastest plane search ---
    if "fastest" in question:

        fastest = max(planes, key=lambda x: planes[x]["speed_value"])

        return jsonify({
            "answer": f"Fastest plane: {fastest}\nSpeed: {planes[fastest]['speed']}"
        })

    # --- normal plane lookup ---
    plane = find_plane(question)

    if plane:

        data = planes[plane]

        return jsonify({
            "answer":
            f"{plane}\n\n"
            f"Nation: {data['nation']}\n"
            f"BR: {data['br']}\n"
            f"Speed: {data['speed']}\n"
            f"Weapons: {data['weapons']}\n\n"
            f"Tip: {data['tip']}",
            "image": data["image"]
        })

    return jsonify({"answer": "Plane not found."})


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
