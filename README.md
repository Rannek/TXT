# TXT.py - Unique Python .txt File Merger

This Python script, merges text files (.txt) in the current directory into a single file. The script uses a Bloom filter to avoid duplicate lines and it can handle large files thanks to a buffer system. This is particularly useful in cases where you have a large number of text files and you want to consolidate them into a single text file.

Please note that this script will **delete** the original files after their contents have been merged into the new file.

## Prerequisites

This script requires the following Python packages:
- `pybloom_live`
- `tqdm`
- `glob`
- `os`

You can install them via pip:

```bash
pip install pybloom_live tqdm
```

## Usage

Save the script in the directory containing the text files to be merged and run it. The script will create a new text file named "merged_file.txt" that contains the contents of all the original files.

```bash
python TXT.py
```

## Warning

**This script deletes the original text files after their contents have been merged into the new file. If you want to keep the original files, comment out or remove the line: `os.remove(txt_file)` before running the script.**

## Customize

You can customize the following parameters in the script:

- `merged_file_name`: the name of the final merged file.
- `capacity` and `error_rate` of Bloom Filter: adjust these values based on your need. A higher capacity can handle more unique lines, but it uses more memory. A lower error rate reduces the chance of false positives (duplicate lines), but it also uses more memory.
- `buffer_size`: the number of lines that the script stores in memory before writing them to the file. If you have a lot of memory, you can increase this value to make the script run faster.
