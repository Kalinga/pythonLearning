import os
import pdfkit

kalinga = 'KALINGA_RAY_2017'
html_file = "../my-pdf/" + kalinga + '.html'
pdf_file = "../my-pdf/" + kalinga + '.pdf'


def skeleton():
    return \
        '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>

        <h1>This is a Heading</h1>
        <p title="I'm a tooltip">
            This is a paragraph with tooltip.
        </p>

        </body>
        </html>
        '''

with open(html_file,'w') as f:
    message = skeleton()

    f.write(message)



pdfkit.from_file(html_file, pdf_file)
