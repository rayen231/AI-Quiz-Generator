from groq import Groq
import base64
from PIL import Image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
def PictureAnalyser(image_path):
    # Path to your image
    #image_path = r"C:\Users\Rayen\Downloads\images.jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)


    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe that picture in details and focus in any informations that can help later to make a quiz ."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url":f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None, 
    )

    return completion.choices[0].message.content
def check_image_size(image_path,MAX_PIXELS=33177600  ):
    with Image.open(image_path) as img:
        width, height = img.size
        total_pixels = width * height

        if total_pixels > MAX_PIXELS:
            print(f"Image too large: {total_pixels} pixels. Resizing...")
            scale_factor = (MAX_PIXELS / total_pixels) ** 0.5  # Calculate scaling factor
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)

            img = img.resize((new_width, new_height),Image.LANCZOS)
            resized_path = image_path.replace(".jpg", "_resized.jpg")  # Change file name
            img.save(resized_path)

            return resized_path  # Return new image path

        return image_path  # If within limit, return original

# print("this is the result :",PictureAnalyser(image_path="output_images/page_1_img_2.png"))