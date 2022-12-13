import os

START_PATH = "/home/gear/Github/DSA_exercises"

### recursively get file size.


def getDiskUsage1(start_path):
    """Return the number of bytes used by a file/folder and any descendents."""

    total = 0
    for dir in os.listdir(start_path):
        if dir[0] != ".":
            candidate_path = os.path.join(start_path, dir)

            if os.path.isdir(candidate_path):
                getDiskUsage1(candidate_path)
            else:
                size = os.path.getsize(candidate_path)
                print(f"File {dir} in directory {start_path} is {size} bits")
                total += size

    return total


def getDiskUsage2(start_path):
    """Return the number of bytes used by a file/folder and any descendents."""

    total = 0
    for dir in os.listdir(start_path):
        if dir[0] != ".":
            candidate_path = os.path.join(start_path, dir)

            if os.path.isdir(dir):
                getDiskUsage2(candidate_path)
            else:
                size = os.path.getsize(dir)
                print(f"File {dir} in directory {start_path} is {size} bits")
                total += size

    return total
