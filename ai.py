import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0
DEFAULT_ANTHROPIC_MODEL_NAME = "claude-3-5-sonnet-20240620"


class AnthropicService:
    def __init__(self, model_name: str = None, anthropic: Anthropic = None):
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise ValueError("No valid API key found for Anthropic.")
        self.client = anthropic or Anthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"])
        self.model_name = model_name or DEFAULT_ANTHROPIC_MODEL_NAME

    def generate_response(self, prompt: str, max_tokens: int = MAX_TOKENS, temperature: float = DEFAULT_TEMPERATURE) -> str:
        msg = self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return msg.content[0].text
