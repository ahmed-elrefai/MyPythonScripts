import os

def files_with_extension(ext, dir='.') -> list[str]:
    """returns all the files that end with ext
       for instance: '.py'"""
    content = os.listdir(dir)
    filtered = [file for file in content if file.endswith(ext)]
    return filtered or None
    
def dirs_with_extension(ext) -> list[str]:
    """returns all the directories containing files with ext
       hint: all the VS projects contain .sln files"""
    dirs = [file.name for file in os.scandir('.') if file.is_dir()]
    filtered_dirs = [dir for dir in dirs if files_with_extension(ext,dir) is not None]
    return filtered_dirs or None

def find_dir_type(dir_path=".") -> str:
    contents = os.scandir(dir_path)
    file_types = {}
    for obj in contents:
        if obj.is_file():
            try:
                ext = "." + obj.name.split(".")[1]
            except:
                if os.access(obj.path, os.X_OK):
                    ext = "bin"
                else:
                    ext = "unknown"
            finally:
                try:
                    file_types[ext] += 1
                except KeyError:
                    file_types[ext] = 1

    return max(file_types, key=file_types.get) 

def is_pure_dir(dir_path=".", dirs_included=False) -> bool:
    contents = os.scandir(dir_path)
    
    file_types = set()
    dir_types = set()
    
    for obj in contents:
        if obj.is_file():
            try:
                ext = "." + obj.name.split(".")[-1]
                file_types.add(ext)
            except IndexError:
                continue
        elif obj.is_dir() and dirs_included:
            dir_types.add(obj.name)
    
    if dirs_included:
        return len(file_types) == 0 and len(dir_types) == 1
    else:
        return len(file_types) == 1

# print("Projects found:")
# for dir in dirs_with_extension(".sln"):
#     print(f"- {dir}")
