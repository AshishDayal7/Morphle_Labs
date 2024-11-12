from flask import Flask
import os
from datetime import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Display Name
    name = "Ashish Ranjan Dayal"
    
    # Get the System Username
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    # Get Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the 'top' command output
    top_output = subprocess.getoutput('top -b -n 1')

    # Create the response HTML
    html = f"""
    <html>
    <body>
        <h1>/htop Endpoint</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
