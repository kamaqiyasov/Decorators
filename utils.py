from datetime import datetime
from functools import wraps
import os


def logger(func_or_path=None):

    def __logger(old_function):
        # @wraps(old_function)
        def new_function(*args, **kwargs):
            
            if isinstance(func_or_path, str) or None:
                filepath = func_or_path
            else: 
                filepath = 'main.log'

            result = old_function(*args, **kwargs)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(os.path.join(os.getcwd(), filepath), 'a', encoding='utf-8') as file:
                file.write(f"{timestamp} {old_function.__name__} {args=} {kwargs=} {result}\n")        
            
            return result
        return new_function
    
    if callable(func_or_path):
        return __logger(func_or_path)
    else:
        return __logger