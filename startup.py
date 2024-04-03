import os
from ElreyOS import *

projects_dir = os.path.expanduser("~/Mycode/python/MyModules") # path relative to current user
supported_ext = {"python":'.py', "java":".java", "c++":".cpp"}

def organize_dirs():
    """
    doing this steps for all project dirs:

    Step1: Choosing one of 3 projects states
    Step2: Expeling Unrelated content
    Step3: Redirecting Expeled content
    Step4: Grouping Projects to Done and InDev
    Step5: Repeat Each Startup.
    """
    state = find_dir_state(projects_dir)
    print(state)
    filter_content(state, projects_dir)




def find_dir_state(working_dir=".") -> int:
    """returns the state of the working dir, according to file structure
    if it consists of dirs only:
        State 1: the working dir has list of projects (dirs that has types)
        State 2: the working dir has two directories, Done and InDev. (check by names)

    if it consists of files only:
        State 3: the working dir has different file types
        returns -1 at empty working directory or single files type (no need to organize)
        """
    if find_dir_type(working_dir) == None:
        content = os.listdir(working_dir)
        if len(content) == 0:
            print("Empty Working Directory.")
            return -1
        elif len(content) == 2:
            if ["Done", "InDev"] in content:
                print("we are in a language Directory.")
                return 2
            print("this is an 'InDev' Projects Directory with 2 Projects")
            return 1
        else:
            print("this is an 'InDev' Projects Directory multiple Projects")
            return 1

    elif find_dir_type(working_dir):
        print("we found files of type:" + find_dir_type(working_dir))
        if is_pure_dir(working_dir):
            if not is_pure_dir(working_dir, True):
                print("we found subdirs, non-dir files will be considered as In Development")
                return 3
            else:
                print("this is a completely pure directory, nothing to organize!")
                return -1
        else:
            print("found multiple file types!, time to organize!")
            return 3
        
    
def filter_content(state:int, dir="."):
    """filters content in 1 of 3 ways according to the state of file tree"""
    
    




def startup():
    organize_dirs()


if __name__ == "__main__":
    startup()
