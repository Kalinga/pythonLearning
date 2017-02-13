#!/bin/bash

# Need to run this script only once
#./init.sh
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
tar -xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
sudo cp -r wkhtmltox/* /usr/
ls -la
rm -rf wkhtmltox

#sudo pip install django-pdfkit

#With pip version 1.5.4- 1.5.6 there are several problems while installing modules from pypi
#As an alternative installaion from PyCharm can be tried Files->Settings->Project-Interpreter->+ (Available Modules)

