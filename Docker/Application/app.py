from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stylish Text Echo</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
    <style>
        body {
            background: #f5f7fa;
            font-family: 'Roboto', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .container {
            background: #fff;
            padding: 2rem 3rem;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            text-align: center;
        }
        input[type="text"] {
            width: 70%;
            padding: 0.7rem;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        button {
            background: #007bff;
            color: #fff;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background: #0056b3;
        }
        .output {
            margin-top: 1.5rem;
            font-size: 1.2rem;
            color: #333;
            word-break: break-word;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Enter Text to Display</h2>
        <form method="POST">
            <input type="text" name="user_text" placeholder="Type something..." value="{{ user_text|default('') }}" autocomplete="off" required>
            <br>
            <button type="submit">Show Text</button>
        </form>
        {% if user_text %}
        <div class="output">
            <strong>You entered:</strong> {{ user_text }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    user_text = ""
    if request.method == 'POST':
        user_text = request.form.get('user_text', '')
    return render_template_string(HTML, user_text=user_text)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')