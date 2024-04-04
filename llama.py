from llama_cpp import Llama
from file_manager import FileManager

import os

class LLM():
	def __init__(self) -> None:
		FileManager.create_dir(dir_name='llm_model')
		cwd = os.getcwd()
		model_path  = f"{cwd}/llm_model/lama-2-7b-chat.Q2_K.gguf"

		self.download_model() if not os.path.isfile(model_path) else None
		self.model = Llama(model_path=model_path, n_ctx=2048)
		self.max_tokens = 2500

	def download_model(self):
		os.system("curl -L --output llm_model/lama-2-7b-chat.Q2_K.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf?download=true")

	def generate_prompt(self,user_message,system_message=""):
		prompt = f"""<s>
		[INST] 
		<<SYS>>
		{system_message}
		<</SYS>>
		{user_message}
		[/INST]"""
		return prompt

	def execute_prompt(self,prompt=""):
		output = self.model(prompt, max_tokens=self.max_tokens, echo=True)
		return output