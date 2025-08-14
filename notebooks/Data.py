from datasets import load_dataset
dataset = load_dataset("mrm8488/goemotions")

print(dataset["train"].to_pandas().head())


train_data = dataset["train"]
print(train_data.column_names) #print columns
