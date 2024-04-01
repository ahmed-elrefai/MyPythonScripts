import os
import ElreyOS

projects_file = "~/Mycode/python"


def clean_system():
    os.chdir(os.path.expanduser(projects_file))  # Step1: setting clean directory
    
    # Step2: look for non-python dirs
    content = os.scandir(".")
    
    parent_dest_path = os.path.dirname(os.path.expanduser(projects_file))
    
    for obj in content:
        if obj.is_dir():
            dir_type = ElreyOS.find_dir_type(obj.path)
            
            if dir_type != ".py":
                dest_path = os.path.join(parent_dest_path, obj.name)
                
                if dir_type == ".cpp":
                    print(f"- dir: {obj.name}\n of type: '.cpp' does not belong here")
                
                elif ElreyOS.is_pure_dir(obj.path):
                    print(f"- dir: {obj.name}\n of type: '{dir_type}' does not belong here")
                


def startup():
    clean_system()


if __name__ == "__main__":
    startup()
