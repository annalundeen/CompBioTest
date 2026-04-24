import sys
import pandas as pd

# assume you already generated MEME results like before
# here we just standardize output

input_file = sys.argv[1]
output_file = sys.argv[2]

df = pd.read_csv(input_file, sep="\t")

df = df.rename(columns={"Match_Sequence": "Match"})
df = df[["Protein", "Motif", "Match", "P_value"]]   # keep P_value
df.to_csv(output_file, sep="\t", index=False)