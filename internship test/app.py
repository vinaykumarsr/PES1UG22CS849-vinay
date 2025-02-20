from flask import Flask, redirect, url_for
import os
import subprocess
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    full_name = "VINAY KUMAR S R"
    username = "vinaykumarsr"
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    top_output = subprocess.getoutput("top -bn1")

    html_content = f"""
    <h2>Name: {full_name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <h4>TOP output:</h4>
    <pre>{top_output}</pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
