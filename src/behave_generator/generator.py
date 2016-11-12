import os

class BehaveGenerator(object):

  environ_template = 'templates/environment_base.py'
  environ_file = 'features/environment.py'

  def build(self):
    """
    Creates the necessary components to start
    writing behave tests.
    """
    self._scaffold_dirs()
    self._create_env_file()

  def _scaffold_dirs(self):
    """
    Builds feature and feature/steps dirs
    which are required to run behave tests.
    """
    from subprocess import call
    call(["mkdir", "features"])
    call(["mkdir", "features/steps"])

  def _create_env_file(self):
    """
    Create an environment.py file
    and place it inside of feature dir
    """
    # with open("templates/environment_base.py") as env_template:
    #   with open("features/environment.py", 'w') as env_file:
    #     for line in env_template:
    #       env_file.write(line)
    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, self.environ_template)
    from subprocess import call
    call(["cp", DATA_PATH, self.environ_file])
