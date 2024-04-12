# imports the class Stocks from aktier.py
import aktier
from webdata import fundamental_analysis_yf
from webdata import technical_analysis_yf

fundamenta_file = "fundamenta.txt"
omx_file = "omx.txt"

# save stocks in dictionary: Name: highest(price), lowest(price), highest(date), lowest(date)
beta_list = []
# list consists of Name, the highest price, the lowest price, highest date, lowest date, solidity, p/e, p/s
stocks_list_of_lists = []
class_dict = {}


# Currently, this function only works for 90 days. Not 30!
def beta_omx(file):
    # Opens txt file
    read_file = open(file, 'r')
    content = read_file.read()
    content_list = content.split()
    read_file.close()
    # Remove unnecessary information from txt file
    content_list.pop(0)
    content_list.pop(0)
    content_list.pop(0)

    # Rounds the quota of the last price and the first price in the list
    beta = round(float(content_list[-1]) / float(content_list[1]), 2)
    return beta


# Reads "kurser.txt" and makes a content list
def file_to_list(file):
    # Opens txt file
    read_file = open(file, 'r')
    content = read_file.read()
    content_list = content.split()
    # stop reading file
    read_file.close()
    # saves data in lists depending on the stock, stock-date-price
    return content_list


# Reads the file "kurser.txt" & gets the highest and lowest prices and respective dates for each stock
def create_stock_dict(kurser_file):
    content_list = file_to_list(kurser_file)
    # Remove unnecessary information from txt file
    for i in range(0, 3):
        content_list.pop(0)
    stocks = []
    growth = []
    highest_price = 0
    lowest_price = 1000000.00

    highest_prices = []
    lowest_prices = []
    i = 0
    for line in content_list:
        # if line is stock name
        stock_nr = len(stocks) - 1

        # date
        if "-" in line:
            date = line

        # price
        elif line.replace('.', '', 1).isdigit():
            price = float(line)
            # check if price is higher than last
            if price > highest_price:
                highest_price = price
                highest_prices[stock_nr] = price
            # check if price is lower than last
            if price < lowest_price:
                lowest_price = price
                lowest_prices[stock_nr] = price
        # new stock name
        elif any(c.isalpha() for c in line):
            stock = line
            stocks.append(stock)
            # set new list item for highest and lowest price lists
            highest_prices.append(0.0)
            lowest_prices.append(0.0)
            # reset highest and lowest price values
            highest_price = 0
            lowest_price = 1000000.00

            # growth
            first_price = content_list[i + 2]
            last_price = content_list[i + 134]
            temp_growth = float(last_price) / float(first_price)
            growth.append(str(round(temp_growth, 2)))

            # BETA
            # Creates dictionary of dictionaries for the beta number
            # We know that the first price for each stock is two lines after its name
            # We know that it is 132 lines between the first and last price for each stock
            omx = beta_omx(omx_file)
            beta = round(temp_growth / omx, 2)
            beta_list.append(beta)

        i += 1

    # find dates for respective highest and lowest price
    highest_dates = []
    lowest_dates = []
    i = 0
    for line in content_list:
        if line.replace('.', '', 1).isdigit():
            if float(line) in highest_prices:
                highest_dates.append(content_list[i - 1])
            if float(line) in lowest_prices:
                lowest_dates.append(content_list[i - 1])

        i += 1

    # Finally, we need to save everything in dictionaries
    for i in range(0, len(stocks)):
        stock_list = [stocks[i], highest_prices[i], lowest_prices[i], highest_dates[i], lowest_dates[i], beta_list[i],
                      growth[i]]
        # appends the list to lists of lists
        stocks_list_of_lists.append(list(stock_list))

    return stocks_list_of_lists


def create_fundamental(file):
    # Opens txt file
    content_list = file_to_list(file)
    # Remove unnecessary information from txt file
    for i in range(0, 5):
        content_list.pop(0)
    i = 0
    y = 0
    for line in content_list:
        # Format: 1.company name, 2.solidity, 3.p/e, 4.p/s
        i += 1
        if i == 1:
            name = line
        elif i == 2:
            solidity = line
        elif i == 3:
            pe = line
        elif 4:
            ps = line
            fundamental_list = [solidity, pe, ps]
            # saves everything into the stock list of lists
            for x in range(len(fundamental_list)):
                stocks_list_of_lists[y].append(fundamental_list[x])
            # reset loop
            i = 0
            y += 1


# convert the list to dictionary related to each stock
def convert_list_dictionary(full_list):
    i = 0
    while i < (len(full_list)):
        class_dict[full_list[i][0]] = aktier.Stock(full_list[i][0], full_list[i][1], full_list[i][2],
                                                   full_list[i][3], full_list[i][4], full_list[i][5],
                                                   full_list[i][6], full_list[i][7], full_list[i][8],
                                                   full_list[i][9])
        i += 1


def stock_option():
    try:
        while True:
            # This list is to assign each stock name to an integer
            temp_list = []
            i = 1
            # Goes through each key (name) in the class dictionary
            for key in class_dict.keys():
                print(i, key)
                temp_list.append(key)
                i += 1
            option = int(input("Which option do you want to choose?")) - 1
            # if the option chosen is smaller than the list, then successful
            if -1 < option < i - 1:
                return temp_list[option]
            # if the option chosen is bigger than the list, then try loop again
            else:
                print("The value is not in the amount. Try again!")

    except ValueError:
        print("You have to choose an integer!")


# Get ranking of stocks depending on their beta value:
def ranking():
    # Store the names in a list so that we don't just get the beta number but also the stock
    temp_list = []
    temp_beta_list = []
    for key in class_dict.keys():
        temp_list.append(key)
        temp_beta_list.append(class_dict[key].beta)

    # Sort both lists by highest number based on the beta worth
    # Got this following (1) row of code from Stack Overflow and remade it to fit my purpose
    # https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
    rank = [x for _, x in sorted(zip(temp_beta_list, temp_list), reverse=True)]

    return rank


def actual_stock_information():
    # Get the stock data for a specific ticker
    ticker = input("Stock ticker: ")

    while True:
        option = input('''Choose an option:
            F. Fundamental Analysis
            T. Technical Analysis
            C. Choose a different stock
            Q. Quit''')

        option = option.lower()
        if option not in ['f', 't', 'c', 'q']:
            print('You have to answer with an integer between 1 and 4!')
        elif option == 'f':
            return fundamental_analysis_yf(ticker)
        elif option == 't':
            return technical_analysis_yf(ticker)
        elif option == 'c':
            return actual_stock_information()
        elif option == 'q':
            return exit()


def continue_quit():
    while "the answer is invalid":
        reply = str(input('Continue? (Y/N): ')).lower().strip()
        if reply[0] == 'y':
            menu()
        if reply[0] == 'n':
            exit()


def type_choice():
    while True:
        try:
            input_choice = int(input('Which option do you want to choose? '))
            if input_choice < 1 or input_choice > 4:
                print('You have to answer with an integer!')
            elif input_choice == 1:
                print('A fundamental analysis can be made of following stocks:')
                option = stock_option()
                # If option is bigger than the amount of stocks, then it will produce an error
                # Therefore we need error handling:
                return class_dict[option].fundamental_analysis()
            elif input_choice == 2:
                print('A technic analysis can be made of following stocks:')
                option = stock_option()
                return class_dict[option].technical_analysis()
            elif input_choice == 3:
                print('Ranking of stocks by their beta value: ')
                # prints the ranking list without brackets
                print(*ranking())
                i = 1
                rank_list = ranking()
                for rank in rank_list:
                    # example: 1 Ericsson 2.65
                    print(i, rank, class_dict[rank].beta)
                    i += 1
                continue_quit()
            elif input_choice == 4:
                return actual_stock_information()
            elif input_choice == 5:
                exit()
        except ValueError:
            print('You have to answer with an integer given in the list!')
        except KeyError:
            print('You have to answer with an integer!')


def menu():
    while True:
        print("""
        —————————Menu———————————
    1.Fundamental analysis (long time holding)
    2.Technical analysis (short time holding)
    3.Ranking of stocks based on their beta value
    4.Stocks on the internet
    5.Quit""")
        type_choice()
        continue_quit()


create_stock_dict("kurser.txt")
create_fundamental(fundamenta_file)

convert_list_dictionary(stocks_list_of_lists)

#menu()
actual_stock_information()


