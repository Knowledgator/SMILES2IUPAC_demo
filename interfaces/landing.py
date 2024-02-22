import gradio as gr

with open('materials/introduction.html', 'r', encoding='utf-8') as file:
    html_description = file.read()

landing = gr.HTML(html_description)