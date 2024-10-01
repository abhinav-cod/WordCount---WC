import sys
import argparse
import os
import gzip
import bz2  

def is_binary(file_path):
  try:
    with open(file_path,'rb') as file:
      chunk = file.read(1024)
      if b'\0' in chunk:
        return True
    return False
  except Exception as e:
    print(f"Error determining file type: {e}")
    return False

def count_lwc(file_path,isbinary=False, exclude_blank_lines=False):
  lines = 0
  words = 0
  chars = 0
  
  try:
    if isbinary:
      with open(file_path,'rb') as file:
        data = file.read()
        chars = len(data)
    else:
      open_func = open
      if file_path.endswith('.gz'):
        open_func = gzip.open
      elif file_path.endswith('.bz2'):
        open_func = bz2.open
      with open_func(file_path,'rt',encoding='utf-8',errors='ignore') as file:
        for line in file:
          if exclude_blank_lines and line.strip() == '':
            continue
          lines+=1
          words+=len(line.split())
          chars+= len(line)
    if lines==0  and chars==0:
      print(f"file '{file_path}' is empty")
    
    return lines,words,chars
  except FileNotFoundError:
    print(f"file '{file_path}' not found.")
    return None,None,None
  except PermissionError:
    print(f"Permission denied: '{file_path}'")
  except Exception as e:
    print(f"An error occurred {e}")
    return None,None,None
      

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser(description = "Custom wc tool in python")
  parser.add_argument("files",nargs="+",help="Path to files")
  parser.add_argument("-c","--chars", action="store_true",help = "Print the character count")
  parser.add_argument("-w","--words",action="store_true",help="Print the word count")
  parser.add_argument("-l","--lines",action="store_true",help="Print the Line count")
  parser.add_argument("-b", "--blank", action="store_true", help="Exclude blank lines")
  parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode (print file names)")
  
  args = parser.parse_args()
  file_paths = args.files
  if not (args.lines or args.words or args.chars):
    args.lines = args.words = args.chars = True
    
    
  total_lines, total_words, total_characters = 0, 0, 0
  
  for file_path in file_paths:
    if not os.path.exists(file_path):
      print(f"file '{file_path}' does not exist.")
      continue
    if os.path.isdir(file_path):
      print(f"'{file_path}' is a directory, not a file")
      continue
  
  
    isbinary = is_binary(file_path)
    print(isbinary)
  
  
    lines,words,chars = count_lwc(file_path,isbinary,exclude_blank_lines=args.blank)
    
    if lines is not None:
      if isbinary:
        if args.verbose:
          print(f"Binary file detected: '{file_path}'")
        if args.chars:
          print(f"{file_path}: Size in bytes: {chars}")
      else:
        if args.verbose:
          print(f"{file_path}:")
      # Print based on user input
        if args.lines:
          print(f"Lines: {lines}")
        if args.words:
          print(f"Words: {words}")
        if args.chars:
          print(f"Characters: {chars}")

  # Accumulate totals
      total_lines += lines
      total_words += words
      total_characters += chars
    
  if len(args.files) > 1:
    print("\nTotal across all files:")
    if args.lines:
      print(f"Total Lines: {total_lines}")
    if args.words:
      print(f"Total Words: {total_words}")
    if args.chars:
      print(f"Total Characters: {total_characters}")
      
      