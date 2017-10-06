import sys
import getopt

input_file = ''
infinite_loop = 999
MenuList = {1: 'Show File', 2: 'Add Account', 0: 'Exit'}


def show_menu():
    print('Choose option:')
    for item in sorted(MenuList):
        print(item, '-', MenuList.get(item))

    option = int(input())
    if option not in MenuList.keys():
        print('[ERR] - option not in list')
        return None

    return option


def main(argv):

    if len(argv) > 0:
        print('Working in console')
        try:
            opts, args = getopt.getopt(argv, "h:i:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print('AccountHolder.py -i <input_file>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print('AccountHolder.py -i <input_file>')
            elif opt in ('-i', '--ifile'):
                input_file = arg

        # draw menu
        user_option = infinite_loop
        while user_option != 0:
            user_option = show_menu()


    else:
        print('Working in window')


if __name__ == "__main__":
    main(sys.argv[1:])
