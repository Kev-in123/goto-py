import inspect
 
FILENAME = inspect.stack()[-1].filename

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def goto(line):
  caller = inspect.stack()[1]
  with open(FILENAME, "r") as f:
    contents = "".join(f.readlines()[line-1:])
  exec(contents, caller.frame.f_globals)
