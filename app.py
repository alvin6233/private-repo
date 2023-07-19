from transformers import pipeline
import gradio as gr
from openxlab.model import download
from openxlab.model import inference

def hello(i):
    # try:
    #     result = inference("meijiawen1/test-image", ["./demo_text_ocr.jpg"])
    # except Exception as e:
    #     print(f'error:{e}')
    download(model_repo='houshaowei/AnimateDiff', model_name=['mm_sd_v15.ckpt','mm_sd_v14.ckpt'])
    classifier = pipeline("sentiment-analysis")
    a = classifier(i)
    return a


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
