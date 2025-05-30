from flask import Flask, render_template, jsonify, request
import subprocess
import os
import signal
import schedule
import time
import threading
import json
import sys
import platform

app = Flask(__name__)

jupyter_process = None
JUPYTER_PORT = 8888
NOTEBOOK_PATH = os.path.join(os.getcwd(), "Untitled.ipynb")
execution_interval = None

def ensure_notebook_exists():
    try:
        print("Checking if notebook exists...")
        if not os.path.exists(NOTEBOOK_PATH):
            empty_notebook = {
                "cells": [],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 4
            }
            with open(NOTEBOOK_PATH, "w") as f:
                json.dump(empty_notebook, f)
            print(f"Created new notebook: {NOTEBOOK_PATH}")
        else:
            print("Notebook already exists.")
    except Exception as e:
        print(f"Error creating notebook: {e}")

def execute_notebook():
    ensure_notebook_exists()
    subprocess.run([
        sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "--allow-errors", NOTEBOOK_PATH
    ], check=True)
    print(f"Executed and updated {NOTEBOOK_PATH}")
    save_notebook()

def save_notebook():
    with open(NOTEBOOK_PATH, "r") as f:
        notebook_data = json.load(f)
    with open(NOTEBOOK_PATH, "w") as f:
        json.dump(notebook_data, f)
    print(f"Notebook {NOTEBOOK_PATH} saved.")

def run_scheduler():
    while True:
        schedule.run_pending()
        save_notebook()  
        time.sleep(1)

@app.route('/start', methods=['GET'])
def start_jupyter():
    global jupyter_process
    if jupyter_process is None:
        jupyter_process = subprocess.Popen([
            sys.executable, "-m", "jupyter", "notebook",
            "--NotebookApp.token=",
            "--NotebookApp.password=",
            "--NotebookApp.allow_origin=*",
            "--NotebookApp.disable_check_xsrf=True",
            "--NotebookApp.ip=0.0.0.0",
            "--NotebookApp.open_browser=False",
            "--NotebookApp.tornado_settings={'headers': {'Content-Security-Policy': \"frame-ancestors 'self' http://127.0.0.1:5700 http://localhost:5700;\"}}",
            "--port=8888"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return jsonify({"message": "Jupyter Notebook started"}), 200
    return jsonify({"message": "Jupyter Notebook is already running"}), 400

@app.route('/stop', methods=['GET'])
def stop_jupyter():
    global jupyter_process
    if jupyter_process:
        if platform.system() == "Windows":
            jupyter_process.terminate()  # Windows-friendly termination
        else:
            os.kill(jupyter_process.pid, signal.SIGTERM)  # Unix-like termination
        jupyter_process = None
        return jsonify({"message": "Jupyter Notebook stopped"}), 200
    return jsonify({"message": "Jupyter Notebook is not running"}), 400

@app.route('/set-timer', methods=['POST'])
def set_timer():
    global execution_interval
    data = request.json
    try:
        interval = int(data.get("interval"))
        if interval <= 0:
            return jsonify({"error": "Interval must be greater than zero"}), 400

        execution_interval = interval
        schedule.clear()
        schedule.every(execution_interval).minutes.do(execute_notebook)
        print(f"Scheduled execution every {execution_interval} minutes")
        return jsonify({"message": f"Notebook will run every {execution_interval} minutes"}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid interval"}), 400

@app.route('/run-notebook', methods=['POST'])
def run_notebook():
    try:
        execute_notebook()
        return jsonify({"message": "Notebook executed and updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

if __name__ == '__main__':
    ensure_notebook_exists()
    app.run(host="0.0.0.0", port=5700, debug=True)
