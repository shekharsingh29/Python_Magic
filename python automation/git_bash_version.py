import subprocess
import platform
# Script to find bash version and git version on Linux, Windows respectively.

'''
sp = subprocess.Popen(CMD,SHELL=True/False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True )
if CMD is a string ('ls -lrt') then next parameter will be True
if CMD is a list (['ls', '-lrt']) then next parameter will be False
if universal_newlines isn't True then output won't be in list format but in a bytecode format
'''

if platform.system() == 'Windows':
    CMD = 'git --version'
else:
    CMD = 'bash --version'


sp = subprocess.Popen(CMD,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True )
rc = sp.wait()
out, err = sp.communicate()

if rc == 0 and platform.system() == 'Windows':
    for each_line in out.splitlines():
        if 'version' in each_line:
            git_version = each_line.split()[2]
            print(f'The Git version is { git_version }')
elif rc == 0 and platform.system() == 'Linux':
    print(f'The output is {out}')
else:
    print(f'The output is {err}')


