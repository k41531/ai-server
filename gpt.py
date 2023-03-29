import openai

class Assistant:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "Your name is Alice. Act as a smart, enigmatic, cynical woman. Keep your response short and simple."}
        ]

    def get_content(self,response):
        return response["choices"][0]["message"]["content"]
    
    def user_message(self, content):
        self.messages.append(
            {"role": "user", "content": content}
        )

    def assistant_message(self, content):
        self.messages.append(
            {"role": "assistant", "content": content}
        )

    def clear_history(self):
        self.messages = []        

    def chat(self, prompt):
        self.user_message(prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.assistant_message(self.get_content(response))
        return self.get_content(response)
    
    def completion(_messages):
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=_messages
        )
