import os


class BehaveGenerator(object):

    browser_template = 'templates/browser.py'
    browser_file = 'features/browser.py'
    environ_template = 'templates/environment_base.py'
    environ_file = 'features/environment.py'

    def __init__(self, browser):
        self.browser = browser.lower() if browser else None

    def build(self):
        """
        Creates the necessary components to start
        writing behave tests.
        """
        self._scaffold_dirs()
        if self.browser:
            self._build_browser()
        self._create_env_file()

    def _scaffold_dirs(self):
        """
        Builds feature and feature/steps dirs
        which are required to run behave tests.
        """
        from subprocess import call
        call(["mkdir", "features"])
        call(["mkdir", "features/steps"])

    def _build_browser(self):
        """
        Create a browser page object
        file inside features dir.
        """
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, self.browser_template)
        with open(DATA_PATH) as browser_template:
            with open(self.browser_file, 'w') as browser_file:
                for line in browser_template:
                    self._write_browser_config(line, browser_file)

    def _write_browser_config(self, line, writefile):
        """
        Handle configuring the specified Browser
        in our browser template and write the template to
        features/browser.py
        """
        if "# insert browser here" in line:
            browser_cfg = {
                "android": "  driver = webdriver.Android()\n",
                "blackberry": "  driver = webdriver.Blackberry()\n",
                "chrome": "  driver = webdriver.Chrome()\n",
                "edge": "  driver = webdriver.Edge()\n",
                "firefox": "  driver = webdriver.Firefox()\n",
                "ie": "  driver = webdriver.Ie()\n",
                "opera": "  driver = webdrive.Opera()\n",
                "phantomjs": "  driver = webdrive.PhantomJS()\n",
                "opera": "  driver = webdrive.Opera()\n",
                "remote": "  driver = webdriver.Remote()\n",
                "safari": "  driver = webdriver.Safari()\n"
            }
            browser_line = browser_cfg.get(self.browser)
            if not browser_line:
                raise Exception("Invalid Browser Name")
            writefile.write(browser_line)
        else:
            writefile.write(line)

    def _create_env_file(self):
        """
        Create an environment.py file
        and place it inside of feature dir
        """
        status = {'previous_line': '', 'line': ''}
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, self.environ_template)
        with open(DATA_PATH) as env_template:
            with open(self.environ_file, 'w') as env_file:
                if self.browser:
                    env_file.write('from browser import Browser\n')
                for line in env_template:
                    status['line'] = line
                    if self.browser:
                        self._write_browser_env(status, env_file)
                    else:
                        env_file.write(line)
                    status['previous_line'] = line

    def _write_browser_env(self, status, writefile):
        """
        Handle defining and cllsing browser statements
        in features/environment.py
        """
        if 'pass' in status['line']:
            if 'before_all' in status['previous_line']:
                browser_line = '    context.browser = Browser()\n'
                writefile.write(browser_line)
            elif 'after_all' in status['previous_line']:
                browser_line = '    context.browser.close()'
                writefile.write(browser_line)
        else:
            writefile.write(status['line'])
