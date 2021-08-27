with open('info.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)

website = input("Enter the website or app the password is for: ")
username = input('Enter the username:')
password = input('Enter the password: ')

with open("info.txt", "a") as f:
    f.write("-----" + "\n" + "Website:" + website + "\n")
    f.write("Username:" + username + "\n")
    f.write("Password:" + password)

with open('info.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)