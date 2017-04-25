# coding=utf-8
import os

import datetime
import pdfkit
from input import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if not os.path.exists("../gen"):
    os.mkdir("../gen")

def footer(mail, name, gen_time):
    return \
        '''
        <footer>
            <p align="middle">The html/pdf is generated by my python project hosted on \
             <a href="https://github.com/Kalinga/pythonLearning/tree/master/projects/cv_generator">GitHub</a> at {2}
            </p>
            <!--p align="middle">Contact \
             <a href={0}>{1}</a> \
             with your questions, comments, and suggestions
            </p-->
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
        <h4>SPECIALIST</h4>
        <p>Software engineer with decade long experience in IT industry, specializing in software application development
        for Car Multimedia application and handheld devices. 1.5yrs of working and living experience in Hildesheim,
        Germany. Possess strong motivation towards learning German language and have completed A2 (Deutsche Sprache)</p>
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
                <li>GUI development using QT, QML, gtk, UIQ, S60</li>
                <li>Sound knowledge of HTML, CSS, XML, Java Script</li>
                <li>Git, ClearCase, Subversion,Eclipse, Carbide, CodeWarior etc..</li>
                <li>Make, CMake, Boost Library</li>
                <li>TDD, Unit testing (JUnit, Google Test), Integration Testing</li>
                <li>Agile methodologies, Scrum, Planning & Estimation, CI(Jenkins)</li>
                <!--li>Sound knowledge of productivity tools like puppet, vagrant</li-->
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
                    <li>Framework development for Interface Test Automation</li>
                    <li>Media Player and Media Gallery</li>
                    <li>Webkit based web browser</li>
                    <li>Predictive Input method solution</li>
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
            <li>Responsible for feature development of various product.</li>
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
        <h4>EDUCATION:</h4>''' + \
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
        <h4>PROJECTS:</h4>
        <h5>Recent Projects</h5>
        <ul>
            <li>Next generation service framework development (using Xtext and Xtend DSL development)</li >
            <li>Test Automation framework development using python,xsd, JSON etc..</li >
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


def personal():
    return \
        '''
        <h5>PERSONAL DETAILS</h5>
        <table>
          <tr>
            <td>Date of Birth</td>
            <td>02 June 1983</td>
          </tr>
          <tr>
            <td>Marital Status</td>
            <td>Married</td>
          </tr>
          <tr>
            <td>Languages Known</td>
            <td>English, Hindi and Oriya, German(A2)</td>
          </tr>
          <tr>
            <td>Passport Number</td>
            <td>G6513632</td>
          </tr>
        </table>
        '''
def personalDelaration():
    return \
        '''
        <h6>DECLARATION</h6>
        <p>I do hereby declare that the above information is true to the best of my knowledge.</p>
        '''

def htmlend():
    return \
        '''
            </body>
        </html>
        '''

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

def mycover(manager_name, company_name):
    hiring_manager = manager_name if manager_name else "Hiring Manager"
    org_name = company_name if company_name else "Organisation"
    str = u'''
        <body>
            <p> Dear {0},<br>
            &nbsp;&nbsp;&nbsp;&nbsp;I found you are in search for a dynamic and highly motivated Software Engineer for
            your company. The job description is so exciting and very much closely matching my experience and ambitions.
            With a Bachelor’s degree in Computer Science and hands-on experience using programming languages such as
            C, C++, Java, Python on Linux platform to create and implement highly sophisticated software applications
            for embedded devices such as handheld devices and head units mounted in car dashboard; I am confident that I
            can step in and make immediate contribution to the project and valuable contribution to {1}'s continued success.</p>

            <p>&nbsp;&nbsp;&nbsp;&nbsp;As a software engineer at {1}, I can collaborate closely with Customers,
            and help junior team members with my knowledge and experience. I enjoy being challenged and working on
            projects that require me to work outside my comfort and knowledge set, as continuing to learn new languages
            and development techniques are important to me, and I consider myself a quick learner. In addition,
            I consider myself a flexible, always wanted to take responsibility, take ownership of core components.</p>

            <p>Few of my skills that I would like to highlight here, that enable me to contribute to the success of the company
            <ul>
                <li>Complete understanding of SDLC (Software development life cycle)</li>
                <li>Highly skilled in designing, testing, and developing software for resource constraint systems</li>
                <li>Thorough understanding of Object Oriented Programming, data structures and algorithms</li>
                <li>Knowledgeable of agile development, best practices, clean code approach</li>
                <li>Hands-on software debugging experience</li>
                <li>Proper documentation, maintainable software development, eagle eye for quality</li>
                </ul>
             </p>

            <p>&nbsp;&nbsp;&nbsp;&nbsp;I’ve attached a copy of my resume that details my projects and experience in
            software development. Thank you for your time and consideration. I look forward to speaking with you about
            this opportunity.</p><br>
            <p>Mit freundlichen Grüßen / Best regards,<br>
            Kalinga Bhusan Ray<br>
            +91 7795346374 | <a href="mailto:mail.kalinga@gmail.com">mail.kalinga@gmail.com</a>
            </p>

        '''.format(hiring_manager, org_name)
    return str

def myAddress():
    return  '''
        Kalinga Bhusan Ray <br>
        #1, Kamakshi Nilaya <br>
        1st Cross, 3rd Main Road <br>
        Pukhraj Layout, Adugodi <br>
        Bangalore, Karnataka, India <br>
        PIN: 560030 <br>
        <hr>
    '''

def companyAddress():

    return  \
        company_long_name + '''<br>''' + company_address + '''<br>''' + \
        company_zip_town + '''<br>'''  + company_state_country + '''<br>''' + \
        '''Dt. ''' +  datetime.datetime.today().strftime('%d %b %y') + '''<hr>'''



def cover_page():
    return \
        htmlstart(contact_name) + \
        myAddress() + \
        companyAddress() +\
        mycover(manager_name, company_name) + \
        htmlend()


with open(cover,'w+') as f:
    message = cover_page()
    f.write(message)

pdfkit.from_file(html_file, pdf_file, cover=cover, cover_first=True)