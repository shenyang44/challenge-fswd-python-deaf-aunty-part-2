orewa = input("What's your name?\n")


def quiet():
    print(f'{orewa}, are you there?')
    count = 0
    while count < 2:
        new_reply = input('Say something:\n')

        if new_reply != '':
            aunty()
            break
        else:
            count += 1
            if count == 2:
                print('ok. Goodbye')
                break


def aunty():
    while True:
        reply = input('Speak to aunty:\n')
        if reply.islower():
            print("WHAT? SPEAK UP!")
        elif reply.isupper():
            print('YOU ARE VERY RUDE!')
        elif reply == ('I love you aunty, I have to go now'):
            print('ok. Goodbye')
            quiet()
            break
        else:
            print('SHOW SOME RESPECT!')


aunty()
