import inspect
 
FILENAME = inspect.stack()[-1].filename

def goto(line):
  caller = inspect.stack()[1]
  with open(FILENAME, "r") as f:
    contents = "".join(f.readlines()[line-1:])
  
  exec(contents, caller.frame.f_globals)
