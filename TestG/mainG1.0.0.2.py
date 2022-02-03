import time
import os

start_screen_list = ['loading offsets...', 'downloading bitmaps...', 'checking for updates...', 'all complete!']
trolls = range(0, (len(start_screen_list)))

developer_mode = input('\n#####################################################'
          '\n              Welcome to Funners!!!'
          "\n               the world's first..."
          '\n    external interaction management base program??\n'
          '\n      you can make a new character by using'
          '\n       the [/funners create] command or'
          '\n  log into an existing account using [/funners login]\n'
          '\n         hope you enjoy the experiment!!'
          '\n#####################################################'
          '\n(press [Enter] to continue)')

if developer_mode == '42069':
    developer_mode = True
    print('<DEVELOPER MODE ACTIVATED>')
    for troll in trolls:
      if troll != len(start_screen_list)-1:
          print(start_screen_list[troll])
      else:
          print(start_screen_list[troll])

else:
    for troll in trolls:
        if troll != len(start_screen_list)-1:
            time.sleep(1)
            print(start_screen_list[troll])
        else:
            time.sleep(2)
            print(start_screen_list[troll])
    time.sleep(1)

# print("loading offsets...\ndownloading bitmaps...\nchecking for updates...\nall complete!\n")
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m' #??

reg = '\033[0m'


commands = {
            '/help': 'gives a list of available commands.',
            '/helpX': 'helpX is a command that defines, explains or helps to use any one of the'
              '\n available commands - for example [/helpX funners]'
              "\n... although you already knew that haven't you?."
                      + '\n..\n...\nough fune,,you just found an easter egg ,, remember the code 00756 '
                        'it may come in handy later on.'
                        '\n {similar commands: [helpx]}', #do something with this number,, lol.
            '/stop': 'closes the program'
                        '\n{similar commands: [/close], [/end], [/quit]}',
            '/countsheeps': 'helps you fall asleep', #delete?
            '/funners': 'displays the welcome screen!',
            '/funners create': 'creates a new Funners character'
                               '\n{similar commands: [/funners register], [/funners make account]}',
            '/funners login': 'logs into and uses an existing Funners character'
                              '\n{similar commands: [/funners log in]}',
            '/funners users': 'displays the current local users that exists on this computer... if there are any',
            }

def CommandsReturnerXD(command):
    bob = str(command).lower()
    if bob == '/helpx':
        bib = '/helpX'
    elif bob == '/close' or  command == '/end' or  command == '/quit':
        bib = '/stop'
    elif bob == '/register' or command == '/account' or command == '/create':
        bib = '/funners create'
    elif bob == '/in' or command == '/login':
        bib = '/funners login'
    elif bob == '/users':
        bib = '/funners users'
    else:
        bib = bob
    return bib


commands_keys_list = list(commands.keys())
commands_values_list = list(commands.values())
number_of_commands_range = range(0, len(commands.items())) #if doesnt work do commands_keys_list instead
CloseProgram = False

#define functions for commands
#########################################################

def help():    #/help
    for y_value_commands in number_of_commands_range:
        current_y_command = str(commands_keys_list[y_value_commands])
        print(blue + current_y_command + reg)

def helpX(UserInput):    #/helpX
    if UserInput.count('/') > 1:
        print(yellow + 'make sure to not use more than one slash "/"  !!' + reg)


    elif UserInput == '/helpx':
        print(blue+ "\n use /helpX + [command name] for the specific command's info" +reg)
    else:
        words2 = UserInput.replace('/helpx','')
        words2 = words2.split(' ')
        if words2.__contains__(''):
            words2 = list(filter(None, words2))
        if len(words2) >= 1:
            UserInput = words2[len(words2) -1]
            UserInput = ('/' + UserInput)
            UserInput = CommandsReturnerXD(UserInput)
            if commands.keys().__contains__(UserInput):
                print(blue + 'The command ' + UserInput + ' =\n' +commands[UserInput] + reg)
            else:
                print(yellow + 'Error -- the command you were trying to examine was not found,'
                      '\nplease try again and check your spelling!' + reg)
        else:
            print(yellow + 'if you want to get an explanation for a certain '
                           '\ncommand - please add the desired command!!!' + reg)

def close():    #/help
    print("hope you enjoyed the testG, have a nice day!")
    time.sleep(2)
    print("closing...")
    time.sleep(1)

def count_sheeps():   #count sheeps
    for x in range(1, 11):
        if x < 2:
            print(str(x) + " sheep")
        else:
            print(str(x) + " sheeps")
    print("you fell asleep")


######################################## main function (funners) ############################################

def Funners_descrition():
    print('\n#####################################################'
          '\n              Welcome to Funners!!!'
          "\n               the world's first..."
          '\n    external interaction management base program??\n'
          '\n      you can make a new character by using'
          '\n       the [/funners create] command or'
          '\n  log into an existing account using [/funners login]\n'
          '\n         hope you enjoy the experiment!!'
          '\n#####################################################')


def onlyABC(question):
    abcABC123_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    loop = True
    while (loop):
        answer = input(question + '\n')
        if any((c in abcABC123_set) for c in answer):
            return answer
            loop = False
        else:
            print('(all answers must only contain English letters and/or numbers!)\n')



def Funners_create():
       #FolderFunners = open('Funners.txt', 'x') #used only to creat a file but will make error if exists.!
       Funners_addtoend = open('Funners.txt', 'a')
       #Funners_overright = open('Funners.txt', 'w')    ** careful - using 'w' wipes all!
       Funners_readonly = open('Funners.txt', 'r')
       copy_of_funners_txt = Funners_readonly.read()
       Funners_readonly.close()
       # copied!


                    #reaches funners txt. creates one if doesnt exist. [done]
                    ##users_name = input('whats your name?\n') [done]
                    ##if line X is occupied, go to X+1
                    ##write (users_name + ":")
                    ##whats your favorite color? whats your favorite food?
                    #ADD PASSWORD

       print('(all answers must only contain English letters and/or numbers!)\n')
       loop = True
       while(loop):
        username_funner = onlyABC('choose a username (?)')
        if len(username_funner) > 8:
            print("sorry!! - usernames must'nt be longer than 8 characters!\n")
        else:
         for x in range((8 - len(username_funner))):
            username_funner += ' '
         loop = False
       username_funner += ': '
       print('username saved.')
       #if username_funner ALready exists!! do smth. try to log in or smth/

       loop = True
       while(loop):
        YesNo = input('\ndo you want a password for your funners (?)\n'
                     '[having no password makes your Funners accessible to All!!]\n')
        if YesNo == 'no':
            print('funners set to public.')
            userpass_funner = 'PUBLIC ' #8chars
        elif YesNo == 'yes':


           while (loop):
            userpass_funner = onlyABC('\nchoose a password.\n(can only use english characters or numbers! '
                                      'AND must not be longer than 8 characters!)')
            if len(userpass_funner) > 8:
                print(yellow + 'invalid password attempt, must be not be longer than 8 characters!!' + reg)
            else:
                for x in range((8 - len(username_funner))):
                    userpass_funner += ' '
                loop = False

           print('good! password set.')
        else:
           print(yellow + 'thats not a yes or a no' + reg)

       if copy_of_funners_txt[len(copy_of_funners_txt) - 2 : len(copy_of_funners_txt)] != '\n':
        #basically makes a new line if there is no new line.
        Funners_addtoend.write('\n')
        #works??
        #... I think this is used for if the file has other junk that I didnt put


       #check how many lines
       number_of_users = copy_of_funners_txt.count('\n') #lol


       Funners_addtoend.write(username_funner + 'pass[' + userpass_funner + '] - ')
       print('\ngreat!! - your Funners has been successfully created!')



       Funners_addtoend.write('\n')
       #above line makes a new line for the next use, after finishing using this one line!!!!

       #FolderFunners.close()
       Funners_addtoend.close()
       #Funners_overright.close()
       Funners_readonly.close()




#################################################################

#using 'w' to open files wipes everything!!! aaaaaaaa

def Funners_Display_Users():
    bye = open('Funners.txt', 'a')
    bye.close()
    #make folder if there is none.

    read_only = open('Funners.txt', 'r')
    copy_of_funners_txt = read_only.read()
    read_only.close()
    #copied!


    if copy_of_funners_txt.count == 0:
        return 'no users found!'
    else:
        users_list = [copy_of_funners_txt.split('\n')]
        number_of_users = copy_of_funners_txt.count('\n') #lol
        position_of_users_X = 8 #max 8.
        if not number_of_users > 0:
            print('no users found')
        else:
            corrupted_lines = []
            has_empty_spaces = '' in users_list
            if has_empty_spaces:   #doesnt work??!?!?!?
                users_list.remove('')
            #removes empty values

            for c in range(0, number_of_users):

                if len(str(users_list[c])) < 8:
                    corrupted_lines += str(c)
                elif not str(users_list[c])[10:17] == ': pass[':
                    corrupted_lines += str(c)
                else:
                    users_list[c] = str(users_list[c])[2:10].strip()
                #filters only "correct" code lines and marks the corrupted lines

            for c in range(0, number_of_users):

                print('user ' + str(c+1) + ': ' + users_list[c])




def Funners_login():
    a = 1
    #should use the Write To Line function. f = open(funners 'w'), f.writetoline
    #should find if the user exists, find the line and only let to enter if pass correct or public.
    #!!! 27 moves to the right is the start of free space after pass!!
    #maybe add encryption to the passwords?? XD









#start dialog
UserInput = 'HM'
while(CloseProgram != True):
    UserInput = input("\nhmm?\n[use /help for a list of commands]\n")
    UserInput = UserInput.lower()
    if UserInput == "/count sheeps" or UserInput == "/Count sheeps" or UserInput == "/Count Sheeps" \
                               or UserInput == "/countsheeps"  or UserInput == "/CountSheeps":
    # func to neglect uppercase characters?
        count_sheeps()

    elif UserInput == "/help":
        help()

    elif UserInput == "/helpX" or UserInput == "/helpx" \
    or UserInput.__contains__("/helpx") and len(str(UserInput)) > 7:
        helpX(UserInput)

    elif UserInput == "/stop" or UserInput == "/close":
        close()
        CloseProgram = True

    elif UserInput == "/funners create" or UserInput == "/funners make account" or UserInput == "/funners register":
        Funners_create()

    elif UserInput == "/funners log in" or UserInput == "/funners login":
        Funners_login()

    elif UserInput == "/funners":
        Funners_descrition()

    elif UserInput == "/funners users":
        Funners_Display_Users()

    #elif

    else:
        print(yellow + "sorry, this is not a viable command!" + reg)


#program ends.

#make pass also always 8 chars
#solve bug with no pass public loop
#make it so no duplicate usernames

#make def to organize file to use in every other 3 commands