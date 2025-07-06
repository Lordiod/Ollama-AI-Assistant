import customtkinter as ctk
from models.chat_message import ChatMessage
from utils.text_utils import calculate_text_height
from typing import List, Callable

class ChatDisplayComponent:
    """Chat display component for showing messages"""
    
    def __init__(self, parent: ctk.CTk):
        self.parent = parent
        self.chat_display = None
        self.chat_history: List[ChatMessage] = []
        self.create_chat_display()
    
    def create_chat_display(self):
        # Main content frame
        main_frame = ctk.CTkFrame(self.parent)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        
        # Chat display area with scrollable frame
        self.chat_display = ctk.CTkScrollableFrame(main_frame, label_text="Conversation")
        self.chat_display.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.chat_display.grid_columnconfigure(0, weight=1)
        
        # Welcome message
        self.add_message("assistant", "Welcome! I'm your AI assistant powered by Ollama. How can I help you today?")
    
    def add_message(self, role: str, content: str):
        """Add a message to the chat display"""
        # Create message object
        message = ChatMessage(role, content)
        
        # Create message frame
        message_frame = ctk.CTkFrame(self.chat_display)
        message_frame.grid(row=len(self.chat_history), column=0, sticky="ew", padx=5, pady=5)
        message_frame.grid_columnconfigure(1, weight=1)
        
        # Role indicator
        role_color = "#2196F3" if role == "user" else "#4CAF50"
        role_text = "You" if role == "user" else "AI Assistant"
        
        role_label = ctk.CTkLabel(message_frame, text=role_text, 
                                 font=ctk.CTkFont(size=12, weight="bold"),
                                 text_color=role_color)
        role_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        
        # Timestamp
        time_label = ctk.CTkLabel(message_frame, text=message.timestamp, 
                                 font=ctk.CTkFont(size=10),
                                 text_color="gray")
        time_label.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="e")
        
        # Message content with compact auto-sizing
        content_height = calculate_text_height(content)
        
        content_textbox = ctk.CTkTextbox(message_frame, height=content_height, wrap="word")
        content_textbox.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        content_textbox.insert("1.0", content)
        content_textbox.configure(state="disabled")
        
        # Store in history
        self.chat_history.append(message)
        
        # Auto-scroll to bottom
        self.parent.after(100, self.scroll_to_bottom)
    
    def scroll_to_bottom(self):
        """Scroll chat display to bottom"""
        self.chat_display._parent_canvas.yview_moveto(1.0)
    
    def clear_chat(self):
        """Clear chat history and display"""
        self.chat_history = []
        for widget in self.chat_display.winfo_children():
            widget.destroy()
        self.add_message("assistant", "Chat cleared. How can I help you?")
