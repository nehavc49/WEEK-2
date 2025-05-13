
# Import Gemini API
import google.generativeai as genai

# Set API Key
api_key = "AIzaSyB-CYkNelmluUaBvMH0mOsNsDY5YEuY8hQ"  
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# #1 Text Generation
def generate_text(prompt):
    return model.generate_content(prompt)

# #2 Text Summarization
def text_summarization(text):
    return model.generate_content(f"Summarize this: {text}")

# #3 Question Answering
def question_answering(context, question):
    return model.generate_content(f"Question: {question} Context: {context}")

# #4 Sentiment Analysis
def sentiment_analysis(text):
    return model.generate_content(f"Analyze the sentiment of this text: {text}")

# #5 Text Translation
def text_translation(text, target_language):
    return model.generate_content(f"Translate this text to {target_language}: {text}")


# Example Usage
if __name__ == "__main__":
    # 1. Text generation
    prompt = "The quick brown fox"
    print(generate_text(prompt).text)

    # 2. Summarization
    text = "The quick brown fox jumps over the lazy dog"
    print(text_summarization(text).text)

    # 3. Question answering
    context = "The quick brown fox jumps over the lazy dog"
    question = "What does the fox jump over?"
    print(question_answering(context, question).text)

    # 4. Sentiment analysis
    text = "The quick brown fox jumps over the lazy dog"
    print(sentiment_analysis(text).text)

    # 5. Translation
    text = "The quick brown fox jumps over the lazy dog"
    target_language = "es"  # Spanish
    print(text_translation(text, target_language).text)
