import os

@given(u'I am in an empty directory')
def step_impl(context):
  path = 'tmp'
  os.makedirs(path)
  os.chdir(path)

@when(u'I type the command "{command}"')
def step_impl(context, command):
  from subprocess import call
  if '--browser' in command:
    cmd = command.split(' ')[0]
    opt = command.split(' ')[1]
    call([cmd, opt])
  else:
    call([command])

@then(u'I should have a {dir_name} directory')
def step_impl(context, dir_name):
  assert os.path.isdir(dir_name)

@then(u'I should have a {file_name} file')
def step_impl(context, file_name):
  assert os.path.exists(os.path.join(os.getcwd(), file_name))

