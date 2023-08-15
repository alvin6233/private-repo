from transformers import pipeline
import gradio as gr
from openxlab.model import download

def hello(i):
    download(model_repo='dongxiaozhuang/cli_down', model_name=['model_1'], overwrite=True)
    return i


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
