### call create_app package initialisation from __init__.py
from project import create_app  


if __name__=='__main__': 
    app=create_app() 
    app.run(debug=True) 
    