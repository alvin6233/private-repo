from transformers import pipeline
import gradio as gr
import os

# If you want more control, you will need to define the tokenizer and model.
from transformers import AutoTokenizer, AutoModelForCausalLM

base_path = './wfbi_repo_3'
os.system(f'git clone https://code-in.openxlab.org.cn/dongxiaozhuang/wfbi_repo_3.git {base_path}')
print(f'git clone finished')
os.system(f'cd {base_path} && git lfs pull')
print(f'git lfs pull finished')

def hello(i):
    #os.system('rm -rf /home/xlab-app-center/.cache/huggingface/hub/models--distilgpt2')
    return i


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
