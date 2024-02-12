from openai import AzureOpenAI
import markdown
from dotenv import load_dotenv
import flask
import os

# Load the environment variables from .env.local file
load_dotenv(dotenv_path='.env.local')


# Access the variables using os.getenv
azure_api_key = os.getenv('azure_api_key')
azure_endpoint = os.getenv('azure_endpoint')
model = os.getenv('model')
api_version = os.getenv('api_verison')  # Note: there's a typo in 'api_verison'. It should be 'api_version'.

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=azure_api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version
)

def generate_streaming_response(user_message):          
        try:                
            stream = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_message}],
                temperature=0.9,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stream=True
            )
            
            for chunk in stream:
                  content = chunk['choices'][0].get('delta', {}).get('content')
                  if content is not None:
                        yield f'data: $s\n\n' % content

        except Exception as e:
              print(e)
              return flask.Response(status=500)
        


            
