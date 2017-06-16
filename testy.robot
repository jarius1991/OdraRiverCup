*** Variables ***
${HOSTNAME}     127.0.0.1
${PORT}         8000
${SERVER}       http://${HOSTNAME}:${PORT}/
${BROWSER}      chrome
${EXECDIR}      H:\
${WRONGEMAIL}   krzysztow.jerzyna@szczecinianin
${WRONGMESSAGE}     Enter text here...
${CORRECTEMAIL}     krzysztow.jerzyna@szczecinianin.pl
${CORRECTMESSAGE}     Dajcie mi wiosłować!



*** Settings ***
Library         Selenium2Library  timeout=10  implicit_wait=0
Library         DjangoLibrary  manage=./manage.py
#${HOSTNAME}  ${PORT}
Library         OperatingSystem
Library         Collections
#Library         robotremoteserver
Suite Setup     Start Django and Open Browser
Suite Teardown  Stop Django and close Browser





*** Keywords ***
Start Django and Open Browser
  Start Django
  Open Browser  ${SERVER}  ${BROWSER}


Stop Django and Close Browser
  Close Browser
  #Stop Django

Cannot Send Message
    [Arguments]  ${email}   ${message}
    Wait Until Page Contains Element    id=nav-input
    Input Text  id=nav-input  ${email}
    Input Text  comment     ${message}
    Click Element   id=nav-input
    Click Element   id=comment
    Element Should Be Disabled  id=form_button

Send Message
    [Arguments]  ${email}   ${message}
    Wait Until Page Contains Element    id=nav-input
    Input Text  id=nav-input  ${email}
    Input Text  comment     ${message}
    Click Element   id=nav-input
    Click Element   id=comment
    Wait Until Page Contains Element    id=nav-input
    Element Should Be Enabled  id=form_button



*** Test Cases ***
Scenario: As a visitor I can visit mainpage
  Go To  ${SERVER}
  Maximize Browser Window
  Page Should Contain  Odra
#  Wait until page contains element  id=explanation
 # Page Should Contain  It worked!
 # Page Should Contain  Congratulations on your first Django-powered page.


Navbar Links: As a visitor I can visit all pages on website
    Go To  ${SERVER}
    Maximize Browser Window
    Click Link  /Harmonogram
    Click Link  /Partnerzy
    Click Link  /Kontakt
    Click Link  /Galeria
    Click Link  /Wyniki
    Click Link  /


Contact Fail: As a visitor I can't send message if email or message is invalid
    Go To  ${SERVER}Kontakt
    Cannot Send Message     ${EMPTY}    ${EMPTY}
    Cannot Send Message     ${CORRECTEMAIL}    ${EMPTY}
    Cannot Send Message     ${EMPTY}    ${CORRECTMESSAGE}
    Cannot Send Message     ${CORRECTEMAIL}     ${WRONGMESSAGE}
    Cannot Send Message     ${WRONGEMAIL}   ${CORRECTMESSAGE}


Contact Succeed: As a visitor I can send message if email and message is valid
    Go To   ${SERVER}
    Click Link  /Kontakt
    Send Message    ${CORRECTEMAIL}  ${CORRECTMESSAGE}


Translate Succeed:
  Wait Until Page Contains Element    id=polisz
  Click Link  id=polisz
  Page Should Contain   Aktualności
  Page Should Contain   Harmonogram
  Page Should Contain   Partnerzy
  Page Should Contain   Kontakt
  Page Should Contain   Galeria
  Page Should Contain   Wyniki
  Page Should Contain   Zaloguj
  Click Link  id=englisz
  Page Should Contain   News
  Page Should Contain   Schedule
  Page Should Contain   Partners
  Page Should Contain   Contact
  Page Should Contain   Gallery
  Page Should Contain   Scores
  Page Should Contain   Login
  Click Link  /






#http://robotframework.org/Selenium2Library/Selenium2Library.html