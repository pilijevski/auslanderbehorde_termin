
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configs import MAX_WAITING_TIME, UserConfig
from selenium.webdriver.support import expected_conditions as EC
from pages import information_page, landing_page, service_selection
from utils import chime_n, create_driver

URL = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en"

OVERALL_RECEIVER = "petar.ilijevski@gmail.com"
SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_s' \
                     'ecret.json'
APPLICATION_NAME = "Desktop client 1"



def book_appointment(user_config: UserConfig):
    timeout = 60*18

    timeout_start = time.time()

    driver = create_driver(URL)
    landing_page(driver)
    information_page(driver)
    service_selection(driver, user_config)
    found_termin = False
    num_next_clicks = 0
    while time.time() < timeout_start + timeout:
        service_selection_next = WebDriverWait(driver, MAX_WAITING_TIME).until(
            EC.element_to_be_clickable((By.ID, "applicationForm:managedForm:proceed")))

        service_selection_next.click()
        print("Trying to Register for Appointment")

        print("Waiting 15 seconds for page to load")
        num_next_clicks += 1
        time.sleep(15)

        print("Checking if there's any appointments")
        try:
            date = driver.find_element_by_class_name('ui-datepicker')
        except Exception as e:
            date = None
        if date:
            print("SELECT APPOINTMENT!!!!")
            found_termin = True
            chime_n(10)
            time.sleep(2000)
            break

    if not found_termin:
        driver.close()




if __name__ == "__main__":
    user_config = UserConfig(citizenship="North Macedonia",number_applicants="2", family_member="yes", family_citizenship="North Macedonia")

    while True:
        found_termin = book_appointment(user_config)
        if found_termin:
            time.sleep(10000)

