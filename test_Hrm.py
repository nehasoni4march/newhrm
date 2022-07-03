from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


def test_login1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.NAME, "FirstName").send_keys("Neha")
    time.sleep(1)
    driver.find_element(By.NAME, "LastName").send_keys("Soni")
    time.sleep(1)
    driver.find_element(By.NAME, "Email").send_keys("nehasoni4mrch@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, "Contact").send_keys("62665961849")
    time.sleep(1)

    countryid = driver.find_element(By.NAME, "Country")
    Select(countryid).select_by_visible_text("India")
    time.sleep(5)


def test_menu2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()

    time.sleep(5)
    driver.quit()


def test_company3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "About Us").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Executive Profile").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Press Releases").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "News Articles").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Company").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Careers").click()

    time.sleep(1)
    driver.quit()


def test_Resources4():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Resources").click()
    print("Resources clicked")
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "A Guide to Choosing the Best:").click()
    time.sleep(1)
    print("A Guide to Choosing the Best clicked")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Building a Happier Workforce:").click()
    time.sleep(1)
    print("Building a Happier Workforce: clicked")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Data-Driven Decision-Making").click()
    time.sleep(1)
    print("Data-Driven Decision-Making clicked")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "More eBooks").click()
    time.sleep(1)
    print("More eBooks")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "Starter Overview (Open Source)").click()
    time.sleep(1)
    print("Starter Overview (Open Source) clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "Advanced Overview (Short)").click()
    time.sleep(1)
    print("Advanced Overview (Short) clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "Advanced Overview (Long)").click()
    time.sleep(1)
    print("Advanced Overview (Long) clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "OrangeHRM ROI").click()
    time.sleep(1)
    print("OrangeHRM ROI clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.PARTIAL_LINK_TEXT, "How can free HR management software").click()
    time.sleep(1)
    print("How can free HR management software clicked")

    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "How can an HRIS help retain the best talent?").click()
    time.sleep(1)
    print("How can an HRIS help retain the best talent? clicked")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "More Topics").click()
    time.sleep(1)
    print("More Topics clicked")
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "Data Security Promise").click()
    time.sleep(1)
    print("Data Security Promise clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "Starter Forum (Open Source)").click()
    time.sleep(1)
    print("Starter Forum (Open Source) clicked")
    driver.back()
    driver.find_element(By.LINK_TEXT, "Resources").click()
    time.sleep(1)
    print("Resources clicked")
    driver.find_element(By.LINK_TEXT, "OrangeHRM API").click()
    time.sleep(1)
    print("OrangeHRM API clicked")
    driver.back()

    driver.quit()


def test_platform5():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "HR Administration").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Employee Management").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Reporting & Analytics").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Recruitment (ATS)").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Onboarding").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "PTO / Leave Management").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Time Tracking").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Payroll Connector").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Performance Management").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Career Development").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Platform").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Training (LMS)").click()
    time.sleep(1)

    driver.quit()


def test_WhyOrangeHRM6():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Case Studies").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Testimonials").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "HR Manager").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "C-Suite").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Recruiter").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "IT Manager").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Partner Programs").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Our Partners").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "HR for All").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "CS & Support").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Customizations").click()

    time.sleep(1)
    driver.quit()


def test_Contactsales7():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="header-navbar"]/ul[3]/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.NAME, "FullName").send_keys("Neha Soni")
    time.sleep(1)
    driver.find_element(By.NAME, "CompanyName").send_keys("Spanidea")
    time.sleep(1)
    driver.find_element(By.NAME, "JobTitle").send_keys("Associate software engineer")
    time.sleep(1)
    driver.find_element(By.NAME, "Contact").send_keys("987654321")
    time.sleep(1)
    driver.find_element(By.NAME, "Email").send_keys("nehasoni4march@gmail.com")
    time.sleep(1)
    noofemployee = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
    Select(noofemployee).select_by_visible_text("101 - 150")

    time.sleep(1)
    driver.quit()


    

