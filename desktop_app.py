import webview
import threading
import subprocess
import time
import logging
import os

# ✅ Suppress webview logs
logging.getLogger("pywebview").setLevel(logging.CRITICAL)

# ✅ Run Flask app in the background
def run_flask():
    subprocess.Popen(["python", "app.py"], shell=True)

# 🔁 Launch Flask app
threading.Thread(target=run_flask, daemon=True).start()

# ⏱ Wait for the Flask app to start
time.sleep(2)

# ✅ Launch desktop app (just open window to Flask server)
try:
    webview.create_window("Career Guidance System", "http://127.0.0.1:5000")
    webview.start(debug=False)
except PermissionError as e:
    print(f"⚠️ Skipped browser cleanup due to permission error: {e}")
    print("✅ Flask app is still running. Visit http://127.0.0.1:5000 in your browser.")
