# ConvoEase - Plugin Architecture Demo

*Note: This is a simplified structural representation demonstrating the plugin-based text and audio moderation architecture, focusing on the abstract base class and registration pattern.*

```python
import base64
from typing import Dict, Any

# --- Plugin Interface ---

class ProcessingPlugin:
    """Base interface for all conversational processing plugins."""
    name = "base"

    def get_input_schema(self) -> Dict[str, str]:
        """Defines expected input payload dictionary."""
        return {}

    def get_output_schema(self) -> Dict[str, str]:
        """Defines returned output dictionary schema."""
        return {}

    def process(self, input_data: Dict[str, Any], context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Executes plugin moderation logic."""
        raise NotImplementedError()


# --- Implementations ---

class TextModerationPlugin(ProcessingPlugin):
    name = "text_moderation"

    def __init__(self, model_config: Dict[str, str]):
        self.config = model_config
        # e.g., self.client = OpenAI(base_url=...)

    def process(self, input_data: Dict[str, Any], context=None) -> Dict[str, Any]:
        message = input_data.get("message", "")
        rules = input_data.get("rules", "")

        # (Simulated API call for demonstration)
        print(f"[API] Moderating text against rules: {rules}")
        if "bad_word" in message:
            return {"allowed": False, "reason": "Violated content guidelines"}
        
        return {"allowed": True, "reason": ""}


class AudioModerationPlugin(ProcessingPlugin):
    """
    Demonstrates multi-modal plugin chaining:
    1. Transcribe (speech-to-text)
    2. Summarize (LLM)
    3. Moderate Summary (TextModerationPlugin)
    """
    name = "audio_moderation"

    def __init__(self, text_moderator_instance: TextModerationPlugin):
        # We reuse the Text Moderator for the final step
        self.text_moderator = text_moderator_instance

    def process(self, input_data: Dict[str, Any], context=None) -> Dict[str, Any]:
        audio_b64 = input_data.get("audio_data", "")
        rules = input_data.get("rules", "")

        # 1. Transcribe (Simulated Google Speech Recognition)
        transcript = self._transcribe_audio(audio_b64)
        
        # 2. Summarize (Simulated AI Summarization)
        summary = f"Summary of audio: {transcript}"

        # 3. Chain into Text Moderation
        moderation_result = self.text_moderator.process({"message": summary, "rules": rules})
        
        # Compose final result
        return {
            "allowed": moderation_result["allowed"],
            "reason": moderation_result["reason"],
            "summary": summary,
            "transcript": transcript
        }

    def _transcribe_audio(self, b64_audio: str) -> str:
        # Stub for speech recognition
        return "This is a transcribed audio message."


# --- Engine Registry ---

class ProcessingEngine:
    """Central dynamic registry for routing payloads to modalities."""
    def __init__(self):
        self._plugins: Dict[str, ProcessingPlugin] = {}

    def register(self, plugin: ProcessingPlugin):
        self._plugins[plugin.name] = plugin

    def process(self, plugin_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        plugin = self._plugins.get(plugin_name)
        if not plugin:
            raise KeyError(f"Plugin {plugin_name} not registered.")
        
        return plugin.process(payload)


# --- Example Usage ---

if __name__ == "__main__":
    engine = ProcessingEngine()
    text_mod = TextModerationPlugin({"mode": "api"})
    audio_mod = AudioModerationPlugin(text_mod)

    engine.register(text_mod)
    engine.register(audio_mod)

    print("--- Text Moderation ---")
    res = engine.process("text_moderation", {"message": "Hello team", "rules": "No bad language"})
    print("Result:", res)

    print("\n--- Audio Moderation ---")
    fake_audio = base64.b64encode(b"fake_audio_stream").decode("utf-8")
    res = engine.process("audio_moderation", {"audio_data": fake_audio, "rules": "No bad language"})
    print("Result:", res)
```
