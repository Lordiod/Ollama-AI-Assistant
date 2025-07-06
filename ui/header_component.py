import customtkinter as ctk
from typing import Callable

class HeaderComponent:
    """Header component with title and status"""
    
    def __init__(self, parent: ctk.CTk):
        self.parent = parent
        self.status_label = None
        self.create_header()
    
    def create_header(self):
        # Header frame
        header_frame = ctk.CTkFrame(self.parent, height=60)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Title and status
        title_label = ctk.CTkLabel(header_frame, text="🤖 Ollama AI Assistant", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")
        
        self.status_label = ctk.CTkLabel(header_frame, text="● Ready", 
                                        font=ctk.CTkFont(size=12), 
                                        text_color="green")
        self.status_label.grid(row=0, column=1, padx=20, pady=15, sticky="e")
    
    def update_status(self, status: str, color: str = "green"):
        """Update the status label"""
        self.status_label.configure(text=f"● {status}", text_color=color)
