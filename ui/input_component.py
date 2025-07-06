import customtkinter as ctk
from typing import Callable

class InputComponent:
    """Input component for user messages"""
    
    def __init__(self, parent: ctk.CTk, on_send: Callable[[str], None], on_clear: Callable[[], None]):
        self.parent = parent
        self.on_send = on_send
        self.on_clear = on_clear
        self.prompt_entry = None
        self.generate_button = None
        self.clear_button = None
        self.create_input_area()
    
    def create_input_area(self):
        # Footer frame for input
        footer_frame = ctk.CTkFrame(self.parent, height=120)
        footer_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        # Input frame
        input_frame = ctk.CTkFrame(footer_frame)
        input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        input_frame.grid_columnconfigure(0, weight=1)
        
        # Prompt entry with better styling
        self.prompt_entry = ctk.CTkTextbox(input_frame, height=60, wrap="word")
        self.prompt_entry.grid(row=0, column=0, sticky="ew", padx=(10, 5), pady=10)
        self.prompt_entry.bind("<KeyPress>", self.on_key_press)
        
        # Button frame
        button_frame = ctk.CTkFrame(input_frame, fg_color="transparent")
        button_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="ns")
        
        # Generate button with better styling
        self.generate_button = ctk.CTkButton(button_frame, text="Send", 
                                           command=self.handle_send,
                                           width=80, height=60,
                                           font=ctk.CTkFont(size=14, weight="bold"))
        self.generate_button.pack(pady=(0, 5))
        
        # Clear button
        self.clear_button = ctk.CTkButton(button_frame, text="Clear", 
                                         command=self.on_clear,
                                         width=80, height=25,
                                         fg_color="gray",
                                         hover_color="dark gray")
        self.clear_button.pack()
    
    def on_key_press(self, event):
        """Handle key press events"""
        if event.keysym == "Return":
            if event.state & 0x1:  # Shift pressed
                return
            self.handle_send()
            return "break"
    
    def handle_send(self):
        """Handle send button click"""
        prompt = self.prompt_entry.get("1.0", "end-1c").strip()
        if prompt:
            self.on_send(prompt)
            self.clear_input()
    
    def clear_input(self):
        """Clear the input field"""
        self.prompt_entry.delete("1.0", ctk.END)
    
    def set_button_state(self, enabled: bool, text: str = "Send"):
        """Set the state of the send button"""
        state = "normal" if enabled else "disabled"
        self.generate_button.configure(state=state, text=text)
