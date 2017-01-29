import os
import pdfkit

kalinga = 'KALINGA_RAY_2017'
html_file = "../gen/" + kalinga + '.html'
pdf_file = "../gen/" + kalinga + '.pdf'

if not os.path.exists("../gen"):
    os.mkdir("../gen")

def skeleton():
    return \
        '''
        <!DOCTYPE html>
        <html>
            <head>
            <title>Kalinga Bhusan Ray</title>
            </head>

            <body>
            <h1>Kalinga Bhusan Ray</h1>
            <p title="I'm a tooltip">
                This is a paragraph with tooltip.
            </p>

            </body>
        </html>
        '''

with open(html_file,'w+') as f:
    message = skeleton()

    f.write(message)



pdfkit.from_file(html_file, pdf_file)
