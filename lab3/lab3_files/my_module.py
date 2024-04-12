import text_encryption_function


# Uppgift 1

def copy_text_file(in_file, out_file):
    rf = open(in_file, 'r')
    wf = open(out_file, 'w')
    for line in rf:
        wf.write(line)
    rf.close()
    wf.close()


# --------------------------------------------------------------------------------------------------
# Uppgift 2

def encrypt_file(in_file, out_file):
    rf = open(in_file, 'r')
    encryptf = open(out_file, 'w')
    for line in rf:
        encryptf.write(text_encryption_function.encrypt(line))


encrypt_file("namn.csv", "secret_names.csv")

# --------------------------------------------------------------------------------------------------
# Uppgift 3

def user_dialogue():
    while True:
        in_file = input("name of existing file: ")
        out_file = input("name of new encrypted file: ")
        try:
            encrypt_file(in_file, out_file)
            break
        except FileNotFoundError as error:
            print("That resulted in an input/output error, please try again! Details: ", error)


# --------------------------------------------------------------------------------------------------
# Uppgift 4

def get_int_input(prompt_string):
    while True:
        try:
            heltal = input(prompt_string)
            int(heltal)
            return heltal
            break
        except ValueError:
            print("Svara med ett heltal!")


get_int_input("Ange ett heltal:")

# Uppgift 5

short_quiz_list_of_lists = ['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn',
                            'Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']


def quiz():
    fact = [1, 1]
    points = 0
    counter = 0

    print('-----------------------')
    print('Välkommen till Quizzet!')
    print('-----------------------')

    for i in range(0, len(short_quiz_list_of_lists) - 1, 4):
        print(short_quiz_list_of_lists[i])
        print('1: ', short_quiz_list_of_lists[i + 1], '2: ', short_quiz_list_of_lists[i + 2], '3: ',
              short_quiz_list_of_lists[i + 3])
        answer = get_int_input("Svar: ")

        if answer == str(fact[counter]):
            print('Rätt! Det var: ', short_quiz_list_of_lists[i + fact[counter]])
            points += 1

        else:
            print('Fel svar... Rätt svar var: ', short_quiz_list_of_lists[i + fact[counter]])
        counter += 1
        print('-----------------------')

    print('Du fick totalt ', points, ' poäng! Grattis!')


quiz()


# --------------------------------------------------------------------------------------------------
# Uppgift 6

def get_quiz_list_handle_exceptions():
    long_string = ''
    bad_question_list = []
    good_question_list = []

    # Loops the try catch
    while True:
        # Tries input for quiz file
        try:
            in_file = input('Name of quiz-file: ')
            rf = open(in_file, 'r')

            for line in rf:
                long_string += line
                bad_question_list.append(line)
            break

        except FileNotFoundError as error:
            print("That resulted in an input/output error, please try again! Details: ", error)

    # Strips and splits each row in the quiz to remove unnecessary ; and \n
    for element in bad_question_list:
        try:
            stripped_line = element.strip('\n')
            split_line = stripped_line.split(';')
            good_question_list.append(split_line)
        except SyntaxError as error:
            print('The file is not made for this function! Details: ', error)
    return good_question_list


get_quiz_list_handle_exceptions()

# --------------------------------------------------------------------------------------------------
# Uppgift 7

#quiz(get_quiz_list_handle_exceptions())