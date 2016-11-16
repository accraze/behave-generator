from selenium import webdriver


class Browser(object):

  base_url = 'http://localhost:8080'

  # insert browser here
  driver.implicitly_wait(10)
  driver.set_window_size(800, 800)
  driver.set_window_position(400, 10)


  def find_element(self, *locator):
    return self.driver.find_element(*locator)

  def close(self):
    self.driver.quit()

  def visit(self, location=''):
    url = self.base_url + location
    self.driver.get(url)

  def get_title(self):
    return self.driver.title

  def get_current_url(self):
    return self.driver.current_url

  def go_back(self):
    self.driver.back()
