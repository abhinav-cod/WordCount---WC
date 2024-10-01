# WordCount-WC-


If you want to get only lines:
```
python wc_tool.py -l <file_path>
```
For words and characters:
```
python wc_tool.py -w -c <file_path>
```
For the default (lines, words, and characters):

```
python wc_tool.py <file_path>
```


Features :
1. Multiple File Support:
2. The tool can process multiple files in one command.
   It displays totals when multiple files are processed.
3. Verbose Mode (-v):
    Displays the file name alongside the counts for better clarity when processing multiple files.
    Compressed File Support:

4. Supports .gz and .bz2 compressed files by detecting the file extension and using the appropriate method to read the file.
5. Exclude Blank Lines (-b):
    Excludes blank lines from the line count when the -b or --blank option is provided.
6. Custom Output Format:
    Allows users to specify whether they want to count lines, words, or characters using the -l, -w, and -c options.

   
