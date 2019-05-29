import os

def findall(path):
    cands = []
    for root, dirs, files in os.walk(path):
        for file in files: cands.append(os.path.join(root, file))
    return cands

