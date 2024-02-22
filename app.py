import gradio as gr
from interfaces import smiles2iupac, iupac2smiles, iupac2style, landing


demo = gr.TabbedInterface([landing, smiles2iupac, iupac2smiles, iupac2style],
                          ["Introduction", "SMILES-to-IUPAC", "IUPAC-to-SMILES", "IUPAC style prediction"],
                          title="ChemicalConverters 🧪🔬🧬👨🏻‍🔬",
                          theme=gr.themes.Base())

demo.launch(share=True)
