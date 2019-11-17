# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import string
import pandas as pd
#from lxml import html
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(r"C:\Users\ajink\Desktop\web_scrapping\chromedriver")
driver.get("https://www.daad.de/deutschland/studienangebote/international-programmes/en/")
university_link =[]
#que=driver.find_element_by_xpath("//input[@name='q']")
que=driver.find_element_by_xpath('//*[@id="suggest"]')
que.send_keys("Electrical Engineering")
time.sleep(2)
que.send_keys(Keys.ARROW_DOWN)
#que.send_keys(Keys.ARROW_DOWN)
#time.sleep(2)

que.send_keys(Keys.RETURN)
time.sleep(10)
#driver.find_element_by_css_selector('#search-form-homepage > div.c-hero__content.no-gutters > div.col-12.col-lg-9.col-xl-7.mx-auto > div > div.c-search > form > div.row > div:nth-child(1) > div > fieldset > div > button > span').click()
driver.find_element_by_xpath('//*[@class="multiselect-selected-text"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="search-form-homepage"]/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/div/fieldset/div/ul/li[2]/label/input').click()
#driver.find_element_by_xpath('//*[@type="checkbox"]').click()......only for an MBA
time.sleep(2)
driver.find_element_by_xpath('//*[@id="filterFos"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="filterFos"]/option[4]').click()
time.sleep(2)
#select_fr.select_by_index(1).click()
#select_fr.select_by_index(0)
#que.send_keys(Keys.RETURN)
#que.send_keys(Keys.RETURN)
que.submit()
time.sleep(3)
'''
#------------------------------------------------------civil--------------
driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/button').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/ul/li[3]/label/input').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/ul/li[4]/label/input').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/ul/li[7]/label/input').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/ul/li[10]/label/input').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="filterSelects"]/div[3]/div[2]/button').click()
time.sleep(3)
#-----------------------------civil----------------------------------
'''
#Advance Search
driver.find_element_by_xpath('//*[@id="c-filterbar"]/div[2]/button/i').click()
time.sleep(4)
#Select the semester
driver.find_element_by_xpath('//*[@id="additionalFilterSelects"]/div/div[2]/div/div[2]/button/span').click()
time.sleep(4)
#Select the Summer semester
driver.find_element_by_xpath('//*[@id="additionalFilterSelects"]/div/div[2]/div/div[2]/ul/li[1]/label/input').click()
time.sleep(4)

'''
#Select the Winter Semester

driver.find_element_by_xpath('//*[@id="additionalFilterSelects"]/div/div[2]/div/div[2]/ul/li[2]/label/input').click()
time.sleep(4)
'''
while True:
    try:
        list_links = driver.find_elements_by_xpath('//*[@class="list-inline-item mr-0 js-course-detail-link"]')
        for i in list_links:
            university_link.append(i.get_attribute("href"))
            #print(university_link)
            #driver.find_elements_by_xpath('//*[@href="#overview"]').click()

        next_page_btn = driver.find_element_by_xpath('//*[@title="next"]')
        next_page_btn.click()
        time.sleep(4) 
    except (ElementNotInteractableException,ElementNotVisibleException) as e:
        print("Last page reached")
        break
'''        
for link in university_link:
    print(link)
    driver.get(link)
    driver.find_element_by_xpath('//*[@href="#overview"]').click()
    driver.find_element_by_xpath('//*[@href="#detail"]').click()
    driver.find_element_by_xpath('//*[@href="#costs"]').click()
    driver.find_element_by_xpath('//*[@href="#registration"]').click()
    driver.find_element_by_xpath('//*[@href="#services"]').click()
'''
driver.quit()
#print(university_link)

Name = []
Course = []
Course_website = []
Degree = []
Teaching_language = []
Languages = []
Programme_duration = []
Beginning = []
Application_deadline = []
Tuition_fees_per_semester_in_EUR = []
Additional_information_on_tuition_fees = []
Semester_contribution = []
Academic_Admission_Requirements = []
Language_requirements = []
i=0
for link in university_link:
#url = "https://www.daad.de/deutschland/studienangebote/international-programmes/en/detail/4536/"
    html = urlopen(link)
    time.sleep(3)
    soup = BeautifulSoup(html,'html.parser')
    Title_d = []
    Title = []
    Description = []
    
    for link in soup.findAll('a',attrs={'class':'btn btn-primary btn-block c-contact__link visitCourseWebsite'}):
        Course_website.append(link.get("href"))

    University_name = soup.find('h3', attrs={'class':'c-detail-header__subtitle'})
    Name_text = University_name.get_text()
    Ulines = (Uline.strip() for Uline in Name_text.splitlines())
    Uchunks = (Uphrase.strip() for Uline in Ulines for Uphrase in Uline.split("  "))
    Name_text = '\n'.join(Uchunk for Uchunk in Uchunks if Uchunk)
    Name.append(Name_text)
    #print(Name)
    
    University_course = soup.find('span', attrs={'class':'d-sm-none'})
    Course_text = University_course.get_text()
    Clines = (Cline.strip() for Cline in Course_text.splitlines())
    Cchunks = (Cphrase.strip() for Cline in Clines for Cphrase in Cline.split("  "))
    Course_text = '\n'.join(Cchunk for Cchunk in Cchunks if Cchunk)
    Course.append(Course_text)
            
    University_title = soup.find_all('dt', attrs={'class':'c-description-list__content'})
    for Tname in University_title :
        Ttext = Tname.get_text()
        # break into lines and remove leading and trailing space on each
        Tlines = (Tline.strip() for Tline in Ttext.splitlines())
        # break multi-headlines into a line each
        Tchunks = (Tphrase.strip() for Tline in Tlines for Tphrase in Tline.split("  "))
        # drop blank lines
        Ttext = '\n'.join(Tchunk for Tchunk in Tchunks if Tchunk)
        Title_d.append(list(Ttext.split("\n")))
    #print(Title)
    #print(len(Title))
    #print(Title.index(['Application deadline']))

    University_Description = soup.find_all('dd', attrs={'class':'c-description-list__content'})
    for Dname in University_Description :
        Dtext = Dname.get_text()
        # break into lines and remove leading and trailing space on each
        Dlines = (Dline.strip() for Dline in Dtext.splitlines())
        # break multi-headlines into a line each
        Dchunks = (Dphrase.strip() for Dline in Dlines for Dphrase in Dline.split("  "))
        # drop blank lines
        Dtext = '\n'.join(Dchunk for Dchunk in Dchunks if Dchunk)
        #Description += list(Dtext.split("\n"))
        Description.append(list(Dtext.split("\n")))
    #print(Description[1][0])
    #print(len(Description))
    #print(Description.index(['Master of Business Administration MBA']))
    #Title_d.sort()
    for elem in Title_d:
        if elem not in Title:
            Title.append(elem)
    for Title_element in Title:
        for Title_element_ in Title_element:
            if (Title_element_ == 'Degree'):
                Degree.append(Description[Title_d.index([Title_element_])][:])
                #print(Degree)
            
            elif (Title_element_ == 'Teaching language'):
                Teaching_language.append(Description[Title_d.index([Title_element_])][:])
                #print(Teaching_language)   

            elif (Title_element_ == 'Languages'):
                Languages.append(Description[Title_d.index([Title_element_])][:])
                #print(Languages)

            elif (Title_element_ == 'Programme duration'):
                Programme_duration.append(Description[Title_d.index([Title_element_])][:])
                #print(Programme_duration)
            
            elif (Title_element_ == 'Beginning'):
                Beginning.append(Description[Title_d.index([Title_element_])][:])
                #print(Beginning)
            
            elif (Title_element_ == 'Application deadline'):
                Application_deadline.append(Description[Title_d.index([Title_element_])][:])
                #print(Application_deadline)
            
            elif (Title_element_ == 'Tuition fees per semester in EUR'):
                Tuition_fees_per_semester_in_EUR.append(Description[Title_d.index([Title_element_])][:])
                #print(Tuition_fees_per_semester_in_EUR)
            
            #elif (Title_element_ == 'Additional information on tuition fees'):
              #  Additional_information_on_tuition_fees.append(Description[Title.index([Title_element_])][0])
                #print(Additional_information_on_tuition_fees)
            
            elif (Title_element_ == 'Semester contribution'):
                Semester_contribution.append(Description[Title_d.index([Title_element_])][:])
                #print(Semester_contribution)
            
            elif (Title_element_ == 'Academic Admission Requirements'):
                Academic_Admission_Requirements.append(Description[Title_d.index([Title_element_])][:])
                #print(Academic_Admission_Requirements)
            
            elif (Title_element_ == 'Language requirements'):
                Language_requirements.append(Description[Title_d.index([Title_element_])][:])
                #print(Language_requirements)
            
            else :
                break
    i=i+1
    print(i)
    
print('---start preparing Excel---')
mapped = list(zip(Name, Course, Course_website, Degree, Teaching_language, Languages, Programme_duration,
                          Beginning, Application_deadline, Tuition_fees_per_semester_in_EUR,
                          Semester_contribution,
                          Academic_Admission_Requirements, Language_requirements))
df = pd.DataFrame(mapped,columns=['Name', 'Course', 'Course_website', 'Degree', 'Teaching language','Languages','Programme duration','Beginning','Application deadline',
                           'Tuition fees per semester in EUR','Semester_contribution',
                           'Academic_Admission_Requirements','Language_requirements'])
#time.sleep(2)
df.to_excel('Electrical_Engineering.xlsx', index=False ,encoding='utf-8')
print('---done---')
