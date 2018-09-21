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
    if (DE):
        return \
            '''
            <footer>
                <p align="middle">Das html / pdf wird von meinem Python-Projekt auf \
                 <a href="https://github.com/Kalinga/pythonLearning/tree/master/projects/cv_generator">GitHub</a> generiert um {2}
                </p>
                <!--p align="middle">Contact \
                 <a href={0}>{1}</a> \
                 with your questions, comments, and suggestions
                </p-->
            </footer>
            '''.format(mail, name, gen_time)

    else:
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
                        M: +49 15163587450<br>
                        E: <a href="mailto:mail.kalinga@gmail.com">mail.kalinga@gmail.com</a><br>
                        <a href=https://www.linkedin.com/in/kalinga-bhusan-ray-88505724/>LinkedIn</a>
                        <a href=https://github.com/Kalinga>GitHub</a><br>
                        Bergrat Mahr Strasse 10,<br> 98693 Ilmenau, <br> Deutschland
                    </address>
                </article>
                <article class="Container_article" id="rightMostImage">
                    <img src="../img/myimage.jpg" alt="Kalinga's photo">
                </article>
            </div >
        '''

def intro():
    if (DE):
        return \
            '''
            <h4>SPEZIALIST</h4>
            <p>Softwareentwickler mit viele jährige Erfahrungen in IT Industrie, spezialisierte in Software Applikation
            Entwicklung für Car Multimedia-Anwendung und Handheld-Geräte. Gearbeitet für 1.5 Jahren bei Robert Bosch
            Car Multimedia GmbH, Hildesheim. Ich habe mich sehr motiviert zu Deutsche lernen und habe B1 (CEFR)
            bestanden in Goethe, Bangalore. Zur Zeit wohne ich in Ilmenau, Deutschland und studiere Masters in Informatik,
            Research in Computer System and Engineering (RCSE) an der TU Ilmenau.</p>
            '''
    else:
        return \
            '''
            <h4>SPECIALIST</h4>
            <p>Software engineer with decade long experience in IT industry, specializing in software development
            for Car Multimedia and handheld devices. Wanted to broaden my technical area and found a new interest
            towards Data Aanalysis and Machine Learning. Possess strong motivation towards learning German language and
            completed B1 (CEFR) at Goethe, Bangalore. Currently living in Ilmenau, Germany and pursuing Masters in Research
            in Computer System and Engineering (RCSE, 3rd Semester) in TU Ilmenau.</p>
            '''


def technical():
    if(DE):
        return \
            '''
            <h4>Technische Domäne:</h4>
                <ul>
                    <li>Objektorientierte Anwendungs- und Framework-Entwicklung mit C, C ++</li>
                    <li>Domänenspezifische Sprache(DSL) Entwicklung mit Core Java, Xtend/Xtext</li>
                    <li>Integrationstest-Framework und Testfälle Entwicklung mit Python</li>
                    <li>HMI-Anwendung Entwicklung für Linux, Symbian, MeeGo Geräten</li>
                    <li>GUI Entwicklung mit QT, QML, gtk, UIQ, S60</li>
                    <li>Testgetriebene Entwicklung (TDD), Komponententest(JUnit, Google Test), Integrationstest</li>
                    <li>Agile Methoden, Scrum, Planung & Schätzung, CI(Jenkins)</li>
                    <!--li>Sound knowledge of productivity tools like puppet, vagrant</li-->
                    <li>Entwerfen mit UML, Enterprise Architect</li>
                    <li>Fundierte Kenntnisse von HTML, CSS, XML, Java Script</li>
                    <li>Git, ClearCase, Subversion,Eclipse, Carbide, CodeWarior etc..</li>
                    <li>Make, CMake, Boost Library</li>
                    <li>Fundierte Kenntnisse von Android, PHP, MySQL, Data Analysis and Machine Learning</li>
                </ul>
                <hr>
            '''
    else:
        return \
        '''
            <h4>Technical Domain:</h4>
                <ul>
                    <li>Object Oriented application and framework development using C, C++</li>
                    <li>Domain Specific Language (DSL) development using Core Java, Xtend/Xtext</li>
                    <li>Integration Test framework and test cases development using Python</li>
                    <li>HMI Application development for Linux, Symbian, MeeGo devices using QT, QML, gtk, UIQ, S60</li>
                    <li>TDD, Unit testing (JUnit, Google Test), Integration Testing</li>
                    <li>Agile methodologies, Scrum, Planning & Estimation, CI(Jenkins)</li>
                    <li>Sound knowledge of Android, PHP, MySQL, Data Analysis using Hadoop and Spark</li>
                    <!--li>Sound knowledge of productivity tools like puppet, vagrant</li-->
                    <li>Sound knowledge of HTML, CSS, XML, Java Script</li>
                    <li>Git, ClearCase, Subversion,Eclipse, Carbide, CodeWarior etc..</li>
                    <li>Make, CMake, Boost Library</li>
                </ul>
                <hr>
        '''

def functional():
    if (DE):
        return \
            '''
            <h4>Funktionsdomäne:</h4>
                    <ul>
                        <li>Car Multimedia Anwendungsentwicklung</li>
                        <li>Service-Framework-Entwicklung (mit DSL)</li>
                        <li>Framework-Entwicklung für die Interface Test Automation</li>
                        <li>Media Player und Mediengalerie</li>
                        <li>Webkit based web browser</li>
                        <li>Predictive Input-Methodenlösung</li>
                    </ul>
                    <hr>
            '''
    else:
        return \
            '''
            <h4>Functional Domain:</h4>
                    <ul>
                        <li>Data analysis using Hadoop, Spark, scala and Python</li>
                        <li>Car Multimedia Application development</li>
                        <li>Service framework development (Using DSL)</li>
                        <li>Media Player and Media Gallery</li>
                        <li>Webkit based web browser</li>
                    </ul>
                    <hr>
            '''

def keyresponsibilities():
    if (DE):
        return \
            '''
            <h4>Hauptverantwortlichkeiten:</h4>
            <ul>
                <li>Teilnahme an der Sprint-Planung (Agile) und Überprüfen</li>
                <li>Entwurf(mit UML) und Designprüfung</li>
                <li>Codierung mit (C, C++, Java, Python, PHP/Linux), code-überprüfen , Komponententests und Dokumentation.</li>
                <li>Verantwortlich für die feature Entwicklung von verschiedener Produkte.</li>
                <li>Testplan und Testautomatisierung</li>
            </ul>
            <hr>
            '''
    else:
        return \
            '''
            <h4>Key Responsibilities:</h4>
            <ul>
                <li>Participation in the Sprint Planning (Agile) and Review</li>
                <li>Design (using UML) and Design review</li>
                <li>Coding(C, C++, Java, Python, PHP/Linux), code review, unit testing and documentation.</li>
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
    if (DE):
        return \
            '''<h4>ERFAHRUNG:</h4>''' + \
            experience("Spezialist-Car Multimedia",
                       "Robert Bosch Engineering and Business Solutions, Bangalore",
                       "Dez'11-Sep' 17") + \
            experience("Senior-Software-Entwickler-R&D (Adaptxt)",
                       "Keypoint technology, Hyd",
                       "Mär'10-Dez'11") + \
            experience("Senior Software Ingenieur (Azingo Browser)",
                       "Azingo Soft Systems India PVT LTD, Hyd",
                       "Mai'09-Mär'10") + \
            experience("Software Ingenieur- (Sasken Media Player)",
                       "Sasken Communication Technologies, Bangalore",
                       "Dez'06-Mai'09") + \
            experience("MIS Exekutive",
                       "iSeva,E4E Pvt ltd,Bangalore",
                       "Apr'06-Dez'06")

    else:
        return \
        '''<h4>EXPERIENCE:</h4>''' + \
        experience("Working Student",
                   "Actian Germany GmbH, Ilmenau",
                   "Dec'17-Till Date") + \
        experience("Specialist-Car Multimedia",
                   "Robert Bosch Engineering and Business Solutions, Bangalore",
                   "Dec'11-Sep'17") + \
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
    if (DE):
        return \
            '''<h4>ZERTIFIZIERUNG:</h4>''' + \
            certificate_link("Prüfung Goethe-Zertifikat B1 ",
                             " Goethe-Instituts, Bangalore ",
                             "8th Aug' 2017",
                             "https://www.goethe.de/de/index.html", "PTN# 32934") + \
            certificate_link("ISTQB Foundation Zertifizierungsprüfung",
                             "ISTQB",
                             "21st Mär' 2017",
                             "http://www.istqb.in/index.php/certified-tester/foundation-level", "Reg# 110964") + \
            certificate_link("Python Zertifizierungstraining",
                             "Edureka",
                             "Dez'16-Feb'17",
                             "https://www.edureka.co/my-certificate/0d74fa2c1a12a33be340ad3c0c6ec264", "AYMLVT4A") + \
            certificate("Symbian C++",
                        "Cranes Varsity, Cranes Software International Limited",
                        "Mär'07-Mai'07") + \
            certificate("Symbian OS Essentials",
                        "Cranes Varsity, Cranes Software International Limited",
                        "Jan'07-Mär'07") + \
            certificate("Design eingebetteter Systeme",
                        "Kiona software, Bangalore",
                        "Dez'05-Apr'06")

    else:
        return \
        '''<h4>CERTIFICATION:</h4>''' + \
        certificate_link("Prüfung Goethe-Zertifikat B1 ",
                         " Goethe-Instituts, Bangalore ",
                         "8th Aug' 2017",
                         "https://www.goethe.de/de/index.html", "PTN# 32934") + \
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
    if (percentage < 5):
        '''
        <div>
            <article><h6>''' + institution + " | " + certificate + ''' with ''' + percentage + '''Grade''' + '''</h6>
            </article>
            <article style="float:right;"> <h6>''' + duration + '''</h6>
            </article>
        </div>
        <!--hr-->
        '''
    else:
        return \
            '''
            <div>
                <article><h6>''' + institution + " | " + certificate + '''</h6>
                </article>
                <article style="float:right;"> <h6>''' + duration + '''</h6>
                </article>
            </div>
            <!--hr-->
            '''

def educations():
    if (DE):
        return \
            '''
            <h4>AUSBILDUNG:</h4>''' + \
            education("TU Ilmenau, Deutschland",
                      "2nd Sem, Master Informatik(RCSE)",
                      "2017-Continue", "NA") + \
            education("ABIT Cuttack, Odisha",
                      "Bachelor in Informatik",
                      "2001-2005", "71") + \
            education("Council of Higher Secondary Education, Orissa",
                      "Höhere Sekundarstufe",
                      "1998-2000", "65") + \
            education("Board of secondary Education, Orissa",
                      "Abitur ",
                      "1997-1998", "78")
    else:
        return \
            '''
            <h4>EDUCATION:</h4>''' + \
            education("TU Ilmenau, Germany",
                      "3rd Sem, Master Research in Computer System and Engineering",
                      "2017-Continue", "NA") + \
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
    if (DE):
        return \
            '''
            <h4>PROJEKTE:</h4>
            <h5>Letzte Projekte</h5>
            <ul>
                <li>Next-Generation-Service-Framework-Entwicklung (mit Xtext und Xtend DSL-Entwicklung)</li >
                <li>Testautomatisierung Framework-Entwicklung mit Python, xsd, JSON usw.</li >
                <li>Java-Plugin-Entwicklung:
                    C++ code generation für Service-spezifisch Stub and Proxy Komponente</li>
                <li>QT / QML basierte HMI und Anwendungsentwicklung:
                     HMI-Anwendung zur Anzeige von Navigationsdaten, GPS-Daten und CAN-Daten
                     Home-Screen-Entwicklung für Infotainment Head Unit</li>
             </ul>
             <h5>Alte Projekte</h5>
             <ul>
                <li>Webkit-basierte Browser-Benutzeroberfläche und Ansichtsentwicklung mit gtk +</li>
                <li>Entwicklung von Media Player- und Media Gallery-Anwendungen mithilfe des S60- und UIQ-Symbian-UI-Frameworks</li >
            </ul>
            '''

    else:
        return \
            '''
            <h4>PROJECTS:</h4>
            <h5>Recent Projects</h5>
            <ul>
                <li>Solving DataLake problem using VectorH (Actian product on Hadoop)</li >
                <li>Analysis of GDELT data using Apache Spark </li>
                <li>TF-IDF analysis of wikipedia data (given stop word data) and clustering</li>
                <li>Analysis of Geo-spatial data using GDELT and OpenStreetMap.org dataset using STARK framework</li>
                <li>Next generation service framework development (using Xtext and Xtend DSL development)</li >
                <li>Test Automation framework development using python,xsd, JSON etc..</li >
                <li>Java plug-in development:
                    C++ code generation for service specific Stub and Proxy component (Code generation for DBus introspection xml)
                    Automatic generation of C++ adapter felicitating Interface test of the services running in the target</li>

             </ul>
             <h5>Old Projects</h5>
             <ul>
                <li>QT/QML based HMI and application development</li>
                <li>Webkit based browser UI and view development using gtk+</li>
                <li>Media Player and Media Gallery application development using S60 and UIQ symbian-UI framework</li >
            </ul>
            '''

def personal():
    if (DE):
        return \
            '''
            <h5>PERSÖNLICHE DETAILS</h5>
            <table>
              <tr>
                <td>Geburtsdatum</td>
                <td>02 Juni 1983</td>
              </tr>
              <tr>
                <td>Familienstand</td>
                <td>Verheiratet</td>
              </tr>
              <tr>
                <td>Bekannte Sprachen</td>
                <td>Englisch, Hindi, Oriya, Deutsche(B1)</td>
              </tr>
              <tr>
                <td>Passnummer</td>
                <td>G6513632</td>
              </tr>
            </table>
            '''
    else:
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
    if (DE):
        return \
            '''
            <h6>ERKLÄRUNG</h6>
            <p>Ich erkläre hiermit, dass die obigen Informationen nach meinem besten Wissen wahr sind.</p>
            '''

    else:
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
            your company to work in Data Science domain . The job description is so exciting and very much closely
            matches to my area of interest. With a Bachelor’s degree in Computer Science and decade long hands-on
            experience using programming languages such as C, C++, Java, Python on Linux platform to create and
            implement highly sophisticated software applications for embedded devices such as handheld devices
            and head units mounted in car dashboard; i found a new interest in the area of data analysis and wish
            to broaden my area expertise. Currently i am pursuing "Research in Computer & Systems Engineering (RCSE)";
            a Masters programme at TU, Ilmenau, Germany. I am confident that I can step in and make immediate contribution to
            the project and valuable contribution to {1}'s continued success and hone my skill as well.<p>&nbsp;&nbsp;&nbsp;&nbsp; I enjoy being challenged and working on projects that require me to work outside my comfort
            and knowledge set, as continuing to learn new languages and development techniques are important to me,
            and I consider myself a quick learner. In addition,I consider myself a flexible, always wanted to take
            responsibility, take ownership of core components.</p>

            <p>Few of my skills that I would like to highlight here, that enable me to contribute to the success of the project
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
            +49 15163587450| <a href="mailto:mail.kalinga@gmail.com">mail.kalinga@gmail.com</a>
            </p>

        '''.format(hiring_manager, org_name)
    return str

def myAddress():
    return  '''
        Kalinga Bhusan Ray <br>
        Bergrat Mahr Strasse 10 <br>
        98693, Ilmenau <br>
        Deutschland<br>
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