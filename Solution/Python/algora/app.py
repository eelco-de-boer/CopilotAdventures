import random
import requests
import json


def dance(lox_moves, drako_moves):
    
    forest_state = "Normal"

    for i in myrange:
        lox_move = lox_moves[i]
        drako_move = drako_moves[i]

        if lox_move == "Twirl" and drako_move == "Twirl":
            forest_state = "Fireflies light up the forest"
        elif lox_move == "Leap" and drako_move == "Spin":
            forest_state = "Gentle rain starts falling"
        elif lox_move == "Spin" and drako_move == "Leap":
            forest_state = "A rainbow appears in the sky"
        elif lox_move == "Twirl" and drako_move == "Leap":
            forest_state = "Leaves rustle in the wind"
        elif lox_move == "Twirl" and drako_move == "Spin":
            forest_state = "Flowers bloom in vibrant colors"
        elif lox_move == "Leap" and drako_move == "Leap":
            forest_state = "Butterflies fill the air"
        elif lox_move == "Spin" and drako_move == "Spin":
            forest_state = "Stars twinkle in the night sky"
        else:
            forest_state = "Different effect"

        print(f"Forest state after sequence {i+1}: {forest_state}")
        print(generate_image(forest_state)) # Generate an image based on the forest state


def generate_image(forest_state):
    url = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generations?api-version=2023-12-01-preview"
    payload = {
        "prompt": forest_state,
        "size": "1024x1024",
        "quality": "hd", 
        "style": "vivid"
    }
    print(payload)
    headers = {
        "Content-Type": "application/json",
        "api-key": "c6793551a72640a6957c02df798df68e"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    if response.status_code == 200:
        response.json()
        image_url = response.json().content.get("url")
        return f"Generated image: {image_url}"
    else:
        return "Failed to generate image"



# Example usage
myrange = range(1)
lox_moves = random.choices(["Twirl", "Leap", "Spin"], k=len(myrange))
drako_moves = random.choices(["Twirl", "Leap", "Spin"], k=len(myrange))

dance(lox_moves, drako_moves)
