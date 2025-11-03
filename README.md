# Flask-Basic-Calculator

🧮 Flask-Basic-Calculator

A simple yet powerful Flask web app that performs basic math operations — Addition, Subtraction, and Multiplication — using a custom Python package named Maths.
Built to demonstrate modular Flask structure, templates, and package imports. ⚙️✨

🚀 Features

➕ Add two numbers

➖ Subtract numbers

✖️ Multiply numbers

🌐 Clean web interface

🧩 Custom Python package (Maths) for all operations

📁 Project Structure
Flask-Basic-Calculator/
│
├── Maths/
│   ├── __init__.py
│   └── mathematics.py
│
├── templates/
│   └── index.html
│
├── server.py
└── README.md

⚙️ How to Run
1️⃣ Clone this repository
git clone https://github.com/YOURUSERNAME/Flask-Basic-Calculator.git
cd Flask-Basic-Calculator

2️⃣ Install Flask
pip install flask

3️⃣ Run the app
python3 server.py


The app will start at:
👉 http://127.0.0.1:8080
 (or another port if specified)

💡 Usage

Open your browser and go to http://localhost:8080

Enter two numbers

Choose an operation (Add, Subtract, Multiply)

🎉 See your result instantly!

🧠 Maths Package Overview
def summation(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

🎯 Learning Outcomes

Flask structure and routing

Importing and using custom Python packages

HTML templates with dynamic data

Deploying Flask apps locally
