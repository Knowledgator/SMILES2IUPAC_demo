import gradio as gr
from chemicalconverters import NamesConverter

def convert(chemical_name, plot):
    # Initialize the ChemicalConverter
    converter = NamesConverter('knowledgator/IUPAC2SMILES-canonical-small')
    converted_name = converter.iupac_to_smiles(chemical_name)[0][:6]
    styles = {"<SYST>": "SYSTEMATIC", "<TRAD>": "TRADITIONAL", "<BASE>": "BASE"}
    return styles.get(converted_name, "")


iupac2style = gr.Interface(
    fn=convert,
    allow_flagging='auto',
    inputs=[
        gr.Textbox(label="Enter your IUPAC name", placeholder="Enter IUPAC name here"),
    ],
    outputs=[gr.Text(label="IUPAC style")],
    examples=[
        ["propan-2-yl 2-[4-(4-chlorophenyl)carbonylphenoxy]-2-methyl-propanoate"]
    ],
)