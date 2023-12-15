import PIL.Image
import google.generativeai as genai
from IPython.display import Markdown



API_KEY = "AIzaSyDuRdWgzewtH-S454likHbb3rQWuqPe9s0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')
img = PIL.Image.open('OIP (4).jpeg')
response = model.generate_content(img)
print(response.text)
