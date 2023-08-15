from transformers import pipeline
import gradio as gr
from openxlab.model import download

def hello(i):
    XLAB_CACHE='/home/xlab-app-center'
    download(model_repo='LAMM/lamm_llm_7b_v0', model_name=['tokenizer.model'],output=XLAB_CACHE, overwrite=True)
    return i


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
