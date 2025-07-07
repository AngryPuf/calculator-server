from flask import Flask, request
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes

@app.route("/")
def home():
    return "Server is running!"

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "")
    try:
        # Allow only math functions and safe built-ins
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names.update({"abs": abs, "round": round})
        allowed_names.update({"log10": math.log10,"log": lambda x, base=math.e: math.log(x, base), "factorial": math.factorial
        })
        
        # Evaluate safely
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return str(result)
    except Exception:
        return "Syntax Error", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)

