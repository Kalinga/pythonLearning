

# coding=utf-8
cv_name = 'KALINGA_RAY_2019'
contact_email = "mailto:mail.kalinga@gmail.com"
contact_name = "Kalinga Bhusan Ray"

#role="Software Engineer(DataManagement) "
role="Data Scientist "

manager_name = ''
company_name = "QUNDIS"
#Complete Address
company_long_name = 'QUNDIS '
company_address = 'Sonnentor 2'
company_zip_town = '99098 Erfurt'

company_state_country = 'Deutschland'

DE=False
hascover=True

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