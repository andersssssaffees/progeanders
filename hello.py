import sys


def main():
    if len(sys.argv) >= 3:
        name = sys.argv[1]
        city = sys.argv[2]
    else:
        print('Mis Su nimi on?')
        name = input()
        city = input('Millises linnas sa elad? ')

    print('Hello', name, 'from', city)
    print('Hello ' + name + ' from ' + city)

    print(sys.argv)
    print('Tere', name)


if __name__ == '__main__':
    main()

