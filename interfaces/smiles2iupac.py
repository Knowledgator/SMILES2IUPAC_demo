import gradio as gr
from rdkit_utils import plot_mol
from chemicalconverters import NamesConverter

def convert(chemical_name, style, validate, plot):
    # Initialize the ChemicalConverter
    converter = NamesConverter("knowledgator/SMILES2IUPAC-canonical-base")
    converted_name = ""
    validation_score = ""
    plot_image = None
    style_prefix = "<" + style[:4] + ">"
    if validate:
        converted_name, validation_score = converter.smiles_to_iupac(style_prefix + chemical_name, validate=True)
    else:
        converted_name = converter.smiles_to_iupac(style_prefix + chemical_name)
    if plot:
        plot_image = plot_mol(chemical_name)
    return converted_name[0], validation_score, plot_image

smiles2iupac = gr.Interface(
    fn=convert,
    allow_flagging='auto',
    inputs=[
        gr.Textbox(label="Enter your SMILES name", placeholder="Enter your SMILES name here"),
        gr.Radio(
            choices=["BASE", "SYSTEMATIC", "TRADITIONAL"],
            label="Choose desired IUPAC style",
        ),
        gr.Checkbox(label="Validate with molecular similarity", value=False),
        gr.Checkbox(label="Plot molecule", value=True)
    ],
    outputs=[gr.Text(label="Converted Name"),
             gr.Text(label="Input-Target similarity score"),
             gr.Image(type='pil', label="Molecule Plot", height=170, width=890)],
    examples=[
        ["CCO", "BASE", True, True]
    ],
)