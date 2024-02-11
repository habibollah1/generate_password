import random
import string
import os

settings = {
    'lower':True,
    'upper':True, 
    'number':True, 
    'symbol':True,
    'space':False,
    'length':8
}

PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30

def clear_screen():
    os.system('cls')


def get_user_password_length(option , default , pw_min_length= PASSWORD_MIN_LENGTH ,
                             pw_max_length= PASSWORD_MAX_LENGTH):
    while True:

        user_input = input(f"enter password length default is {default}. (enter: default)  ")
        

        if user_input == "":
            return default

        if user_input.isdigit():
            user_password_length = int(user_input) 
            if pw_min_length <=  user_password_length <=pw_max_length:
                return int(user_input)
            print("invalid input")
            print(f'password length should be between {pw_min_length} and {pw_max_length} ')
        
        else:
            print("invalid number. you should enter a number. ")
        print("please try again ")

def get_yes_or_no_for_list(option , default):
    while True:

        user_input = input(f"include {option}? "
        f"default is {default} choose (yes: y) or (no: n) or (enter: default) ")

        if user_input == "":
            return default


        if user_input in ['y' , 'n']:
            return user_input == "y"
        print("invalid input. please try again")
        #     return True
        # else:
        #     False



        # if user_input == "y" or user_input == "n":
            
        #     if user_input == "y":
        #         # settings[option] = True
        #         return True
        #     else:
        #         # settings[option] = False
        #         return True
        #     break

        # else:
        #     print("invalid input . please try again")



def get_settings_from_user(settings):

    for option , default in settings.items():
        if option != "length":
            user_choice = get_yes_or_no_for_list(option , default)
            print(user_choice)
            settings[option] = user_choice

        else:
            user_password_length = get_user_password_length(option , default)
            print(user_password_length)
            settings[option] = user_password_length


def ask_if_change_settings(settings):
    while True:
        user_answer = input ('do you want to change default settings? (yes: y , no: n , enter: yes): ')
        if user_answer in ['y' , 'n' , '']:
            if user_answer in ['y' , '']:
                print('-'* 5 ,  'change settings',  '-'  * 5 , sep='')
                get_settings_from_user(settings)
            break
        else:
            print('invalid input')
            print('please try again')
        
        # if user_answer in ['y' , 'n' , '']:
        #     if user_answer == 'n':
        #         return False
        #     get_settings_from_user(settings)
        # else:
        #     print('invalid input')
        #     print('please try again')


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_symbol():
    return random.choice(string.punctuation)

def get_random_number():
    return random.choice(string.digits)


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'lower':
        # a = random.choice(string.ascii_lowercase)
        # return a
        return get_random_lower_case()
    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '




def password_generator(settings):

    final_password = ''

    password_length = settings['length']

    choices = list(filter(lambda x: settings[x] == True, ['lower' , 'upper'
     , 'number' , 'symbol' , 'space']))
    #  فیلتر چیزیه که ما باید روش حرکت بکنیم
    print(choices)

    # choices = []
    # for key , value in settings.items():
    #     if value and key != 'length':
    #         choices.append(key)
    # print(choices)

    for i in range(password_length):
        final_password += generate_random_char(choices)
        # final_password += 'a'

    return final_password


def ask_user_to_generate_another_password():
    while True:
        user_answer = input('regenerate? (yes: y , no: n , enter: yes) ')

        if user_answer in ['y' , 'n' , '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('invalid input')
            print('please try again')



def generate_password_loop(settings):
    while True:
        print('-'* 20)
        print(f'generated password: {password_generator(settings)}')
        

        if ask_user_to_generate_another_password() == False:
            break

        # while True:
        #     want_another_password = input('do you want another password? (yes: y) or (no: n) (enter: yes) ')
        #     if want_another_password in ['y' , 'n' , '']:
        #         if want_another_password == 'n':
        #             return 
        #         break
        #     else:
        #         print('invalid input. (choose from yes: y, no: n, enter: yes) ')    
        #         print('please try again')

        

def run_game():
    clear_screen()
    ask_if_change_settings(settings)
    generate_password_loop(settings)
    print('thank you for chooseing us')
    
    
run_game() 