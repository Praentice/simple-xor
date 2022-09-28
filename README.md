# Simple-xor
This CLI tool allows you XOR two files and output the result to another file.
Useful if you need to recreate the parity disk of a RAID array.
## Install
```
git clone link_of_repository 
```
### Running the tool
```
./main.py -f1 path/to/first/file -f2 path/to/second/file #XOR two files and output the result to a file named "output"
./main.py -f1 path/to/first/file -f2 path/to/second/file -o custom_output #XOR two files and output the result to a file named "custom_output"

```
## Documentation
### Mandatory flags
| Flag          | Description                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f1 / --file1 | Absolute path of the first file to be XOR                                                                                                                                   |
| -f2 / --file2 | Absolute path of the second file to be XOR                                                                                                                                  |
### Optional flags
| Flag           | Description                                                                       |
|----------------|-----------------------------------------------------------------------------------|
| -o / --output  | Specify a name for the output file (Without this flag, default name is "output".) |
| -v / --version | Print the version of tool and exit                                                |
## Credits

This tool was created by Prantice but was heavily inspired by Megabeets, don't hesitate to check his article and website on the following link (https://www.megabeets.net/xor-files-python/). 

This tool is provided for free under GNU License.


