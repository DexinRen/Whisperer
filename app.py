from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

history = []
notes = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    message = request.form["message"]
    print(message)
    history.append(("User", message))
    # TODO: Send message to responder and get response
    # response = ...
    # history.append(("Responder", response))
    return jsonify({"success": True})

@app.route("/get_history")
def get_history():
    return jsonify(history)

@app.route("/create_note", methods=["POST"])
def create_note():
    note_title = request.form["note_title"]
    note_text = request.form["note_text"]
    notes[note_title] = note_text
    return jsonify({"success": True})

@app.route("/get_notes")
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)