import os 
import lzma
from tqdm import tqdm 

def xz_files_in_dir(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files


folder_path = "C:/Users/user/Documents/שנה ב/פרויקט/create_gpt/openwebtext"
output_file_train = "train_split.txt"
output_file_test = "val_split.txt"
vocab_file = "vocab.txt"

# split_files = int(input("how many files would you like to slit this into?"))
# max_count = total_files // split_files if split_files != 0 else total_files

files = xz_files_in_dir(folder_path)
total_files=len(files)

split_index = int(total_files*0.9)
files_train = files[:split_index]
files_test = files[split_index:]


vocab = set()

#process the training file
with open(output_file_train, "w", encoding="utf-8") as outfile:
    for filename in tqdm(files_train, total=len(files_train)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding="utf-8")as infile:
            text = infile.read()
            outfile.write(text)
            chars = set(text)
            vocab.update(chars)

#process the testing file
with open(output_file_test, "w", encoding="utf-8") as outfile:
    for filename in tqdm(files_test, total=len(files_test)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding="utf-8")as infile:
            text = infile.read()
            outfile.write(text)
            chars = set(text)
            vocab.update(chars)

#write the vocab
with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')
