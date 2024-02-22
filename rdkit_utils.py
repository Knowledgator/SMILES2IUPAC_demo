from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image


def plot_mol(smiles):
    # Convert the SMILES string to an RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)

    # Use RDKit to draw the molecule to an image, with original intended size
    img = Draw.MolToImage(mol, size=(185, 185))

    # Create a new, blank image with the desired final size (800x190 pixels) with a white background
    final_img = Image.new('RGB', (890, 185), 'white')

    # Calculate the position to paste the original image onto the blank image to keep it centered
    left = (890 - 185) // 2
    top = (185 - 185) // 2  # This will be zero in this case but included for clarity

    # Paste the original image onto the blank image
    final_img.paste(img, (left, top))

    return final_img
