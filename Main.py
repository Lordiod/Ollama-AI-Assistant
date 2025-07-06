#!/usr/bin/env python3
"""
Ollama AI Assistant - Main Entry Point

A modern desktop AI chat application built with Python and CustomTkinter
that interfaces with Ollama's local AI models.

Author: Your Name
License: MIT
Version: 1.0.0
"""

from chatbot_app import ChatBotApp


def main() -> None:
    """Main entry point for the Ollama AI Assistant application."""
    try:
        app = ChatBotApp()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
