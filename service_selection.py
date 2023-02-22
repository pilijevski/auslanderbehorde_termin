import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configs import MAX_WAITING_TIME


def select_citizenship(driver, citizenship_id):
    citizenship = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "xi-sel-400")))
    time.sleep(1)
    citizenship_select = Select(citizenship)
    time.sleep(1)
    citizenship_select.select_by_value(citizenship_id)
    time.sleep(1)


def select_num_people(driver, num_people):
    num_people_field = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "xi-sel-422")))
    num_people_select = Select(num_people_field)
    num_people_select.select_by_value(num_people)


def select_live_in_berlin(driver, family_member):
    in_berlin = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "xi-sel-427")))
    in_berlin_select = Select(in_berlin)
    in_berlin_select.select_by_value(family_member)


def select_family_citizenship(driver, family_citizenship_id):
    citizenship = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, "xi-sel-428")))
    time.sleep(1)
    citizenship_select = Select(citizenship)
    time.sleep(1)
    citizenship_select.select_by_value(f'{family_citizenship_id}-0')


def select_residence_title(driver, citizenship_id):
    # TODO: Needs to be updated to be configurable for all titles
    time.sleep(1)
    residence_title = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.CLASS_NAME, f"kachel-{citizenship_id}-0-1")))
    residence_title.click()
    economic_activity = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.CLASS_NAME, f"accordion-{citizenship_id}-0-1-1")))
    economic_activity.click()
    blue_card = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.ID, f"SERVICEWAHL_EN{citizenship_id}-0-1-1-324659")))
    # https://stackoverflow.com/questions/18079765/how-to-find-parent-elements-by-python-webdriver
    # blue_card_div = blue_card.find_elements_by_xpath('..')
    blue_card.click()
