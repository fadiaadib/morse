"""
    A text-based Python program to convert Strings into Morse Code.
"""
from morse import Morse
from banner import banner


def main():
    morse = Morse()
    print(banner)
    print('Welcome to the Morse Code generator!')

    loop_on = True
    while loop_on:
        morse.text = input('Enter the text to encode, or "q" to quit: \n')
        if morse.text == 'q':
            loop_on = False
        else:
            morse.encode()
            morse.show()
            morse.play()
    else:
        print('Goodbye!!')


if __name__ == '__main__':
    main()
