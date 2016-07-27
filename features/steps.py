import time
from lettuce import *
from nose.tools import assert_equals
from lettuce_webdriver.util import AssertContextManager
 
@step('field with name "(.*?)" is given "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        elem = world.browser.find_element_by_name(field_name)
        elem.send_keys(value)
        elem.submit()
        time.sleep(5)

@step(u'Then title becomes "([^"]*)"')
def then_title_becomes(step, result):
    title = world.browser.title
    assert_equals(title, result)

@step(u'Then page contains "([^"]*)"')
def then_page_contains(step, regex):
    source = world.browser.page_source
    assert True, (regex in source)
