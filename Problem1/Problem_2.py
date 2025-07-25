import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_found = []
    files_found = _recursion_find_files(suffix, path)
    return files_found

def _recursion_find_files(suffix, path):
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return None
    elif os.path.isdir(path):
        files = []
        file_list = os.listdir(path)
        for file in file_list:
            next_path = os.path.join(path, file)
            result = _recursion_find_files(suffix, next_path)
            if result is not None:
                files = files + result
        return files


# None case;
print(find_files(".c", "./testdir"))
# Python files;
print(find_files(".py", "./"))
# PDFs;
print(find_files(".pdf", "./")) 
# Pictures;
print(find_files(".jpg", "./"))

# Edge case;
print(find_files("", "./")) # prints all, but its invalid (empty) suffix;