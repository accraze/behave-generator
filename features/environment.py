import os
import shutil

def before_all(context):
  pass

def after_scenario(context, scenario):
  os.chdir(os.pardir)
  shutil.rmtree('tmp', ignore_errors=True)

def after_all(context):
  os.chdir(os.pardir)
  shutil.rmtree('tmp', ignore_errors=True) 
