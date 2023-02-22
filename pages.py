import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configs import MAX_WAITING_TIME, UserConfig
from service_selection import select_citizenship, select_family_citizenship, select_live_in_berlin, select_num_people, \
    select_residence_title


def landing_page(driver):
    book_appt = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Book Appointment')]")))
    time.sleep(1)
    book_appt.click()


def information_page(driver):
    # https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable
    time.sleep(3)
    # Agree to terms and conditions
    agree = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "xi-cb-1")))
    agree.click()
    # Click net
    next = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "applicationForm:managedForm:proceed")))
    next.click()





def service_selection(driver, user_config: UserConfig):
    select_citizenship(driver, user_config.citizenship_id)

    select_num_people(driver, user_config.number_applicants)

    select_live_in_berlin(driver, user_config.family_member)

    if user_config.family_member == "1":
        select_family_citizenship(driver, user_config.family_citizenship_id)

    select_residence_title(driver, user_config.citizenship_id)
