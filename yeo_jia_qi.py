### A login function
## Requirements:
# CLI only
# Allow only 3 attempt
# Assume validations needed for both username and password

## Least
# Conditional
# Uses of function
# Object oriented

class Login:
    def main(self):
        login = False
        x = 0

        def _login(username, password) -> bool:
            if (username == "admin") & (password == "password"):
                return True
            else:
                return False

        while login == False:
            if x == 3:
                print("Login limitation reached.")
                break

            username = input("Username: ")
            password = input("Password: ")

            if (username == "") | (password == ""):
                print("Do not leave blanks. Please try again.")
            else:
                login = _login(username, password)
                if login == True:
                    print("Login successful.")
                    break
                else:
                    print("Login failed.")

            x += 1

user = Login()
user.main()

        

        

