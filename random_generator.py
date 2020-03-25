import string
import random

digits = string.digits
ascii_lowercase = string.ascii_lowercase
ascii_uppercase = string.ascii_uppercase
specials = "!@#$%^"

def save_html(passwords):
    html = "<html><head></head><body><table><tbody>"
    for i, password in enumerate(passwords):
        html = html + "<tr><td>" + password + "</td></tr>"
    html = html + "</tbody></table></body></html>"
    f = open("passwords.html", "w")
    f.write(html)
    f.close()
        
def main():
    passwords = []
    for i in range(100):
        password = ""
        for i2 in range(3):
            password = password + random.choice(ascii_lowercase)
        for i3 in range(3):
            password = password + random.choice(ascii_uppercase)
        for i4 in range(3):
            password = password + random.choice(digits)
        for i5 in range(3):
            password = password + random.choice(specials)
        print(password)
        passwords.append(password)
    #save
    save_html(passwords)
    
if __name__ == "__main__":
    main()