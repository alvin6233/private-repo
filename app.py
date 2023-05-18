from transformers import pipeline
import gradio as gr
from openxlab.model import download

print(download('alvin123/test_01', 'model_1'))

def hello(i):
    classifier = pipeline("sentiment-analysis")
    a = classifier(i)
    return a


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
