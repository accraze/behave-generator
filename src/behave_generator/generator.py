
class BehaveGenerator(object):

  def build(self):
    """
    Creates the necessary components to start
    writing behave tests.
    """
    self._scaffold_dirs()

  def _scaffold_dirs(self):
    """
    Build feature and feature/steps dirs
    which are required to run behave tests.
    """
    from subprocess import call
    call(["mkdir", "features"])
    call(["mkdir", "features/steps"])

