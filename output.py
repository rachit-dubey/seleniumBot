from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import io

from PIL import Image

from actions import actionTake
import time
	
def output(action,driver,action1,action2,action3,action4,count): #this is the function that should be called by the wrapper. 
	if action == 0:
		screen = driver.get_screenshot_as_png()
		img = Image.open(io.BytesIO(screen))
		img = img.resize((42,42))
		#img.save('screenie_'+str(count)+'.png')
		#driver.save_screenshot('screenie_'+str(count)+'.png')
	else:
		#start_time = time.time()
		actionTake(action,action1,action2,action3,action4)
		screen = driver.get_screenshot_as_png()
		img = Image.open(io.BytesIO(screen))
		img = img.resize((42,42))
		#img.save('screenie_'+str(count)+'.png')
		#driver.save_screenshot('screenie_'+str(count)+'.png')
		#print("--- %s seconds ---" % (time.time() - start_time))

	return img
