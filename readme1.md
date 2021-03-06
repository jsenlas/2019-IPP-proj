Documentation of Project Implementation for IPP 2018/2019  
Name and surname: Jakub Sencak  
Login: xsenca00  

--------

## About

I have implemented extension STATP.  
I have not implemented short options.    

--------

## Dependencies

Using **PHP v7.3**

There has to be few dependencies installed to run this script:

- XMLWriter [1]  

- SimpleXML

- libxml

--------

## Files

#### parse.php

Contains the ```main``` part of the script. Everything starts here.

#### debug.php
 
Contains one value ```$debug``` which is used to print a lot of stuff to *stdout*. Diagnostics information and it may help during debugging.

#### stat.php

Contains definition of ```class Statistics```. It has 4 private parameters which are set to 0 at the beginning and 4 enable parameters which act as flags. These flags are necessary during printing statistics to the statistics file.  

```public function setEnable ($params_array)```  Checks whether there is a parameter in array of parameters and sets the *enable flags*.

There are public functions that are used for incrementing values of private parameters as well as methods for getting the values.

#### functions.php

This file was made to make the parse.php file a little bit lightweight.


```function err_out($ret_val)``` Returns return value to the *stderr*      

These functions generate XML:  
```function generate_instruction_start($xw, &$line_counter, $word)```  
```function generate_arg($xw, $type, $arg, $attr)```  
```function generate_symb($xw, $order, $word_a)```  
```function generate_instruction_end($xw)```  

Check string for lexical errors:  
```function symb_regex($symb_string)```  
```function var_regex($var_string)```  


#### Errors.php

Takes care of all errors, assess arguments and decides what to do.   

--------

## How does it work

1. Take care of the arguments  
2. Open files
3. Process one line of source file - using regular expressions to check lexical errors
4. Output to XML - using XMLWriter functions
5. Loop 3. and 4.
6. Close files 
7. Write statistics
8. Close files   

--------

## Literature 

[1] http://php.net/manual/en/book.xmlwriter.php

> Have a nice day