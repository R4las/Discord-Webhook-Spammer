from colorama import Fore
import requests
import time

print(' ')
print('                                                    WEBHOOK SPAMMER                        ')
time.sleep(0.3)
print((' '))

webhook = input("[>] Enter The Webhook Link: ")
message = input("[>] Enter The Message: ")
delay = float(input("[>] Enter The Delay (EX: 0.1): "))
spam = input('[>] Enter The Threads: ')
spam = int(spam)
print('')




while spam:

    print("Sending -> " + message)
    try:
        time.sleep(delay)
        _data = requests.post(webhook, json={'content': message})

        if _data.status_code == 204:
            print("Sent -> " + message)
            print(' ')

    except:
        print("Something Happend! | Probably Broken Webhook -> " + webhook)
        time.sleep(5)
        exit()

    spam = spam -1

input('Press enter 3 times for close')
input('2')
input('1')




