# ai_generator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_marketing_content(prompt):
    """
    Generate marketing content using OpenAI API.
    :param prompt: The input text describing what you want (e.g. "Write an email to promote a new product")
    :return: Generated text content
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful marketing assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your marketing prompt: ")
    result = generate_marketing_content(user_prompt)
    print("\nGenerated Content:\n")
    print(result)
