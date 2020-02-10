# use mobile.facebook.com
# disable javascript
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options


#CHROME WITHOUT JS
if __name__ == "__main__":
      print ("Web Scrap")
      mychrome_options = Options()
      mychrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
      chromedriver = r"C:\Users\HP\Downloads\scrap\chromedriver.exe"
      chrome = webdriver.Chrome(chromedriver,chrome_options=mychrome_options)
      chrome.get('https://mobile.facebook.com/')

      ## MOD now get more data

# WORKING 2 firefox
# if __name__ == "__main__":
#     print ("Web Scrap")
#     # profile = webdriver.FirefoxProfile()
#     # profile.set_preference("javascript.enabled", False);
#
#     foxdriver = r'C:\Users\HP\Downloads\scrap\geckodriver.exe'
#     browser_exe = 'C:\Program Files\Mozilla Firefox'
#     # WORKING 2
#     driver = webdriver.Firefox(executable_path=r'C:\Users\HP\Downloads\scrap\geckodriver.exe')
# #    driver.get("https://google.com")
#     driver.get("http://mobile.facebook.com")
#
#     print (driver.title)
#
#     # driver.close()
#     print ("Completed")

# DEMO FIRST PROGRAM
# from selenium import webdriver
#
# if __name__ == "__main__":
#     print ("Web Scrap")
#     chromedriver = r"C:\Users\HP\Downloads\scrap\chromedriver.exe"
#     driver=webdriver.Chrome(chromedriver)
#     driver.maximize_window()
#     driver.get("https://google.com")
#
#     print (driver.title)
#
#     #driver.close()
#     print ("Completed")
