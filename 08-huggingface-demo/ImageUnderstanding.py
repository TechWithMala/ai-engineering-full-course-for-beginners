# pip install transformers

import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 

raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

question = "What is the color of the dog?"
inputs = processor(raw_image, question, return_tensors="pt")
out = model.generate(**inputs)

print(processor.decode(out[0], skip_special_tokens=True))

raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

question = "What is the color of the girl's shirt?"
inputs = processor(raw_image, question, return_tensors="pt")
out = model.generate(**inputs)

print(processor.decode(out[0], skip_special_tokens=True))