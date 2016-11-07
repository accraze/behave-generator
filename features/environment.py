import os
import shutil

def before_all(context):
  pass

def after_all(context):
  os.chdir(os.pardir)
  shutil.rmtree('tmp', ignore_errors=True) 
