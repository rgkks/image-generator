import requests
import urllib.parse

def generate_high_quality_image(prompt):
    
    enhanced_prompt = f"{prompt}, 8k resolution, cinematic lighting, masterpiece, highly detailed, high bitrate, clean shadows, smooth gradients, no compression artifacts, 16-bit color depth"
    
    encoded_prompt = urllib.parse.quote(enhanced_prompt)
    
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&width=1024&height=1024&enhance=true&nologo=true"
    
    print(f"Generating image from: {url}")
    filename = f"{prompt}.jpg"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"✅ Success! Image saved as {filename}")
        else:
            print(f"❌ Failed to generate image. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

while True:
    my_prompt = input(">")
    generate_high_quality_image(my_prompt)
