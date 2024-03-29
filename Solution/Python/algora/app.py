import random
import requests

def generate_images(forest_state):
    api_key = "KEY"  # Replace with your actual API key

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    endpoint = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generations?api-version=2023-12-01-preview"
    payload = {
        "prompt": forest_state,
        "size": "1024x1024",
        "quality": "hd", 
        "style": "vivid"
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()

    result = response.json()
    image_url = result["data"][0]["url"]
    return image_url

def simulate_dance(lox_moves, drako_moves):
    forest_state = []
    effects = {
        ("Twirl", "Twirl"): "Fireflies light up the forest.",
        ("Leap", "Spin"): "Gentle rain starts falling.",
        ("Spin", "Leap"): "A rainbow appears in the sky.",
    }
    animals = ["bear", "rabbit", "deer", "fox", "squirrel"]
    animal_moves = ["flying", "diving", "singing"]

    for lox_move, drako_move in zip(lox_moves, drako_moves):
        effect = effects.get((lox_move, drako_move))
        if effect is None:
            effect = f"A {random.choice(animal_moves)} {random.choice(animals)} appears."
        forest_state.append(effect)

    return forest_state

lox_moves = ["Twirl", "Leap", "Spin", "Twirl", "Twirl", "Leap"]
drako_moves = ["Spin", "Twirl", "Leap", "Leap", "Twirl", "Spin"]

forest_state = simulate_dance(lox_moves, drako_moves)

for i, state in enumerate(forest_state, 1):
    print(f"After sequence {i}, {state}")
    image_url = generate_images(state)
    response = requests.get(image_url)
    response.raise_for_status()
    image_data = response.content
    file_path = f"/workspaces/CopilotAdventures/Solution/Python/algora/Tmp/image{i}.jpg"  # Replace with your desired file path
    with open(file_path, "wb") as file:
        file.write(image_data)
    print(f"Image downloaded and stored at: {file_path}")
    print(f"Generated image URL: {image_url}")