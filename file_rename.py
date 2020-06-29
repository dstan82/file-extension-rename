import glob
import os


def confirm_path():
    while True:
        path = '/home/storm/test1' # path = input('Please select the main folder PATH:')
        if os.name == 'nt':
            os.system('tree /f '+path)
        else:
            os.system('tree '+path)
        confirm = input('Press <enter> to confirm or "r" to enter again:')
        if confirm != 'r':
            return path


def search_file(path):
    files_to_be_renamed = []

    extension = input('Enter the file extension you wish to rename (ie: txt, xlsx, srt, sub):')
    rename_to = input('Enter the new file extension (ie: txt, srt, ro.srt, old.conf):')
    print('\n'+'='*60)

    for file in glob.iglob(path + '/**/*.'+extension, recursive=True):
        if extension < rename_to:
            print(f'File needs renaming: {file.split("/")[-1]}')
            files_to_be_renamed.append(file)
        elif file.endswith(rename_to):
            pass
        else:
            print(f'File needs renaming: {file.split("/")[-1]}')
            files_to_be_renamed.append(file)
    if len(files_to_be_renamed) == 0:
        print('No files match the criteria to be renamed. Exiting.')
        exit()
    else:
        print(f'='*60 + f'\n{len(files_to_be_renamed)} files will be affected')
        answer = input(f'Proceed with renaming? (Y/n):')
        if answer == 'Y':
            rename(files_to_be_renamed, extension, rename_to)
        else:
            print('Exit with no changes.')


def rename(files_to_be_renamed, extension, rename_to):
    print('='*60)
    for file in files_to_be_renamed:
        print(f'Renaming file: {file.split("/")[-1]} to {file.split("/")[-1][:-len(extension)]+rename_to}')
        os.rename(file, file[:-len(extension)]+rename_to)
    print(f'\n{len(files_to_be_renamed)} files renamed.')


search_file(confirm_path())
