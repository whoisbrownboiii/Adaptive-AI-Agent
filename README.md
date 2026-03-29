# 🤖 Adaptive AI Personal Assistant Agent

## 📌 Description

An adaptive AI Personal Assistant agent built using the Google Gemini API. The system follows the ReAct (Reason → Act → Observe) pattern and is designed using SOLID principles and software design patterns to ensure modularity, extensibility, and maintainability.

---

## 🏗️ Architecture

The project is structured into the following components:

* **Agent** – Controls the reasoning loop and interacts with the Gemini API
* **MemoryManager** – Stores conversation history
* **ToolRegistry** – Dynamically manages and executes tools (Factory Pattern)
* **BaseTool** – Defines a standard interface for all tools (Strategy Pattern)

---

## 🎯 Design Patterns Used

* Strategy Pattern (Tool abstraction)
* Factory / Registry Pattern (Tool management)
* ReAct Pattern (Reason → Act → Observe loop)
* SOLID Principles (clean architecture)

---

## 🧰 Tools Implemented

* 🔢 Calculator Tool
* ⏰ Time Tool
* 🌍 Translation Tool (Custom)
* 📂 File Reader Tool (Custom)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Adaptive-AI-Agent.git
cd Adaptive-AI-Agent
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup API Key 🔑

This project requires a Google Gemini API key.

#### macOS / Linux:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

#### Windows:

```bash
set GEMINI_API_KEY="your_api_key_here"
```

⚠️ **IMPORTANT:**
Do NOT put your API key inside the code. Always use environment variables.

---

## ▶️ Running the Application

```bash
python3 main.py
```

---

## 💬 Example Usage

```
You: What is 25 * 6?
Agent: 150

You: What time is it?
Agent: 2026-03-29 12:45:00

You: Read file notes.txt
Agent: (file content displayed)
```

---

## 📁 Project Structure

```
AI ChatBot/
│
├── agent.py
├── memory_manager.py
├── tool_registry.py
├── base_tool.py
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── tools/
    ├── calculator_tool.py
    ├── time_tool.py
    ├── translation_tool.py
    └── file_reader_tool.py
```

---

## ⚠️ Error Handling

The system handles:

* API errors (quota, invalid key, network issues)
* Invalid tool inputs
* Unknown tool requests
* File reading errors

---

## 🚧 Limitations

* Some Gemini models may require billing to access
* Translation tool is a basic implementation
* Requires internet connection

---

## 🚀 Future Improvements

* Add real APIs (weather, translation, news)
* Implement GUI interface
* Add persistent memory (database)
* Add logging system (Observer Pattern)

---

## 🔐 Security Notes

* API keys are NOT stored in the repository
* `.gitignore` prevents sensitive files from being uploaded
* Always use environment variables for credentials

---

## 👨‍💻 Author

* Name: [Thokozile Mabo]
* Course: Applied Systems Software
* Assignment: AI Agent Architecture

---

## 📄 License

This project is for academic purposes only.
