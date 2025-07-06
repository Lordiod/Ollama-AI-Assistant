# 🤖 Ollama AI Assistant

A modern, desktop AI chat application built with Python and CustomTkinter that interfaces with Ollama's local AI models.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)

## ✨ Features

- 🎨 **Modern Dark UI** - Beautiful interface built with CustomTkinter
- 🚀 **Local AI Integration** - Connect to Ollama's local AI models
- ⚡ **Real-time Chat** - Instant responses with threading support
- 🎯 **Smart Text Handling** - Auto-sizing text boxes and smooth scrolling
- ⌨️ **Keyboard Shortcuts** - Enter to send, Shift+Enter for new lines
- 🔄 **Error Handling** - Robust connection and timeout error management
- 📱 **Responsive Design** - Resizable interface with minimum size constraints
- 🧹 **Chat Management** - Clear chat history with one click

## 🎬 Demo

The application provides a clean, intuitive interface for chatting with AI models:

- **Header**: Shows connection status and app title
- **Chat Area**: Scrollable conversation history with timestamps
- **Input Area**: Text input with Send and Clear buttons

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
   - Download from: [ollama.ai](https://ollama.ai/)
   - Install a model: `ollama pull llama3.2:3b`
   - Start Ollama service: `ollama serve`

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/lordiod/ollama-ai-assistant.git
cd ollama-ai-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

## 📁 Project Structure

```
├── main.py                          # 🚪 Entry point
├── chatbot_app.py                   # 🏗️ Main application class
├── requirements.txt                 # 📦 Dependencies
├── LICENSE                          # 📄 MIT License
├── .gitignore                       # 🙈 Git ignore rules
├── models/                          # 📊 Data models
│   ├── __init__.py
│   └── chat_message.py             # 💬 Chat message model
├── services/                        # 🛠️ Business logic
│   ├── __init__.py
│   └── ollama_service.py           # 🤖 Ollama API service
├── ui/                             # 🎨 User interface
│   ├── __init__.py
│   ├── header_component.py         # 📋 Header with status
│   ├── chat_display_component.py   # 💭 Chat display
│   └── input_component.py          # ⌨️ Input handling
└── utils/                          # 🔧 Utilities
    ├── __init__.py
    └── text_utils.py               # 📝 Text processing
```

## 🔧 Configuration

### Ollama Settings
The application uses these default settings (configurable in `services/ollama_service.py`):

- **Server URL**: `http://localhost:11434`
- **Default Model**: `llama3.2:3b`
- **Timeout**: 30 seconds

### UI Customization
Modify appearance in `chatbot_app.py`:

```python
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
```

## 🛠️ Architecture

This project follows a **modular architecture** with clear separation of concerns:

### 📊 Models Layer
- **ChatMessage**: Handles message data with timestamps and serialization

### 🛠️ Services Layer  
- **OllamaService**: Manages API communication, threading, and error handling

### 🎨 UI Layer
- **HeaderComponent**: Status display and app branding
- **ChatDisplayComponent**: Message rendering and chat history
- **InputComponent**: User input and button interactions

### 🔧 Utils Layer
- **text_utils**: Text processing and height calculations

## 🚦 Error Handling

The application handles various error scenarios:

- **Connection Errors**: When Ollama service is unavailable
- **Timeout Errors**: When requests take too long
- **Model Errors**: When the specified model isn't available
- **Network Errors**: General connectivity issues

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.