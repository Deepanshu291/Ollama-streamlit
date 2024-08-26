import ollama

# models = ollama.list()
# for i in models['models']:
#     print(i['name'])

models = "\n".join([i['name'] for i in ollama.list()['models']])
print(models)


# def chat(user_input):
#     res = ollama.chat(model='phi3',messages=[
#     {
#         'role':'user',
#         'content': user_input
#     }
#     ])
#     return res

# while True:
#     user_input = input(">>")
#     res = chat(user_input)
#     print(res['message']['content'])
