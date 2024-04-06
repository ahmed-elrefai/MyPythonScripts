import os
from ElreyOS import *
import shutil

supported_ext = {'.py':"python", ".java":"java", ".cpp":"c++"}
projects_dir = os.path.expanduser("~/Mycode/") # path relative to current user

def organize_dirs():
    """
    doing this steps for all project dirs:

    Step1: Choosing one of 3 projects states
    Step2: Expeling Unrelated content
    Step3: Redirecting Expeled content
    Step4: Grouping Projects to Done and InDev
    Step5: Repeat Each Startup.
    """
    
    # for dir in supported_ext.values():
        # state = find_dir_state(projects_dir + dir)
        # print(state)
        # filter_content(state, projects_dir + dir)
    state = find_dir_state("/home/elreyodev/Mycode/python/MyModules/dir")
    filter_content(state,"/home/elreyodev/Mycode/python/MyModules/dir")    

    # for dir in os.listdir(projects_dir):
    #     dir_type = find_dir_type(projects_dir + dir)
    #     if dir not in supported_ext.values() and dir_type:
    #         print(dir)
    #         shutil.move(projects_dir + dir, projects_dir + supported_ext[dir_type])
    #     elif dir not in supported_ext.values() and (dir_type == None or dir_type == "unknown"):
    #         if not os.path.exists(projects_dir + "other"):
    #             os.mkdir(projects_dir+ "other")
    #         print(dir)
    #         shutil.move(projects_dir + dir, projects_dir + "other")





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
        
        if os.path.exists(os.path.join(working_dir, "Done")) and os.path.exists(os.path.join(working_dir, "InDev")):
            print("we are in a language Directory.")
            return 2
        else:
            print("this is an 'InDev' Projects Directory")
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
        
    
def filter_content(state:int, working_dir="."):
    """filters content in 1 of 3 ways according to the state of file tree"""

    content = os.scandir(working_dir)
    parent_dir = os.path.dirname(working_dir)
    # meaning: dir content is a group of other directories 
    if state == 1:
        dirs_type = find_dirs_type(working_dir, supported_ext)
        print(dirs_type)
        for dir in content:
            if find_dir_type(dir) != dirs_type:
                shutil.move(dir.path, parent_dir)
                print("The directory: '",dir.name, "' has been moved to:", parent_dir)
        if parent_dir == "InDev":
            shutil.move()
        
    elif state == 2:
        for dir in content:
            if "-done" in dir.name:
                print("marking '",dir.name,"' as done")
                shutil.move(dir, os.path.join(working_dir , "Done"))
            elif "-done" not in dir.name and dir.name != "Done":
                shutil.move(dir, os.path.join(working_dir , "InDev"))
    elif state == 3:
        dir_type = find_dir_type(parent_dir)
        for file in content:
            file_type = "." + file.name.split(".")[1]
            if  file_type != dir_type:
                shutil.move(file, parent_dir)

    else:
        print("invalid state!")
        return
    


def startup():
    organize_dirs()


if __name__ == "__main__":
    startup()
