# 🚀 Jupyter Notebook Automation

![Jupyter](https://img.shields.io/badge/Jupyter-Automation-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📌 Overview  
A web interface to **start/stop** a Jupyter Notebook server, execute notebooks, and schedule periodic runs using Flask and Jupyter.

## ✨ Features  
✅ Start & stop Jupyter Notebook from the web interface  
✅ Execute a specific Jupyter Notebook on demand  
✅ Set a timer for scheduled executions  
✅ Auto-refresh embedded iframe for real-time updates  

## ⚡ Prerequisites  
Ensure you have the following installed:  
- **Python 3.x**  
- **Jupyter Notebook**  
- **Flask**  

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/JayanthSL/jupyter_notebook_automation.git
cd jupyter_notebook_automation
```

### 2️⃣ Install Dependencies

### 3️⃣ Run the Flask Application
```sh
python main.py
```
### 4️⃣ Access the Web Interface
```sh

Open your browser and go to:
👉 http://localhost:5700/
```
### 🚀 Usage
```sh

▶️ Start Jupyter Notebook
Click the "Start Jupyter" button to launch the Jupyter Notebook server.

⏹️ Stop Jupyter Notebook
Click "Stop Jupyter" to shut down the Jupyter server.

🏃 Execute Notebook
Click "Run Notebook" to execute the notebook (Untitled.ipynb).

⏳ Set Execution Timer
Enter interval (in minutes).
Click "Set Timer" to schedule automatic executions.
🔄 Auto-Refresh
The notebook automatically refreshes every 30 seconds.
```
### 🔗 API Endpoints
```sh

Method	Endpoint	Description
GET	/start	Starts the Jupyter Notebook server
GET	/stop	Stops the Jupyter Notebook server
POST	/run-notebook	Executes the notebook
POST	/set-timer	Sets execution timer
🔒 Security Considerations
⚠️ Jupyter Notebook starts without authentication (--NotebookApp.token=).
If deploying in production, add authentication & access control to secure the setup.
```
### 📜 License
```sh

This project is licensed under the MIT License.
📄 See the LICENSE file for details.
```
