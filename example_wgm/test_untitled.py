# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class TestUntitled(BaseCase):
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  @pytest.mark.expected_failure
  def test_untitled(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1110, 808)
    self.driver.find_element(By.ID, "kw").send_keys("gggss")
    self.driver.find_element(By.ID, "su").click()
    element = self.driver.find_element(By.LINK_TEXT, "更多")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("gggsssss")
    self.driver.find_element(By.ID, "su").click()
    self.assert_element("FakeElement.DoesNotExist", timeout=0.4)
    self.driver.close()
  
