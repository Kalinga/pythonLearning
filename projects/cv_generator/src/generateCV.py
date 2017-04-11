# coding=utf-8
import os

import datetime
import pdfkit

cv_name = 'KALINGA_RAY_2017'
html_file = "../gen/" + cv_name + '.html'
pdf_file = "../gen/" + cv_name + '.pdf'
cover = "../gen/" + 'cover.html'

if not os.path.exists("../gen"):
    os.mkdir("../gen")

def footer(mail, name, gen_time):
    return \
        '''
        <footer>
            <p align="middle">The html/pdf is generated by python project hosted on \
             <a href="https://github.com/Kalinga/pythonLearning/tree/master/projects/cv_generator">GitHub</a> at {2}
            </p>
            <p align="middle">Contact \
             <a href={0}>{1}</a> \
             with your questions, comments, and suggestions
            </p>
        </footer>
        '''.format(mail, name, gen_time)

def emptylines(no):
    return '''<br>''' * no

def htmlstart(title_name):
    return \
        '''
        <!DOCTYPE html>
        <html>

            <head>
                <title>{0}</title>
                <meta charset="UTF-8">
                <link href="../src/main.css" rel="stylesheet" type="text/css">
            </head>
        '''.format(title_name)

def pageheading():
    return \
        '''
        <body>
            <div id="Container">
                <article class="Container_article" id="personal_details">
                    <h3>Kalinga Bhusan Ray</h3>
                    <address>
                        M: +91-7795346374<br>
                        E: <a href="mailto:mail.kalinga@gmail.com">mail.kalinga@gmail.com</a><br>
                        <a href=https://www.linkedin.com/in/kalinga-bhusan-ray-88505724/>LinkedIn</a>
                        <a href=https://github.com/Kalinga>GitHub</a><br>
                        DOB: 2nd June 1983<br>
                        Indian | Married<br>
                        Adugodi, Bangalore, India, PIN: 560030<br>
                    </address>
                </article>
                <article class="Container_article" id="rightMostImage">
                    <img src="../img/myimage.jpg" alt="Kalinga's photo">
                </article>
            </div >
        '''

def intro():
    return \
        '''
        <h4>CAREER OBJECTIVE</h4>
        <p> To pursue a Master’s Degree in the field of applied Computer science such as Data Analysis, Data science,
            which would enhance my existing skills, give me practical exposure of utilizing the theoretical concepts
            taught during Undergraduate course (as well as self taught in the recent past) in a real time environment.
            And hone my professional skills that I have gained while working as Software engineer in IT industry for
            last 10 years. Also want to spent some more time learning and  living in German society as my last 1.5yrs
            of stay in Hildesheim, Germany was great and enriching in terms of personal and professional life.
        </p>
        '''

def technical():
    return \
        '''
        <h4>Technical Domain:</h4>
            <ul>
                <li>Object Oriented application and framework development using C, C++</li>
                <li>Domain Specific Language (DSL) development using Core Java, Xtend/Xtext</li>
                <li>Integration Test framework development using Python</li>
                <li>HMI Application development for Linux, Symbian, MeeGo devices</li>
                <li>Sound knowledge of HTML, CSS, XML, Java Script</li>
                <li>Git, ClearCase, Subversion,Eclipse, Carbide, CodeWarior etc..</li>
                <li>Make, CMake, Boost Library</li>
                <li>TDD, Unit testing (JUnit, Google Test), Integration Testing</li>
                <li>Agile methodologies, Scrum, Planning & Estimation, CI(Jenkins)</li>
                <li>Disigning using UML, Enterprise Architect</li>
                <li>Working knowledge of Android, Shell script, Perl, Data Analysis and Machine Learning</li>

            </ul>
            <hr>
        '''

def functional():
    return \
        '''
        <h4>Functional Domain:</h4>
                <ul>
                    <li>Car Multimedia Application development</li>
                    <li>Service framework development (Using DSL)</li>
                    <li>Interface Test Automation</li>
                    <li>Media Player and Media Gallery</li>
                    <li>Webkit based web browser</li>
                </ul>
                <hr>
        '''
def keyresponsibilities():
    return \
        '''
        <h4>Key Responsibilities:</h4>
        <ul>
            <li>Participation in the Sprint Planning (Agile) and Review</li>
            <li>Design (using UML) and Design review</li>
            <li>Coding(C, C++, Java, Python/Linux), code review, unit testing and documentation.</li>
            <li>Test Plan and Test Automation</li>
        </ul>
        <hr>
        '''

def experience(position, company, duration):
    return \
        '''
        <h5>''' + position + '''</h5>
        <div>
            <article><h6>''' + company + '''</h6>
            </article>
            <article style="float:right"> <h6>''' + duration + '''</h6>
            </article>
        </div>
        <!--hr-->
        '''

def experiences():
    return \
    '''<h4>EXPERIENCE:</h4>''' + \
    experience("Specialist-Car Multimedia",
               "Robert Bosch Engineering and Business Solutions, Bangalore",
               "Dec'11-Present") + \
    experience("Senior Software Engineer-R&D (Adaptxt)",
               "Keypoint technology, Hyd",
               "Mar'10-Dec'11") + \
    experience("Senior Software Engineer (Azingo Browser)",
               "Azingo Soft Systems India PVT LTD, Hyd",
               "May'09-Mar'10") + \
    experience("Software Engineer- (Sasken Media Player)",
               "Sasken Communication Technologies, Bangalore",
               "Dec'06-May'09") + \
    experience("MIS executive",
               "iSeva,E4E Pvt ltd,Bangalore",
               "Apr'06-Dec'06")

def certificate(cert, institute, duration):
    return \
        '''
        <h5>''' + cert + '''</h5>
        <div>
            <article><h6>''' + institute + '''</h6>
            </article>
            <article style="float:right"> <h6>''' + duration + '''</h6>
            </article>
        </div>
        <!--hr-->
        '''
def certificate_link(cert, institute, duration, link, id):
    return \
        '''
        <h5>''' + cert + '''</h5>
        <div>
            <article><h6>''' + institute + '''</h6>
            </article>
            <article id="certificate"><span>Certificate Id: </span><a id="certificate" href='''+link+'''>'''+ id +'''</a>
            </article>
            <article style="float:right"> <h6>''' + duration + '''</h6>
            </article>
        </div>
        '''

def certificates():
    return \
    '''<h4>CERTIFICATION:</h4>''' + \
    certificate_link("ISTQB Foundation Certification Examination",
                     "ISTQB",
                     "21st Mar' 2017",
                     "http://www.istqb.in/index.php/certified-tester/foundation-level", "Reg# 110964") + \
    certificate_link("Python Certification Training",
               "Edureka",
               "Dec'16-Feb'17",
               "https://www.edureka.co/my-certificate/0d74fa2c1a12a33be340ad3c0c6ec264", "AYMLVT4A") + \
    certificate("Symbian C++",
              "Cranes Varsity, Cranes Software International Limited",
              "Mar'07-May'07") + \
    certificate("Symbian OS Essentials",
               "Cranes Varsity, Cranes Software International Limited",
               "Jan'07-Mar'07") + \
    certificate("Embedded Systems Design",
               "Kiona software, Bangalore",
               "Dec'05-Apr'06")


def education(institution, certificate, duration, percentage):
    return \
        '''
        <div>
            <article><h6>''' + institution + " | " + certificate + ''' with ''' + percentage + '''%''' + '''</h6>
            </article>
            <article style="float:right;"> <h6>''' + duration + '''</h6>
            </article>
        </div>
        <!--hr-->
        '''

def educations():
    return \
        '''
        <br><h4>EDUCATION:</h4>''' + \
        education("ABIT Cuttack, Odisha",
                  "BE Computer Science and Engineering",
                  "2001-2005", "71") + \
        education("Council of Higher Secondary Education, Orissa",
                  "Higher Secondary Examination Certificate",
                  "1998-2000", "65") + \
        education("Board of secondary Education, Orissa",
                  "High school Certificate Examination ",
                  "1997-1998", "78")
def projects():
    return \
        '''
        <br>
        <h4>PROJECTS:</h4>
        <h5>Recent Projects</h5>
        <ul>
            <li>Test Automation framework development using python,xsd, JSON etc..</li >
            <li>Next generation service framework development (using Xtext and Xtend DSL development)</li >
            <li>Java plug-in development:
                C++ code generation for service specific Stub and Proxy component (Code generation for DBus introspection xml)
                Automatic generation of C++ adapter felicitating Interface test of the services running in the target</li>
            <li>QT/QML based HMI and application development:
                 HMI application displaying Navigation data, GPS data and CAN data
                 Home screen development for Infotainment Head Unit</li>
         </ul>
         <h5>Old Projects</h5>
         <ul>
            <li>Webkit based browser UI and view development using gtk+</li>
            <li>Media Player and Media Gallery application development using S60 and UIQ symbian-UI framework</li >
        </ul>
        '''


def personalDelaration():
    return \
        '''
        <h5>DECLARATION</h5>
        <p>I do hereby declare that the above information is true to the best of my knowledge.</p>
        '''

def htmlend():
    return \
        '''
            </body>
        </html>
        '''
contact_email = "mailto:mail.kalinga@gmail.com"
contact_name = "Kalinga Bhusan Ray"

def mycover(manager_name, company_name):
     hiring_manager = manager_name if manager_name else "Hiring Manager"
     org_name = company_name if company_name else "Organisation"
     str = u'''
        <body>
            <p> Dear {0},<br><br>
            &nbsp;&nbsp;&nbsp;&nbsp;I found you are in search for a dynamic and highly motivated Software Engineer for
            your company. The job description is so exciting and very much closely matching my experience and ambitions.
            With around 10 years of experience in IT, i am confident that i can step in and make immediate contribution
            to the project and valuable contribution to {1}'s continued success.<p>

            <p>&nbsp;&nbsp;&nbsp;&nbsp;As a software engineer at {1}, I can collaborate closely with Customers,
            and help junior team members with my knowledge and experience. In addition, I consider myself a flexible,
            always wanted to take responsibility, take ownership of core components. I consider myself a quick learner
            and have motivation towards learning new technologies and apply them in solving real world problems.<p>

            <p>&nbsp;&nbsp;&nbsp;&nbsp;I look forward to discuss further on details of this position. In the meantime,
            please take a look at my resume attached. Please feel free to contact for additional information
            required if any.
            <p><br>

            <p>Mit freundlichen Grüßen / Best regards,<br>
            Kalinga Bhusan Ray<br>
            +917795346374<br>
            </p>

        '''.format(hiring_manager, org_name).encode("utf-8")
     return  str

def skeleton():
    return \
        htmlstart(contact_name) \
        + pageheading() \
        + intro() \
        + technical() \
        + functional() \
        + keyresponsibilities() \
        + experiences() \
        + projects() \
        + certificates() \
        + educations() \
        + personalDelaration() \
        + footer(contact_email, contact_name,
                 datetime.datetime.today().strftime('%d %b %y %H:%M')) \
        + htmlend()

with open(html_file,'w+') as f:
    message = skeleton()

    f.write(message)

pdfkit.from_file(html_file, pdf_file)
