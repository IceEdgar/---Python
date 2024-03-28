import yaml
from module import Site
import pytest
import time

with open("testdata.yaml", 'r', encoding="utf-8") as f:
    testdata = yaml.safe_load(f)



def test_step1(site,selector_login, selector_password, selector_button, create_button, selector_error, status_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", selector_button)
    btn.click()
    err_lable = site.find_element("xpath", selector_error)
    assert err_lable.text == status_error








"""
css_selector = "span.mdc-text-field__ripple"
print(site.get_element_property("css", css_selector, "height"))

xpath = '//*[@id="login"]/div[3]/button/div'
print(site.get_element_property("xpath", xpath, "color"))"""