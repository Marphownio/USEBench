import pandas as pd


df = pd.read_csv("/hdd1/mww/USEBench/S-Bench/prompt-based-attack.csv",header=0)


df0 = df[df["attack"]=="ICA"]
print(len(df0))
df0.to_csv("/hdd1/mww/USEBench/S-Bench/ICA.csv",index=False)

