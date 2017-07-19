from Account import *;
import File;
import io;

a = Account('1 name','2 lnk','3 lgn','4 pswd','5 comnt');
a.show_account();

f = File.File('accounts.txt','d:\\OneDrive\\Documents\\!Different\\');
f.get_details();
'''
print('input pass_phrase:');
pass_phrase = input();
print('password = {}'.format(pass_phrase));
'''


menu_commands = dict();
menu_commands = {1:'exit', 2:'enter pass phrase', 3:'open file'};

commands = menu_commands.values();
commands_number = menu_commands.keys();

print('MENU:');
for item in menu_commands.items():
  print('- {} - {}'.format(item[0],item[1]));


command = 0;

while command != 1:
  print('enter command: ');
  command = int(input());
  if command not in commands_number:
      print('!!! WRONG COMMAND !!! please choose from menu');
    
      