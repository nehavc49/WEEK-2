import google.generativeai as genai
import time

# 🔐 Set your Gemini API key
GOOGLE_API_KEY = "AIzaSyDVpzkqtOh34j7RtU0crvTfwFjExTwELxU"
genai.configure(api_key=GOOGLE_API_KEY)

def planner_agent(user_prompt: str) -> str:
    print("🧭 Planner Agent working...\n")
    
    models_to_try = ["models/gemini-1.5-pro", "models/gemini-pro"]
    retries = 3
    delay_seconds = 30

    for model_name in models_to_try:
        for attempt in range(retries):
            try:
                print(f"🔄 Attempt {attempt + 1} with model: {model_name}")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(user_prompt)
                return response.text
            except Exception as e:
                print(f"⚠️ Error with model {model_name}: {e}")
                print(f"⏳ Waiting {delay_seconds} seconds before retry...")
                time.sleep(delay_seconds)

        print(f"❌ All {retries} retries failed for model {model_name}. Trying next model...\n")

    return "❌ Failed to generate a response due to API quota issues or other errors."

def main():
    user_task = (
        "Plan a 7-day budget-friendly solo travel itinerary through South India. "
        "Include top places to visit, suggested routes, local food recommendations, and estimated cost per day."
    )

    plan = planner_agent(user_task)

    print("\n📌 Travel Plan:\n")
    print(plan)

if __name__ == "__main__":
    main()
