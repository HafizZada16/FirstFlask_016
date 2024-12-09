from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("text_field")
        response = f"Anda mengirimkan: {user_input}"
        return jsonify({"message": response})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
