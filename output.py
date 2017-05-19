from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from actions import actionTake
import time
	
def output(action,actions,driver,count): #this is the function that should be called by the wrapper. 
	if action == 0:
		#screen = element.screenshot_as_png
		driver.save_screenshot('screenie_'+str(count)+'.png')
	else:
		start_time = time.time()
		actionTake(action,actions)
		#print("--- %s seconds ---" % (time.time() - start_time))		
		#screen = element.screenshot_as_png
		driver.save_screenshot('screenie_'+str(count)+'.png')
	#return screen