# How to Read a PDF file, extract informations and save them in a XLSX file

Hi, there! 
In this short tutorial, I will show you how to implement the Python PDF Reader, extracting relevant pieces of information and also saving this information in an XLSX file.

This Extractor program is capable to:
- Read PDF files, including files that have images and codes (like QR codes)
- Find dates using Regular Expressions
- Find some corresponding information according to what was required
- Create a DataFrame with all the information, joining match elements
- Check if the specific folder exists. If not, create a folder to save the file
- Save the XLSX file into the folder that was created or found 

# Install the Python Libraries
All the libraries that I used could be found in the **requirements.txt** file

# About the other Files
The **example-files** The folder includes three (3) files that I create to use as examples in this tutorial.

The **Folder_Name** is just a folder example that I created in this test.

The **file_sheet_name.xlsx** is a file created in this test inside the folder.

# About the Regex Library
When you use the _re_ library, it is possible just check if the element exists, find this element, and also save this element in a variable. In this tutorial, I needed to save the elements to include in my DataFrame. To do that I needed to use the _compile_ and after the _findall_ methods. These methods return a list and a list inside the main list includindg the element if it has been found and an empty list if not. For that reason a need to filter this main list after applied the Regex just to take the elements.
To learn more about Regex, try the [documentation](https://docs.python.org/3/library/re.html)
To practice Regular Expressions, try [this site](https://docs.python.org/3/library/re.html) 

# Result with the File Examples

Trying this code with the example files, I got the result below:

![alt text][image]

[image]: data-frame.png "Prompt Image"


### I hope tha I could help, enjoy! 
