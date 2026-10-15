from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load the API key from your .env file
load_dotenv()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

# Run the query
result = llm.invoke("What is the capital of countries in north america?")

# FIX: Extract the text out of the list and dictionary structure
if isinstance(result.content, list) and len(result.content) > 0:
    clean_text = result.content[0].get('text', '')
else:
    clean_text = result.content

# Output only the readable text
print(clean_text)
