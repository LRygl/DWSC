import os


def getFileSize(filePath):
    file_size = os.path.getsize(filePath)
    return convertBytes(file_size)

def isFileOverSizeLimit(filePath, fileLimit):
    print("File size ", getFileSize(filePath))
    print("File limit ", fileLimit)
    return getFileSize(filePath) > fileLimit

def convertBytes(size, unit=None):
    if unit == 'KB':
        return size / 1024
    elif unit == 'MB':
        return size / (1024 ** 2)
    elif unit == 'GB':
        return size / (1024 ** 3)
    else:
        return size
