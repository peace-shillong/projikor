# #use mobile.facebook.com
# #disable javascript
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import json

def get_user_name_password():
    config_data = None
    with open('config.json') as json_file:
        config_data = json.load(json_file)

    return config_data["facebook"]
#main function
if __name__ == "__main__":
      print ("Web Scrap")
      mychrome_options = Options()
      mychrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
      chromedriver = r"C:\Users\HP\Downloads\scrap\chromedriver.exe"
      chrome = webdriver.Chrome(chromedriver,chrome_options=mychrome_options)
      chrome.maximize_window()
      #chrome = webdriver.ChromeOptions(mychrome_options)
      #chrome.get('http://stackoverflow.com/')
      chrome.get('https://mobile.facebook.com/')

      user_detail = get_user_name_password()

      #id in fb page
      username_element = chrome.find_element_by_id("email")
      password_element = chrome.find_element_by_id("pass")
      submit_btn_element = chrome.find_element_by_id("loginbutton")

      username_element.send_keys(user_detail["user"])
      password_element.send_keys(user_detail["pass"])
      submit_btn_element.click()
      wait = WebDriverWait(chrome, 5)

      print(chrome.title)

      # profile_name_list = driver_obj.find_elements_by_class_name("profileLink")
      # for profile_name in profile_name_list:
      #    print("profile_name: " + profile_name.text)

      chrome.get("https://www.facebook.com/groups/214914325234824/")

      profile_name_list = chrome.find_elements_by_class_name("profileLink")
      wait = WebDriverWait(chrome, 15)
      for profile_name in profile_name_list:
            print("profile_name: " + profile_name.text)
            print(profile_name.get_attribute("href"))

      #driver_obj.close()
      print("Web Scrapping Application Completed.")




