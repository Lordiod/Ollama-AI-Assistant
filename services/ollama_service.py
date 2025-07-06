import requests
import threading
from typing import Callable, Optional

class OllamaService:
    """Service for handling Ollama API calls"""
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.2:3b"):
        self.base_url = base_url
        self.model = model
        self.timeout = 30
    
    def generate_response(self, prompt: str, callback: Callable[[str, bool], None]):
        """Generate response from Ollama API in a separate thread"""
        threading.Thread(target=self._api_call, args=(prompt, callback), daemon=True).start()
    
    def _api_call(self, prompt: str, callback: Callable[[str, bool], None]):
        """Make API call to Ollama"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(f"{self.base_url}/api/generate", 
                                   json=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            result = data.get("response", "No response received.")
            
            # Call callback with success
            callback(result, True)
            
        except requests.exceptions.ConnectionError:
            error_msg = "❌ Connection Error: Unable to connect to Ollama server.\nPlease ensure Ollama is running on localhost:11434"
            callback(error_msg, False)
        except requests.exceptions.Timeout:
            error_msg = "⏱️ Timeout Error: The request took too long to complete."
            callback(error_msg, False)
        except Exception as e:
            error_msg = f"❌ Unexpected Error: {str(e)}"
            callback(error_msg, False)
