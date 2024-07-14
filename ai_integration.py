# ChatGPT 3.5 Turbo

import requests
import config

chatgptapi = config.config["chatgpt_api_key"]

def get_chatbot_response(user_input):
    url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role" : "system", "content" : "Give short and friendly responses please.",

                "role" : "user",
                "content" : user_input
            }
        ]
    }
    headers = {
        "x-rapidapi-key": chatgptapi,
        "x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # Extract the "choices" key from the JSON response
    result = response.json().get("choices")[0].get("message").get("content")
    

    if result:
        return result
    else:
        return "Error: Unable to retrieve chatbot response."

