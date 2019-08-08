# coding=utf-8
cv_name = 'KALINGA_RAY_2019'
contact_email = "mailto:mail.kalinga@gmail.com"
contact_name = "Kalinga Bhusan Ray"


manager_name = ''
company_name = ""

#Complete Address
company_long_name = ''
company_address = ''
company_zip_town = ''
company_state_country = 'Deutschland'

DE=False

html_file = "../gen/" + cv_name + '.html'
pdf_file = "../gen/" + cv_name + '_' + company_name + '.pdf'
cover = "../gen/" + 'cover.html'

def mailBody():
    '''
    Hello,

    Please find the attached Profile matching the advertised job along with the cover letter.

    The most recent profile can be found at: https://github.com/Kalinga/pythonLearning/blob/master/projects/cv_generator/cv/KALINGA_RAY_2019.pdf

    Best Regards,
    Kalinga
    '''

