# Git commit with message "Change model files to lower-case"

All the model files were renamed to lower case because

a) It was confusing to have the file share the same name as the class within it.
   (It made it seem like you were importing the class, when you were actually importing
   the module which contained the class)

b) It's the standard: https://peps.python.org/pep-0008/#package-and-module-names

Additionally, in this commit, I removed all the code in models/__init__.py
because exporting modules from an __init__.py was an unneccessary, outdated approach. 

Nowadays python can import the modules from any folder as long as it has the
__init__.py file. That file can be empty.