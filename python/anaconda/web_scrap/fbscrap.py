# #use mobile.facebook.com
# #disable javascript
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import json

def get_user_name_password():
    config_data = None
    with open('data.json') as json_file:
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
      username_element = chrome.find_element_by_id("m_login_email")#email
      password_element = chrome.find_element_by_id("m_login_password")
      submit_btn_element = chrome.find_element_by_name("login")

      username_element.send_keys(user_detail["user"])
      password_element.send_keys(user_detail["pass"])
      submit_btn_element.click()
      wait = WebDriverWait(chrome, 5)

      print(chrome.title)

      # profile_name_list = driver_obj.find_elements_by_class_name("profileLink")
      # for profile_name in profile_name_list:
      #    print("profile_name: " + profile_name.text)
      #mobile scrap group
      #1. Inkscape
      #chrome.get("https://m.facebook.com/groups/2675326577?refid=46&__xts__%5B0%5D=12.%7B%22unit_id_click_type%22%3A%22graph_search_results_item_tapped%22%2C%22click_type%22%3A%22result%22%2C%22module_id%22%3A1%2C%22result_id%22%3A2675326577%2C%22session_id%22%3A%22e7024e4c599eb5b833dba4f9f7f2d7af%22%2C%22module_role%22%3A%22ENTITY_GROUPS%22%2C%22unit_id%22%3A%22browse_rl%3Ac7da41bc-d0cd-4365-9ccf-d5e908fc3ae3%22%2C%22browse_result_type%22%3A%22browse_type_group%22%2C%22unit_id_result_id%22%3A2675326577%2C%22module_result_position%22%3A0%7D") #214914325234824

      # 2. Shillong Taffic Police
      chrome.get("https://m.facebook.com/TrafficPoliceShillong/?_rdc=1&_rdr&refsrc=https%3A%2F%2Fmobile.facebook.com%2FTrafficPoliceShillong%2F")

      profile_name_list = chrome.find_elements_by_class_name("_5msj")
      wait = WebDriverWait(chrome, 15)
      #for profile_name in profile_name_list:
       #     print("text: " + profile_name.text)
          #  print(profile_name.get_attribute("href"))

      paragraphs = chrome.find_element_by_tag_name("p").text
      #for paragraph in paragraphs:
        #print("paragraph "+paragraph)
      print("What is "+paragraphs)
      chrome.get_screenshot_as_file("F:\\peace\\fb.png")
      #chrome.close()
      print("Web Scrapping Application Completed.")




