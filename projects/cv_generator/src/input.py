

# coding=utf-8
cv_name = 'KALINGA_RAY_2019'
contact_email = "mailto:mail.kalinga@gmail.com"
contact_name = "Kalinga Bhusan Ray"

#role="Software Engineer(DataManagement) "
#role="Senior Data Analyst "
role="Industrial Data Science Engineer "


manager_name = ''
company_name = ""
#Complete Address
company_long_name = 'gmbh '
company_address = ''
company_zip_town = 'Berlin'

company_state_country = 'Germany'

DE=False
#hascover=True
hascover=False

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