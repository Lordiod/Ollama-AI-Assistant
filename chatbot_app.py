"""
Ollama AI Assistant - Main Application

This module contains the main ChatBotApp class that orchestrates all UI components
and services to create a complete AI chat application.

Classes:
    ChatBotApp: Main application class that manages UI and services
"""
from typing import Optional
import customtkinter as ctk
from ui.header_component import HeaderComponent
from ui.chat_display_component import ChatDisplayComponent
from ui.input_component import InputComponent
from services.ollama_service import OllamaService


class ChatBotApp:
    """
    Main ChatBot Application class.
    
    This class manages the entire application lifecycle, coordinates UI components,
    and handles communication with the Ollama service.
    
    Attributes:
        app: The main CustomTkinter window
        header: Header component with title and status
        chat_display: Chat display component for messages
        input_component: Input component for user interaction
        ollama_service: Service for Ollama API communication
    """
    
    def __init__(self) -> None:
        """Initialize the ChatBot application."""
        self.app: Optional[ctk.CTk] = None
        self.header: Optional[HeaderComponent] = None
        self.chat_display: Optional[ChatDisplayComponent] = None
        self.input_component: Optional[InputComponent] = None
        self.ollama_service: Optional[OllamaService] = None
        
        self.setup_ui()
        self.setup_services()
        
    def setup_ui(self) -> None:
        """Initialize the user interface"""
        # Initialize app
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Ollama AI Assistant")
        self.app.geometry("900x700")
        self.app.minsize(600, 500)
        
        # Configure grid weights
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=1)
        
        # Create components
        self.header = HeaderComponent(self.app)
        self.chat_display = ChatDisplayComponent(self.app)
        self.input_component = InputComponent(
            self.app, 
            on_send=self.generate_text,
            on_clear=self.clear_chat
        )
    
    def setup_services(self) -> None:
        """Initialize services for the application."""
        self.ollama_service = OllamaService()
    
    def generate_text(self, prompt: str) -> None:
        """
        Generate text response from user prompt.
        
        Args:
            prompt: The user's input message to send to the AI
        """
        if not prompt:
            if self.header:
                self.header.update_status("Please enter a message", "orange")
            return

        # Add user message to chat
        if self.chat_display:
            self.chat_display.add_message("user", prompt)
        
        # Disable button and show loading
        if self.input_component:
            self.input_component.set_button_state(False, "Sending...")
        if self.header:
            self.header.update_status("Generating response...", "orange")
        
        # Make API call
        if self.ollama_service:
            self.ollama_service.generate_response(prompt, self.handle_response)
    
    def handle_response(self, result: str, success: bool) -> None:
        """
        Handle response from the Ollama API.
        
        Args:
            result: The response text from the API
            success: Whether the API call was successful
        """
        # Schedule UI update in main thread
        if self.app:
            self.app.after(0, lambda: self._update_ui_with_response(result, success))
    
    def _update_ui_with_response(self, result: str, success: bool) -> None:
        """
        Update UI with response (called in main thread).
        
        Args:
            result: The response text to display
            success: Whether the operation was successful
        """
        # Add AI response to chat
        if self.chat_display:
            self.chat_display.add_message("assistant", result)
        
        # Re-enable button and update status
        if self.input_component:
            self.input_component.set_button_state(True, "Send")
        if self.header:
            if success:
                self.header.update_status("Ready", "green")
            else:
                self.header.update_status("Error occurred", "red")
    
    def clear_chat(self) -> None:
        """Clear the chat history and display."""
        if self.chat_display:
            self.chat_display.clear_chat()
            
    def run(self) -> None:
        """Run the application main loop."""
        if self.app:
            self.app.mainloop()
