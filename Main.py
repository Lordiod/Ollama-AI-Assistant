import customtkinter as ctk
import requests

def generate_text():
    prompt = prompt_entry.get()
    if not prompt:
        response_textbox.delete("1.0", ctk.END)
        response_textbox.insert(ctk.END, "Please enter a prompt.")
        return

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        data = response.json()
        result = data.get("response", "No response.")
    except Exception as e:
        result = f"Error: {e}"

    response_textbox.delete("1.0", ctk.END)
    response_textbox.insert(ctk.END, result)

# Initialize app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Ollama Llama3.2 Local AI")
app.geometry("600x400")

# Prompt Entry
prompt_entry = ctk.CTkEntry(app, placeholder_text="Enter your prompt here...")
prompt_entry.pack(padx=20, pady=20, fill="x")

# Generate Button
generate_button = ctk.CTkButton(app, text="Generate", command=generate_text)
generate_button.pack(pady=10)

# Response Textbox
response_textbox = ctk.CTkTextbox(app, wrap="word", height=200)
response_textbox.pack(padx=20, pady=20, fill="both", expand=True)

app.mainloop()
