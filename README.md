# 🖼️ Image Captioning App (BLIP + Gradio)
This project implements an AI-powered image captioning application using the BLIP (Bootstrapped Language Image Pretraining) model from Hugging Face Transformers. The model leverages transfer learning, using a pretrained vision–language transformer to generate natural language descriptions from images.
A lightweight Gradio interface allows users to upload images and instantly receive AI-generated captions.
* ⚙️ Tech Stack
* 🐍 Python
* 🔥 PyTorch
* 🤗 Hugging Face Transformers
* 🎛️ Gradio
* 🖼️ PIL
* 🧠 Model Approach
* 
The application uses transfer learning, where the pretrained BLIP model—trained on large-scale image–text datasets—is applied to generate captions for new images without additional training.
This demonstrates how vision and language models can be integrated into practical applications with minimal infrastructure.
### 📊 Observations
The model performs well on clear, single-subject images.
For complex scenes with multiple objects or environments, captions may become less precise or incomplete, reflecting limitations of general-purpose pretrained models.
Examples are shown below in the demo screenshots.
### 📷 Comparing two images 
Example outputs from the application:
Simple image 
Image: Cat
Caption generated: “a cat laying on the floor looking up”
Complex scene
Image: Outdoor park with fountain and structures
Caption generated: “a small pond with a fountain and a few boats”
The second example highlights how scene complexity can reduce caption accuracy, as the model simplifies the environment.
