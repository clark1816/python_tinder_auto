# import module
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pickupline

# Create object
driver = webdriver.Chrome()
  
# Assign URL
url = "https://www.tinder.com/"

def tinder_bot():
# Opening first url
    driver.get(url)

    sleep(2)
    #iaccept = driver.find_element('/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
    login = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    login.click()
    sleep(2)
    #/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]
    continue_with_number = driver.find_element('xpath','/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]')
    continue_with_number.click()

    t = input("Enter the time in seconds you think it will take you to log in: ")
    ##put code for timer here 
    countdown(int(t))


def auto_right_swipe():
    #will be auto swiping right to make this very simple thanks to Internet Made Code
    #get the xpath of the full doc 
    doc = driver.find_element('xpath', '/html/body')
    doc.send_keys(Keys.ARROW_RIGHT)
    print('auto swiping')

def swipe():
    while True:
        sleep(2)
        auto_right_swipe()

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		sleep(1)
		t -= 1
	
	print('Fire in the hole!!')

def get_matches():
    match_profiles = driver.find_elements('class name', 'matchListItem')
    print(len(match_profiles))
    message_links = []

    for profile in match_profiles:
        if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
            continue
        message_links.append(profile.get_attribute('href'))
    return message_links 
    
     

def get_list_of_matches():
    links = get_matches()  
    for x in range(len(links)):
        send_message(x,links)  # type: ignore

def send_message(x,links):
    driver.get(links[x])
    sleep(2)
    text_area = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
    
    print(x)   
    text_area.send_keys(pickupline.pick_up_lines[x])
    text_area.send_keys(Keys.ENTER)
    sleep(2) 




tinder_bot()

#uncomment the below line if you want to auto swipe.
#swipe()

#once you have matches you must message them these defs will do that 
get_matches()
get_list_of_matches()
send_message()  # type: ignore