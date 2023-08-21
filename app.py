from transformers import pipeline
import gradio as gr

# If you want more control, you will need to define the tokenizer and model.
from transformers import AutoTokenizer, AutoModelForCausalLM


def hello(i):
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")
    return i


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
