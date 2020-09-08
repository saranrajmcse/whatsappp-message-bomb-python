from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Hai!!!\Downloads\chromedriver_win32\chromedriver')
browser.get('https://web.whatsapp.com')


friend = input('Enter your friend name: ')
message = input('Enter your message: ')
Number = int(input('Enter number of messages to send :'))

searchbox = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(friend)
searchbox.send_keys(Keys.ENTER)

for i in range(Number):
  messagebox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
  messagebox.send_keys(message)
  messagebox.send_keys(Keys.ENTER)