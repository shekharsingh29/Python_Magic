import re

with open('.\Input\Letters\starting_letter.txt',mode="r") as file1:
    starting_letter_content = file1.read()
    print(starting_letter_content)
    file1.close()

with open(r'.\Input\Names\invited_names.txt') as file2:
    invited_names = re.split('\n',file2.read())
    file2.close()

for invite in invited_names:
    
    starting_letter_content_temp = starting_letter_content.replace('[name]', invite)
    print(invite)
    with open(f'.\Output\ReadyToSend\{invite}.txt',mode="w") as file3:
        file3.write(starting_letter_content_temp)
        file3.close()


    
    
