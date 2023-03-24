### A login function
## Requirements:
# CLI only
# Allow only 3 attempt
# Assume validations needed for both username and password

## Least
# Conditional
# Uses of function
# Object oriented


class login:
    username = "hongwei"
    password = "aaaaaa"
    attempt = 3

    def __credentialCheck(self, username, password) -> bool:
        if self.attempt > 3:
            print("You're not able to login anymore(Attempt left: 0)")
            return False
        elif username == self.username and password == self.password:
            return True
        else:
            self.attempt -= 1
            print(f"Nice try (Attempt left: {self.attempt})\n")
            return False

    def run(self,
            username="",
            password="") -> None:

        print(
            f"""
Login to get Google Swag
({self.attempt} attempts only)
            """
        )

        while (self.attempt > 0):
            username = input("Username: ")
            password = input("Password: ")

            if (self.__credentialCheck(username, password)):
                print("\nCongratulation, just joking")
                break


login = login()
login.run()