 import openai

openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key

def generate_image(prompt, size="1024x1024"):
    """Generate an image based on a text prompt using OpenAI DALL·E."""
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size
    )
    return response['data'][0]['url']  # Returns the image URL

# Example usage (You can remove this in production)
if __name__ == "__main__":
    print(generate_image("A futuristic cyberpunk city"))
