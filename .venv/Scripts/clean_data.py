import gdown
import tempfile
import pandas as pd

file_id = "1UaGOuNBi0IeInwah93ltlrNIUj9bNFgp"
url = f'https://drive.google.com/uc?id={file_id}'

with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
    gdown.download(url,tmp.name,quiet=False)
    tmp.close

df = pd.read_csv(tmp.name)
df