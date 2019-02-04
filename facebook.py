#!/usr/bin/python

from selenium import webdriver
import getpass

#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#caps=DesiredCapabilities.FIREFOX.copy()
#caps['marionette'] = False

email = raw_input("please enter your email id")
print "please enter your passsword"
password = getpass.getpass()
driver=webdriver.Firefox()
driver.get("https://www.facebook.com")

email_id = driver.find_element_by_name("email")
email_id.send_keys(email)

passwd = driver.find_element_by_name("pass")
passwd.send_keys(password)

sub = driver.find_element_by_id("u_0_2").submit()
