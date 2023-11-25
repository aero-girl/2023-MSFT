from dotenv import load_dotenv
import os

# check if the .env file exists
def main():
    load_dotenv()
    print(os.getenv("OPENAI_API_TYPE"))
    print(os.getenv("OPENAI_API_VERSION"))
    print(os.getenv("OPENAI_API_BASE"))
    print(os.getenv("OPENAI_API_KEY"))

if __name__ == '__main__':
    main()