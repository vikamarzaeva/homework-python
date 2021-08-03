import os

def check_modified_files():
    path = input("Enter path to the git repository: ")
    os.chdir(path)                                         #change the directory
    current_dir = os.getcwd()                              #check current directory
    bash_command = [f"cd {current_dir}", "git status"]
    result_os = os.popen(' && '.join(bash_command)).read()
    for result in result_os.split('\n'):
        if 'modified' in result:
            prepare_result = result.replace('\tmodified:   ', '')
            print(f"{current_dir}+'/'+{prepare_result}")

if __name__ == '__main__':
    check_modified_files()
