import os

# Try except blocks to handle common errors and right way of writing them.

def main():
    print(f'Your current directory is {os.getcwd()}')
    dir_name = input('Enter path/directory you want to change to ?')
    try:
        os.chdir(dir_name)
        print(f'Your directory is changed to {os.getcwd()}')
    except FileExistsError:
        print("The given path isn't valid as file not found.")
    except NotADirectoryError:
        print("The given path isn't a directory")
    except PermissionError:
        print("Sorry you don't have access for the given path, so can't change working directory")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()