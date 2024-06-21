from ollama import Client
def main_ai2(input2): 
    client = Client(host='http://localhost:11434')
    response = client.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': input2,
    },
    ])
    return (response['message']['content'])
