from llama import LLM
import json

class Main():
	def start(self):
		llm = LLM()
				  
		system_message = "You are a text extractor"
		user_message = "Extract the job requirements for the following job offer and write them in topics and do not include any other detail: ${job_scrap}".format(
			job_scrap = open('job.txt','rt').read()
		)
		prompt = llm.generate_prompt(system_message=system_message,user_message=user_message)
		output = llm.execute_prompt(prompt=prompt)

		output['choices'][0]['text'] = output['choices'][0]['text'].split('[/INST]')[-1]
		with open('result.json','w') as file:
			json.dump(output, fp=file)

		job = open('result.json','r').read()
		print (json.loads(job)['choices'][0]['text'])

if __name__ == "__main__":
	main = Main()
	main.start()