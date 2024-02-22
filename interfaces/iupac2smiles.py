import gradio as gr
from rdkit_utils import plot_mol
from chemicalconverters import NamesConverter

def convert(chemical_name, plot):
    # Initialize the ChemicalConverter
    converter = NamesConverter('knowledgator/IUPAC2SMILES-canonical-small')
    converted_name = ""
    plot_image = None
    converted_name = converter.iupac_to_smiles(chemical_name)[0][6:]
    if plot:
        plot_image = plot_mol(converted_name)
    return converted_name, plot_image


iupac2smiles = gr.Interface(
    fn=convert,
    allow_flagging='auto',
    inputs=[
        gr.Textbox(label="Enter your IUPAC name", placeholder="Enter IUPAC name here"),
        gr.Checkbox(label="Plot molecule", value=True)
    ],
    outputs=[gr.Text(label="Converted Name"),
             gr.Image(type='pil', label="Molecule Plot", height=170, width=890)],
    examples=[
        ["ethanol", True]
    ],
)