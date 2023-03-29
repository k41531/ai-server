from gpt import Assistant

if __name__ == "__main__":
    assistant = Assistant()
    while True:
        message = input(">> ")
        res = assistant.chat(message)
        print(res)