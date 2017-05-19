from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def up(actions):
	actions.key_down(Keys.ARROW_UP).send_keys("n").key_up(Keys.ARROW_UP).perform()

def left(actions):
	actions.key_down(Keys.ARROW_LEFT).send_keys("n").key_up(Keys.ARROW_LEFT).perform()

def right(actions):
	actions.key_down(Keys.ARROW_RIGHT).send_keys("n").key_up(Keys.ARROW_RIGHT).perform()
	
def down(actions):
	actions.key_down(Keys.ARROW_DOWN).send_keys("n").key_up(Keys.ARROW_DOWN).perform()
	
def actionTake(act,actions) :
	if act == 1:
		up(actions)
	elif act == 2:
		down(actions)
	elif act == 3:
		left(actions)
	elif act == 4:
		right(actions)