from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def up(action):
	action.perform()

def down(action):
	action.perform()
	
def left(action):
	action.perform()

def right(action):
	action.perform()
	
def actionTake(act,action1,action2,action3,action4) :
	if act == 1:
		up(action1)
	elif act == 2:
		down(action2)
	elif act == 3:
		left(action3)
	elif act == 4:
		right(action4)
