from functools import wraps

def log_activity(func):
    @wraps(func)
    def warapper(*args,**kwargs):
        print(f"🍉Calling: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return warapper

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")

brew_chai("Masala")