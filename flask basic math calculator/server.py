from flask import Flask, request, render_template
from Maths.mathematics import summation, subtraction, multiplication

app = Flask(__name__)

# Root endpoint: render index.html
@app.route("/")
def render_index_page():
    return render_template("index.html")

# /sum endpoint
@app.route("/sum")
def sum_numbers():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = summation(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

# /sub endpoint
@app.route("/sub")
def sub_numbers():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = subtraction(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

# /mul endpoint
@app.route("/mul")
def mul_numbers():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    result = multiplication(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
