import time
import random
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from output import output

display = Display(visible=0, size=(300, 300))
display.start()
#driver = webdriver.Firefox(executable_path=r'C:\Users\RACH0_000\Downloads\geckodriver\geckodriver.exe') #do not delete geckodriver from downloads
driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(360, 480) #resize the window here before starting the game, this will also save tons of time while capturing screenshot
driver.get("https://dry-anchorage-61733.herokuapp.com/")

actions = ActionChains(driver)
#predefine all the actions here
action1 = actions.key_down(Keys.ARROW_UP).send_keys("n").key_up(Keys.ARROW_UP)
action2 = actions.key_down(Keys.ARROW_DOWN).send_keys("n").key_up(Keys.ARROW_DOWN)
action3 = actions.key_down(Keys.ARROW_LEFT).send_keys("n").key_up(Keys.ARROW_LEFT)
action4 = actions.key_down(Keys.ARROW_RIGHT).send_keys("n").key_up(Keys.ARROW_RIGHT)

element = driver.find_element_by_tag_name("canvas")
time.sleep(1)
actions.click(element).perform() #really need to first click on the canvas to do anything
#to time the while loop
t_end = time.time() + 40
count = 0
while time.time() < t_end:	
	act = random.randint(1,4)
	output(act,driver,action1,action2,action3,action4,count)	
	count = count+1
	
driver.close()
	
	
