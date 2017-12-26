# WhatsTheFile
Python library for obtaining file info and for hashing a text file with md5 or sha1


## Contents
whatsTheFile.py contains the 4 functions that take a filepath as an argument.   
- getFileName()  ...return the string of filename of the file at the filepath or "file does not exist"    
- getFileSize()  ...return the string of filesize fo the file at the filepath or "file does not exist"     
- to_md5()       ...return the string of md5 digest of the file at the filepath or "file does not exist"    
- to_sha1()      ...return the string of sha1 digest of the file at the filepath or "file does not exist"  

ex. If the filepath was "/home/aaa/mydata.txt", which contains the text "The quick brown fox jumps over the lazy dog",  
  ....... getFileName(filepath) return "mydata.txt"  
  ....... getFileSize(filepath) return "44"  
  ....... to_md5(filepath)   return "2fd4e1c67a2d28fced849ee1bb76e7391b93eb12"  
  ....... to_sha1(filepath) return "9e107d9d372bb6826bd81d3542a419d6"  

## How To Use
1. copy whatsTheFile.py into the same directory with a .py file that you want to use this function.
or your LIB directory of the python.

2. Add "import whatsTheFile" in the .py file.

```
import whatsTheFile
```

3. Set filepath as an argument. 
```
//ex. 
print(getFileName("c/document/text.txt"))
```
```
//ex. 
filepath = "c/document/text.txt"
print(getFileName(filepath))   
```
4. call a fanction with the whatsTheFile.wtf.\[function name\](filepath)   
```
//ex. 
print(whatsTheFile.wtf.getFileName(filePath))   
```

... or make an instance first, then call a function   
```
//ex.
a = whatsTheFile  
print(a.wtf.getFileName(filePath))  
```

## License

MIT


