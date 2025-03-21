Jupyter Notebook Automation

Overview

This project provides a simple web interface to control a Jupyter Notebook server, execute notebooks automatically, and schedule periodic executions using Flask and Jupyter.

Features

Start and stop the Jupyter Notebook server from the web interface.

Execute a specific Jupyter Notebook on demand.

Set a timer to schedule automatic executions at regular intervals.

Auto-refresh the notebook display in the embedded iframe.

Prerequisites

Ensure you have the following installed:

Python 3.x

Jupyter Notebook

Flask

Required dependencies (see installation steps below)

Installation

Clone the Repository:

git clone https://github.com/JayanthSL/jupyter_notebook_automation.git
cd jupyter_notebook_automation

Install Dependencies:

Run the Flask Application:

python main.py

Access the Web Interface:
Open your browser and go to:

http://localhost:5700/

Usage

Start Jupyter Notebook

Click the "Start Jupyter" button to launch the Jupyter Notebook server.

Stop Jupyter Notebook

Click "Stop Jupyter" to shut down the Jupyter server.

Execute Notebook

Click "Run Notebook" to execute the specified notebook (Untitled.ipynb).

Set Execution Timer

Enter the interval (in minutes) in the input field.

Click "Set Timer" to schedule automatic executions at the specified interval.

Auto-Refresh

The notebook iframe automatically refreshes every 30 seconds to reflect updates.

API Endpoints

The Flask server exposes the following endpoints:

GET /start – Starts the Jupyter Notebook server.

GET /stop – Stops the Jupyter Notebook server.

POST /run-notebook – Executes the notebook.

POST /set-timer – Sets the execution timer for automatic notebook runs.

Security Considerations

The notebook server is started without authentication (--NotebookApp.token=). Ensure this is safe for your use case.

Consider adding authentication and access control if deploying in a production environment.

License

This project is licensed under the MIT License. It allows for commercial use, modification, and distribution. See the LICENSE file for details.