#Calen's Site
#Freeze.py
#Created: 11-03-2019

#Import modules section
from flask_frozen import Freezer
from myapp import app


#freeze app code
freezer = Freezer(app)

if __name__=='__main__':
    freezer.freeze()
