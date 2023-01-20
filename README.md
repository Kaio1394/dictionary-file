# Official repository (Dictionary file)

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Dicionary file</h3>



---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## Table of Contents

- [About](#about)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## About <a name = "about"></a>

This project aims to manipulate files (txt and yaml) to save requests in a REST API.
Ex.: save the requests that will be used in a POST in a .txt file, thus making the project more organized.

### Prerequisites

- generate-lib
- Robotframework


### Installing

To install the library just use command line:
```
pip install dictionary-file
```
In addition to having python installed.
Obs.: You can create a python environment(recommended) or not.

## Running the tests <a name = "tests"></a>

To run the functions just import the library in your robotframework project.
```robotframework
*** Settings ***
Library    dictionary_file
*** Keywords ***
Library testing
    ${t}        CREATE DICT BY FILE TXT    file_name=${EMPTY}        full_path=C:\\Users\\Vericoders\\Documents\\test-lib\\dicionario.txt
    UPDATE DICTIONARY    ${t}     name=Yuri
    Log To Console    \n${t}
*** Test Cases ***
Scenario 01
    [Tags]        teste
    Library testing
```

The keyword (CREATE DICT FILE TXT) create a dictionary through txt file.
```python
def create_dict_by_file_txt(self, name_file: str, full_path: str = None) -> dict:
        if full_path is None:
            arq =  open(os.path.dirname(__file__) + f"/{name_file}", 'r')
        elif full_path is not None and name_file == "":
            arq =  open(f"{full_path}", 'r')
        lines = arq.readlines()
        dict_ = dict()
        for line in lines:
            if line is not None and "=" in line:
                list_kys_values = ''.join(line.replace(' ', '')).split(',')
                for item in list_kys_values:
                    key = item.split('=')[0]
                    value = item.split('=')[1]  
                    if "@" in value:
                        value =  generate_email_random(1)
                    if self.LINE_BREAK in value: 
                        value = value.replace(self.LINE_BREAK, '')
                    if value.startswith(self.STR):
                        value = value.replace(self.STR, '').replace(')', '')
                    if value.startswith(self.INT):
                        value = int(value.replace(self.INT, '').replace(')', ''))                                                          
                    dict_.update({key: value})               
            else:
                break
        return dict_
```
The file .txt needs to contains some features. Example:
```txt
name=str(kaio), email=str(kaio.santiago@hotmail.com), password=int(1234), admin=str(true)
```
Values of dict needs to be defined type as in the example above.
- string: str(<word>)
- int: int(number_int)
- bool: bool(true_or_false)

## Usage <a name="usage"></a>

Use to take information through txt file to create dictionary. This is useful to create requisition(dictionary) to test automation API REST. 

## Built Using <a name = "built_using"></a>

- [Python](https://docs.python.org/3/) - Programming language
- [Robot](https://robotframework.org/) - Automation Framework

## Authors <a name = "authors"></a>

- [@Kaio1394](https://github.com/Kaio1394) - Idea & Initial work