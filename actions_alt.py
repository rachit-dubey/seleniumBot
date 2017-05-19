from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def up(actions):
	actions.perform()

def left(actions):
	actions.perform()

def right(actions):
	actions.perform()
	
def down(actions):
	actions.perform()
	
def actionTake(act,actions1,actions2,actions3,actions4) :
	if act == 1:
		up(actions1)
	elif act == 2:
		down(actions2)
	elif act == 3:
		left(actions3)
	elif act == 4:
		right(actions4)