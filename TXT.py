import os
import glob
from pybloom_live import BloomFilter
from tqdm import tqdm

# get the list of all .txt files in the directory
all_txt_files = glob.glob("*.txt")

# name of the final merged file
merged_file_name = "merged_file.txt"

# Make sure the merged_file is not already in the list of txt files to be merged
if merged_file_name in all_txt_files:
    all_txt_files.remove(merged_file_name)

# sort them by file size in descending order
all_txt_files.sort(key=os.path.getsize, reverse=True)

# Create a Bloom Filter. Adjust the expected number of items (218000000)
# and false positive rate (0.01) as needed.
bloom = BloomFilter(capacity=5000000000, error_rate=0.00000001)

print(f"Starting the merging process of {len(all_txt_files)} files.")

buffer_size = 1000000  # adjust this value based on your memory
buffer = []

# write the content of each txt file into the final merged file
for i, txt_file in enumerate(all_txt_files, 1):
    print(f"Processing file {i} of {len(all_txt_files)}: {txt_file}")

    with open(txt_file, "r") as file:
        for line in tqdm(file, desc=f"Processing '{txt_file}'", unit="line"):
            # only remember the line if it has not been written before
            if line not in bloom:
                bloom.add(line)
                buffer.append(line)

            # write to file when the buffer reaches the buffer size
            if len(buffer) >= buffer_size:
                with open(merged_file_name, "a") as merged_file:
                    merged_file.writelines(buffer)
                buffer = []

    # delete the txt file after merging its content
    os.remove(txt_file)

# write the remaining lines in the buffer to the file
if buffer:
    with open(merged_file_name, "a") as merged_file:
        merged_file.writelines(buffer)

print("All txt files have been merged into:", merged_file_name)
