import os
import openai

from dotenv import load_dotenv
import webbrowser

load_dotenv()
#print(os.environ["API_SECRET_KEY"])

# Load your API key from an environment variable or secret management service
openai.api_key = os.environ["API_SECRET_KEY"]

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
#print(response)
response = openai.Image.create(
  prompt="a avatar for sophia",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

#print(image_url)
webbrowser.open(image_url)

#https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CnstXx9UKdCHVIDSA5XJqXm/user-2cePJUZHPMuc5KWViMtS3luX/img-QFtq5IjUrd1DtTTilfvqrXcL.png?st=2022-12-25T20%3A32%3A28Z&se=2022-12-25T22%3A32%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-25T14%3A26%3A38Z&ske=2022-12-26T14%3A26%3A38Z&sks=b&skv=2021-08-06&sig=30WYU/HESwOLMwDcJfzP9gmtXcSLV/2KMvXrkWmh1I8%3D

#https://oaidalleapiprodscus.blob.core.windows.net/private/org-2CnstXx9UKdCHVIDSA5XJqXm/user-2cePJUZHPMuc5KWViMtS3luX/img-UibRVVmX6a5o0DATTv0wKa1B.png?st=2022-12-25T20%3A35%3A10Z&se=2022-12-25T22%3A35%3A10Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-25T15%3A01%3A57Z&ske=2022-12-26T15%3A01%3A57Z&sks=b&skv=2021-08-06&sig=u%2Bi8dBYJLUk6zkva9xy0ofbvkLs/pZztx1PWWQH5tyQ%3D