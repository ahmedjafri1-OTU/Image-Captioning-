import torch
import gradio as gr
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

#Load model and processor once
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    if image is None:
        return "Please upload an image."

    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

app = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning App",
    description="Upload an image and generate a caption using BLIP.")

app.launch()