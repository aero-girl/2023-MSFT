from dotenv import load_dotenv
import os
import openai

# check if the .env file exists
def main():
    load_dotenv()
    
    # Get API key from environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY") 
    print(f"OPENAI_API_KEY:{openai.api_key}") 

    openai.api_base = os.getenv("OPENAI_API_BASE") 
    print(f"OPENAI_API_BASE:{openai.api_base}") 

    openai.api_type = os.getenv("OPENAI_API_TYPE")
    print(f"OPENAI_API_TYPE:{openai.api_type}") 

    openai.api_version = os.getenv("OPENAI_API_VERSION")
    print(f"OPENAI_API_VERSION:{openai.api_version}") 

if __name__ == '__main__':
    main()