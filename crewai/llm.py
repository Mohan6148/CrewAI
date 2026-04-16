import os

import google.generativeai as genai


class LLM:
    def __init__(self, provider=None, model=None, api_key=None, temperature=0.7, verbose=False, **kwargs):
        self.provider = provider or "gemini"
        self.model = model or os.getenv("GEMINI_MODEL", "gemini/gemini-1.5-flash")
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        self.temperature = temperature
        self.verbose = verbose

        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY or GEMINI_API_KEY is required")

        genai.configure(api_key=self.api_key)
        self._model_name = self.model.replace("gemini/", "")
        self._model = genai.GenerativeModel(self._model_name)

    def generate(self, prompt):
        response = self._model.generate_content(
            prompt,
            generation_config={"temperature": self.temperature},
        )
        text = getattr(response, "text", None)
        if text:
            return text.strip()
        return str(response)

    def invoke(self, prompt):
        return self.generate(prompt)
