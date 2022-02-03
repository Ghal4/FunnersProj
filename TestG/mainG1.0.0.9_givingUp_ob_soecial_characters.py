import time
import os

blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'  # ??

reg = '\033[0m'

def bop():
    speacial_char_list = ['#', '!', '*']
    cant_be = ['$', '%', '()[]{}', '^', '&', ';_-~']
    already_is = \
        {
        '$': 'used in CASH player info.',
        '%': 'separate usersname and password.',
        '[](){}': 'idk but I think itll cause problems',
        '^': "separate user info's like CASH^HP^POSITION",
        '&': 'separate user and pass to user info',
        ';': 'separate map tiles',
        '_': "separate map tile's information",
        '-': "separate map tile's information's to a bunch of information on each tile.",
        '~': 'separate map tiles to map info on tiles'
        }
    return 'you handsome bro'

def start_program(SPEED):
    if SPEED == 3: #get speed so it affects all program.

        start_screen_list = ['loading Funners content', 'decrypting...', 'analyzing data...', 'setting up...',
                             'all complete!']

        SPEED_GET = 1
        trolls = range(0, (len(start_screen_list)))
        developer_mode = input('(press [Enter] to start)')
        if developer_mode == '42069':
            developer_mode = True
            SPEED_GET = 0
            print('<DEVELOPER MODE ACTIVATED>')
            return SPEED_GET
        return SPEED_GET
    else:

        start_screen_list = ['loading Funners content', 'decrypting...', 'analyzing data...', 'setting up...',
                             'all complete!']
        trolls = range(0, (len(start_screen_list)))

        print('looking for Funners folder...')
        time.sleep(SPEED)
        check = open('Funners.txt', 'r')
        check_content = check.read()
        check.close()

        content_list = []
        if check_content == '' or not '\n' in check_content:  #~ is between lines of world/game in line 0
            if not '\n' in check_content:
                corruptedFunners = open('CorruptedFunners.txt', 'a')
                corruptedFunners.write('\n' + check_content)
                corruptedFunners.close()
                print('a ' + yellow + 'corrupted ' + reg + 'Funners folder was found!!')
                print('all of the corrupted text had been moved and stored in a new file named "CorruptedFunners",\n'
                      'and a new Funners file have been created!')
                time.sleep(SPEED)
            else:
                print('no previous record found, a brand new Funners folder have been created!')
                time.sleep(SPEED)
            content_list = check_content
        else:
            print('Funners folder found!')
            time.sleep(SPEED / 2)
            print('checking for corruption...')
            time.sleep(SPEED / 2)
            content_list = (check_content.split('\n'))
            number_of_lines = check_content.count('\n')
            number_of_corrupted_lines = 0
            corrupted_lines_position = []
            corrupted_lines_content = []
            number_of_empty_strings = 0

            if '~' in check_content:   #makes it so if #0 occupupied it wont check but If It isnt it will check #0 for users
                q = 1
            else:
                q = 0

            for c in range(q, len(content_list)):#q bc line #0 can be WroldInfo
                if len(content_list[c]) < 25 and str(content_list[c])[8:15] != ': pass[' and content_list[c] != '':
                    number_of_corrupted_lines += 1
                    corrupted_lines_position += str(c)
            # saves the number and position of corrupted strings
            if number_of_corrupted_lines != 0:
                print(yellow + 'your file is corrupted!!' + reg)
                time.sleep(SPEED)
                print('* make sure not to touch or change anything within the files. *')
                print('cleaning corruption from flie...')
                time.sleep(SPEED / 2)
                for c in range(0, number_of_corrupted_lines):
                    corrupted_lines_content.append(content_list[int(corrupted_lines_position[c])])
                    content_list[int(corrupted_lines_position[c])] = ''
                corruptedFunners = open('CorruptedFunners.txt', 'a')
                for c in range(0, len(corrupted_lines_content)):
                    corruptedFunners.write('\n' + corrupted_lines_content[c])
                corruptedFunners.close()
                print('all of the corrupted text had been moved and stored in a new file named "CorruptedFunners",\n'
                      "now the original file is corruption free! ,"
                      "\n(you should take a look and see if there haven't been any mistake or important information "
                      "removed)")
                time.sleep(SPEED)

            # turns corrupted strings into empty ones and saves them aside

            for c in range(0, len(content_list)):
                if '' == content_list[c]:
                    number_of_empty_strings += 1
            # saves the number and position of empty strings
            if number_of_empty_strings != 0:
                for c in range(0, number_of_empty_strings):
                    content_list.remove('')
            # removes all the empty strings

            print('everything looks fine! Funners file is ready to go!!')
            time.sleep(SPEED / 2)
            print('starting...')
            time.sleep(SPEED * 2)

        a = input('\n#####################################################'
                  '\n              Welcome to Funners!!!'
                  "\n               the world's first..."
                  '\n    external interaction management base program??\n'
                  '\n      you can make a new character by using'
                  '\n       the [/funners create] command or'
                  '\n  log into an existing account using [/funners login]\n'
                  '\n         hope you enjoy the experiment!!'
                  '\n#####################################################'
                  '\n(press [Enter] to continue)')

        for troll in trolls:
            if troll != len(start_screen_list) - 1:
                time.sleep(SPEED)
                print(start_screen_list[troll])
            else:
                time.sleep(SPEED * 2)
                print(start_screen_list[troll])
            time.sleep(SPEED)
        # print("loading offsets...\ndownloading bitmaps...\nchecking for updates...\nall complete!\n")
        if len(content_list) != 0:
            refresh = open('Funners.txt', 'w')
            for c in range(0, len(content_list)):
                refresh.write(content_list[c] + '\n')
            refresh.close()
            # makes the file clean and corruption free.. not really necssesary but why not lol

        return content_list

SPEED = 3
SPEED = start_program(SPEED) #get SPEED
FUnnersContent = []
FunnersContent = list(start_program(SPEED))




users_list = []
pass_to_user = {}
user_content = []
user_serial_number = {}

if FunnersContent != '':
    if len(FunnersContent) == 0:
        nothing = 'no users'
    else:
        position_of_users_X = 8  # max 8.
        if not len(FunnersContent) > 0:
            nothing = 'no users'
        else:
            for c in range(0, len(FunnersContent)):
                if not '~' in FunnersContent[c] or c != 0:#because #0 line is not a users
                    users_list.append(str(FunnersContent[c])[0:8].strip())
                    #basically = as long as c is NOT 0 do the line. and if c is 0, if line c(line 0) has ~, dont do line
            # sets each user name as a value in the user list
            for c in range(0, len(users_list)):
                if not '~' in FunnersContent[c] or c != 0:
                    pass_to_user[users_list[c]] = (str(FunnersContent[c])[15:23].strip())

commands = {
    '/help': 'gives a list of available commands.',
    '/helpX': 'helpX is a command that defines, explains or helps to use any one of the'
              '\n available commands - for example [/helpX funners]'
              "\n... although you already knew that haven't you?."
              + '\n..\n...\nough fune,,you just found an easter egg ,, remember the code 00756 '
                'it may come in handy later on.'
                '\n {similar commands: [helpx]}',  # do something with this number,, lol.
    '/stop': 'closes the program'
             '\n{similar commands: [/close], [/end], [/quit]}',
    '/countsheeps': 'helps you fall asleep',  # delete?
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
    elif bob == '/close' or command == '/end' or command == '/quit':
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
number_of_commands_range = range(0, len(commands.items()))  # if doesnt work do commands_keys_list instead
CloseProgram = False


# define functions for commands
#########################################################

def help():  # /help
    for y_value_commands in number_of_commands_range:
        current_y_command = str(commands_keys_list[y_value_commands])
        print(blue + current_y_command + reg)


def helpX(UserInput):  # /helpX
    if UserInput.count('/') > 1:
        print(yellow + 'make sure to not use more than one slash "/"  !!' + reg)


    elif UserInput == '/helpx':
        print(blue + "\n use /helpX + [command name] for the specific command's info" + reg)
    else:
        words2 = UserInput.replace('/helpx', '')
        words2 = words2.split(' ')
        if words2.__contains__(''):
            words2 = list(filter(None, words2))
        if len(words2) >= 1:
            UserInput = words2[len(words2) - 1]
            UserInput = ('/' + UserInput)
            UserInput = CommandsReturnerXD(UserInput)
            if commands.keys().__contains__(UserInput):
                print(blue + 'The command ' + UserInput + ' =\n' + commands[UserInput] + reg)
            else:
                print(yellow + 'Error -- the command you were trying to examine was not found,'
                               '\nplease try again and check your spelling!' + reg)
        else:
            print(yellow + 'if you want to get an explanation for a certain '
                           '\ncommand - please add the desired command!!!' + reg)


def close():  # /help
    print("hope you enjoyed the testG, have a nice day!")
    time.sleep(2)
    print("closing...")
    if len(FunnersContent) != 0:
        refresh = open('Funners.txt', 'w')
        for c in range(0, len(FunnersContent)):
            refresh.write(FunnersContent[c] + '\n')
        refresh.close()
    time.sleep(1)


def count_sheeps():  # count sheeps
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
        Valid = True
        answer = input(question + '\n')
        answerSplit = [char for char in answer]
        for c in range(0, len(answerSplit)):
            if not answerSplit[c] in abcABC123_set:
                Valid = False
        if Valid == False:
            print('(all answers must only contain English letters and/or numbers!)\n')
        else:
            loop = False
            return answer


def Funners_create():
    global FunnersContent
    # FolderFunners = open('Funners.txt', 'x') #used only to creat a file but will make error if exists.!
    Funners_addtoend = open('Funners.txt', 'a')
    # Funners_overright = open('Funners.txt', 'w')    ** careful - using 'w' wipes all!

    list_of_existing_users = []
    for c in range(1, len(FunnersContent)):
        list_of_existing_users.append(str(FunnersContent[c])[0:8].strip())

        # reaches funners txt. creates one if doesnt exist. [done]
        ##users_name = input('whats your name?\n') [done]
        ##if line X is occupied, go to X+1
        ##write (users_name + ":")
        ##whats your favorite color? whats your favorite food?
        # ADD PASSWORD

    print('(all answers must only contain English letters and/or numbers!)\n')
    loop = True
    while (loop):
        username_funner = onlyABC('choose a username (?)')
        if len(username_funner) > 8:
            print("sorry!! - usernames must'nt be longer than 8 characters!\n")
        elif username_funner in list_of_existing_users:
            print('sorry! usersname already exists!!')
        else:
            for x in range((8 - len(username_funner))):
                username_funner += ' '
            loop = False
    username_funner += ': '
    print('username saved.')

    loop = True

    while (loop):
        userpass_funner = onlyABC('\nset a password for your Funners.'
                                  '\n(can only use english characters or numbers! '
                                  'AND must not be longer than 8 characters!)'
                                  '\nif you want your Funners to be public please '
                                  '\n[having no password makes your Funners accessible to All!!]\n'
                                  )
        if userpass_funner == 'PUBLIC' or 'public' or 'Public':
            print('funners set to public.')
            userpass_funner = 'PUBLIC  '  # 8chars
            loop = False

        elif len(userpass_funner) > 8:
            print(yellow + 'invalid password attempt, must be not be longer than 8 characters!!' + reg)
        else:
            for x in range((8 - len(username_funner))):
                userpass_funner += ' '
            loop = False

    print('good! password set.')

    if FunnersContent[len(FunnersContent) - 2: len(FunnersContent)] != '\n':
        # basically makes a new line if there is no new line.
        Funners_addtoend.write('\n')
        # works??
        # ... I think this is used for if the file has other junk that I didnt put

    # check how many lines
    number_of_users = FunnersContent.count('\n')  # lol
    FunnersContent += [username_funner + 'pass[' + userpass_funner + ']&']
    print('\ngreat!! - your Funners has been successfully created!')

    Funners_addtoend.write('\n')
    # above line makes a new line for the next use, after finishing using this one line!!!!

    # FolderFunners.close()
    Funners_addtoend.close()
    # Funners_overright.close()
    return username_funner + '%' + userpass_funner


#################################################################

# using 'w' to open files wipes everything!!! aaaaaaaa

def Funners_Display_Users():
    if len(users_list) == 0:
        print('no users found!')
        return 'no users found!'
    else:

        for c in range(0, len(users_list)):
            print('user ' + str(c + 1) + ': ' + users_list[c])


def Funners_login():
    # should use the Write To Line function. f = open(funners 'w'), f.writetoline
    # should find if the user exists, find the line and only let to enter if pass correct or public.
    # !!! 27 moves to the right is the start of free space after pass!!
    # maybe add encryption to the passwords?? XD

    user_input = input('please enter your username\n')
    if not user_input in users_list:
        print('this user does not exist!')
        print('check if you have any spelling mistakes or try to find your account inside the user list')
        print('\n by using /funners users')
    else:
        desired_account = user_input
        failed_attempts = 0
        loop = True
        while (loop):
            user_input = input('nice!, now please enter your password')
            if pass_to_user[desired_account] == user_input:
                LoggedIn = True
                LoggedUser = user_input
                loop = False
            elif user_input == 'back!':
                LoggedIn = False
                LoggedUser = 'nope'
                loop = False
            else:
                print('password incorrect , please try again')
                failed_attempts += 1
                if failed_attempts > 3:
                    print('you can go back by writing "back!".')
    return LoggedUser


def LoggedInProtocole(LoggedUser):
    # for c in range(0, len(FunnersContent)):
    #    if str(FunnersContent[c])[0:8].strip() == LoggedUser:
    #        FunnersContent_LoggedUser = FunnersContent[c]
    # find the right line.

    positionOfLoggedUserInFunnersContent = users_list.index(user_and_pass[0])
    FunnersContent_LoggedUser = FunnersContent[positionOfLoggedUserInFunnersContent]
    # also finds the right line but without going over all the lines...

    FunnersContent_LoggedUser = FunnersContent_LoggedUser.split('&') #^ between em
    filteredContent_userNpass = FunnersContent_LoggedUser[0]
    FunnersContent_LoggedUser = FunnersContent_LoggedUser[1]
    # choose and make it so its not equal to the start thingy - pass and user.
    # I mean - filters the unnecessary.

    if FunnersContent_LoggedUser == '': #user never played and don't have info
        print('a new user!! welcome!!!')
        FunnersContent_LoggedUser = 'POS^HP^CASH^QUEST^INV' #make dict of pos=0,hp=1,cash=2,quest=3,inv=4?
                                                           #looklike-> '58^20^55$^kill dragon^bottle↨swordLVL2↨rock

    print('checking for a Local world...')
    time.sleep(1 * SPEED)
    if not '~' in FunnersContent[0]:#Means never played Because no ~,since ~ happens after loging in for the 1st time
        FunnersContent.insert(0, '') #makes line #0 free to use. or rather creates a new one!
        FunnersContent_Line0 = ['WrldTiles', 'WrldInfo']

    else:
        FunnersContent_Line0 = FunnersContent[0].split('~')
        #should look like : 'Y1;forest;forest;forest;forest...', '___IronSword[lvl1](1){trapped}-rock__
        # raw = Y0;forest;forest;forest;forest...Y20Y40~___IronSword[lvl1](1){trapped}-rock__

    FunnersContent_Line0_WrldTiles = FunnersContent_Line0[0]
    FunnersContent_Line0_WrldInfo = FunnersContent_Line0[1]
    if '-' in FunnersContent_Line0_WrldTiles:
        print('Local world found!')
        time.sleep(0.5 * SPEED)
        FunnersContent_Line0_WrldTiles = FunnersContent_Line0_WrldTiles.split('-')
        print('analyzing world data...')
        time.sleep(1 * SPEED)
        if '_' in FunnersContent_Line0_WrldInfo:
            FunnersContent_Line0_WrldInfo = FunnersContent_Line0_WrldInfo.split('_')
        if len(FunnersContent_Line0_WrldTiles) == 20*20 and len(FunnersContent_Line0_WrldInfo) == 20*20:
            print('analyzing done!')
            #######yooooooooooo btwwwwwwwww I should add simulation thing that once a few actions the world plays itself
        else:
            print(yellow + 'there was an error while trying to analyze your Local world data.'
                  '\nit seems as if your world has been corrupted, and it is advised to created a new world.' + reg)
            loop = True
            while(loop):
                refreshworld = input('would you like to create a new world?')
                if refreshworld == 'no':
                    print('alright. logging out...')
                    return() #goes out of def
                elif refreshworld == 'yes':
                    print('...')
                    time.sleep(1 * SPEED)
                    loop = False
                else:
                    print('sorry that is not a valid answer.')

            #WIPE!!
            FunnersContent_Line0 = ['WrldTiles', 'WrldInfo']
            FunnersContent_Line0_WrldTiles = FunnersContent_Line0[0]
            FunnersContent_Line0_WrldInfo = FunnersContent_Line0[1]
            print('world has been wiped!!!')

    if FunnersContent_Line0 == ['WrldTiles', 'WrldInfo']: ##### generate new world!!!!!!!!!!!!!!!!!!
        print('------- !generating new world! -------')
        time.sleep(1 * SPEED)
        print('- planting trees....')
        time.sleep(2 * SPEED)
        FunnersContent_Line0[0] = ''
        for c in range(0,20*20):
            FunnersContent_Line0[0] += ['Y' + str(c*20) + ';' + 'forest;' * 19]
        a = 1






    # read the content based on what im gonna make like STAT and FOOD and COIN ...

    InGame_Commands_description = {
                           #######v#commands that only work alone#v#####

                           ##v#META commands (outside the game)#v##
                           'LOGOUT': 'log out and exit Funners',  # cant log out everywhere
                           'STATUS': 'set a public status for your user',

                           ##v#Value or information commands#v##
                           'HP': 'displays your current amount of hit points - health',
                           'CASH': 'the amount of money you have',
                           'SHOP': 'presents the local items catalogue',
                           'QUEST': 'a quest you have to complete in order to get rewards',
                           'LOCATION' or 'POS': 'where you currently are',
                           'LOOK AROUND': 'describes what you see by your surroundings',
                           # this helps the program, but shouldn't always display because it's a secret sometimes.
                           # ohh and it should say the area based on pos like X2Y4 by reading the self made dict!!!!
                          'INV' or 'I': 'checks your inventory',

                           #######v#commands that require input#v#######

                           ##v#Action Commands
                          'READ': 'read something',
                          'LOOK': 'look at a direction [up down left right]',
                          'EXAMINE': 'check something',
                           # if you examine someone it can offend them, lmao.
                          'TAKE': 'take something',
                          'GO': 'walk towards a certain direction  [left, up, right, down] (2D, up is forward..)',
                          'CLIMB': 'climb something. actually go up',
                          'USE' : ' use one of your items from inventory',
                          # climb a tree, climb the stairs. can fall.
                          'talk with': 'have a conversation with someone',

                                  }

    InGame_All_ItemsDescription = {
                            'EMPTY BOOK': 'publish your own book',  # and put it in store and get money
                            # like, put it in inv and then u can offer it to the shop keeper
                            # also make it so has to be X lines else people won't buy??, or other users.
                            # what do u want to call your book? input('The ') ... Add it to this dict if player gets
                            'THE ' + '...': 'a book named + '"the ..."' + written by: ' + '',
                            'SIGN': 'put a sign on things for newcomers to observe',
                            'HOUSE KEY': 'get your own house! (and a number/street/city name.)',
                            'EMPTY BOTTLE': 'an empty bottle.',  # "a bottle with X in it!",
                            'WATER BOTTLE': 'a water bottle filled with' + '27%?X' + 'water!',
                            'UNKOWN BOTTLE': 'a bottle filled with ' + 'something',
                            'MAP': 'displays a graphic view of the world ????',
                            'SPIRIT STICK': 'a dark brown stick that feels lighter than it should. '
                            "you can hear whispering coming from it, it's asking you to break it",
                            # saves game without quitting!!!!
                            # 'as you break the stick a portion of white smokey thing comes out and
                            # disappears to the air. your progress has been saved!!'
                            'iron sword LVL ' + '1': 'a metal two handed sword that deals ' + '1 ' + 'damage on hit',
                            'wooden bow LVL ' + '1': 'a wooden bow that shoots arrows dealing ' + '1' + 'damage each',
                            'iron dagger LvL ' + '1': 'a short one handed dagger that deals ' + '1 ' + 'damage on hit'

                            }

    # make something that if I'm at X and go up I end up at Y.
    # plus do that it will act different if at city.. can't walk through walls.
    # yo I have an idea
    WorldMapTiles = ['Y1', '0forest', '1forest', '2forest', '3forest', '4forest', '5forest', '6forest', '7forest',
                     '8forest', '9forest', '10forest', '11forest', '12forest', '13forest', '14forest', '15forest',
                     '16forest', '17forest', '18forest',
    'Y2', '0forest', '1city wall', '2city wall', '3city wall', '4forest', '5forest', '6forest', '7forest', '8forest', '9forest', '10forest', '11forest', '12forest', '13forest', '14forest', '15forest', '16forest', '17forest', '18forest',
    'Y3', '0forest', '1city wall', '2city enterance', '3city wall', '4forest', '...'
    ]
    # the y's are 0, 20, 40, 60...

    WorldMapContent = ['', '', '',
    '', '', '',
    '', '', '', 'two guards-[talkable, fightable...]-a sign-[readable, pickable...]'
    # make it so if there are humans, they should care if you take something depending on their position like being guards. and fight u or smth
    ]
    # you see: two guards, a sign. talk with guard -> sorry that's not possible. you can talk with: guards.


    # everything forest. make random number to define 1x1 2x2 or 3x3... do 1+2+3+21+22+23+41+42+43 = desert
    # then add lakes with 1 tile of distance for horizontally and diagonally. bc -1 -2 +1 +2 -20 -21 -40 -19 +20 +21 +40 +19 can't be water. smth like 3 lakes.
    # desert. meadows. black forest. forest(reg). swamp.
    # ohhh choose heart of biom and do that next biom cannot overright heart but can the sided!!
    # and do a maximum amount of bioms maby.

    ##if PlayerInput == 'go up' and POS >= 20:
    ##    if WorldMapTiles[int(POS) - 20] != None_passable_area
    ##        POS = POS-20
    ##        DescribeArea(POS)
    ##
    ### delete this
    ##player_pos = POS
    ##player_pos.split('X')  # 'X5Y3' -> '5','Y3'
    ##player_pos.remove('Y')  # -> '5', '3'
    ##player_pos =[int(player_pos[0]), int(player_pos[1])]]
    # now... (5,3) is actually WorldMap[28]
    # find equation to make it righttt
    # (11*(3-1)+(5+1)) damnnnn
    # but what if pos was 28?
    # then up is -11, down is +11, left -1 and right +1
    # I can even remove the 'Y' because yk lol
    # then it would be -10 and +10
    # although I don't wanna do it because if the string would be one line it'll be difficult to get where is a new line (visually)
    # okay now the map is 19x19, y's are 0,20,40... and up/down is -20/+20

    # OH MY GOD, BEST IDEA ever === make it randomized!!

    # add this to Helpx and Help, and make it so it only happens after logged protocol happened.
    # also make Funners create and Funners login and maybe welcome won't work
    # based on if Logged_User != 'none'
    # I was also thinking about maybe making a different file to run this.

    pos_U = positionOfLoggedUserInFunnersContent
    FunnersContent[pos_U] =[filteredContent_userNpass + '&' + FunnersContent_LoggedUser]
    # at the end puts everything back into FunnersContent.
    # although this needs to be done after finishing to change everything
    # means after interacting and

# start dialog
UserInput = 'HM'
while (CloseProgram != True):
    UserInput = input("\nhmm?\n[use /help for a list of commands]\n")
    UserInput = UserInput.lower()
    if UserInput == "/count sheeps" or UserInput == "/Count sheeps" or UserInput == "/Count Sheeps" \
            or UserInput == "/countsheeps" or UserInput == "/CountSheeps":
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
        add_to_list = Funners_create()
        user_and_pass = add_to_list.split(': %')
        users_list += [user_and_pass[0].strip()]
        pass_to_user[user_and_pass[0].strip()] = user_and_pass[1].strip()
        ###################################################### important!! add here whatever new I make like status etc

    elif UserInput == "/funners log in" or UserInput == "/funners login":
        LoggedUser = Funners_login()
        if LoggedUser != 'nope':
            LoggedInProtocole(LoggedUser)

    elif UserInput == "/funners":
        Funners_descrition()

    elif UserInput == "/funners users":
        Funners_Display_Users()

    # elif

    else:
        print(yellow + "sorry, this is not a viable command!" + reg)

# program ends.

# make pass also always 8 chars | Done
# solve bug with no pass public loop | Done
# make it so no duplicate usernames | Done

# make def to organize file to use in every other 3 commands
