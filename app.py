from transformers import pipeline
import gradio as gr
from openxlab.model import download

def hello(i):
    print(download('alvin123/test_01', 'model_1'))
    classifier = pipeline("sentiment-analysis")
    a = classifier(i)
    return a


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
