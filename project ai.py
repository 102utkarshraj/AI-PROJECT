import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyB3i--ZJyZSUOkws4_DHx4u70Q2LvAPNAE"

genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def grammar_check_with_gemini(text):
    prompt = f"""
    You are an AI grammar and spelling coach. Check the following sentence for grammar and spelling errors.
    Provide the corrected version of the text and briefly explain any changes.

    Text: "{text}"
    """

    response = model.generate_content(prompt)
    return response.text

# Test it
user_input = input("Enter your sentence: ")
result = grammar_check_with_gemini(user_input)

print("\n--- Gemini Grammar Coach Response ---")
print(result)
