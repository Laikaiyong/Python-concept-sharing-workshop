# ## A login function
# # Requirements:
# CLI only
# Allow only 3 attempt
# Assume validations needed for both username and password
from typing import Dict


class Login:
    user_name: str = "Vandyck Daddy"
    password: str = "I want the lanyard"
    login_status: Dict[str, str] = {
        "status": "",
        "message": ""
    }
    attempt: int = 1

    def __check_attempt(self) -> bool:
        return self.attempt < 4

    def __check_match(self, user_name: str, password: str) -> bool:
        if user_name == self.user_name and password == self.password:
            return True
        else:
            return False

    @staticmethod
    def __display_message(status: str, message: str) -> None:
        print(f"""
Login {status}.
Message: {message}.      
        """)

    def __login(self) -> None:
        while self.__check_attempt():
            if self.login_status["status"] == "SUCCESS":
                return
            print(f"**************************************\n\n"
                  f"Login attempt: {self.attempt}")
            user_name = input("User Name: ")
            password = input("Password: ")
            self.attempt += 1
            if user_name == "" or password == "":
                self.login_status["status"] = "FAIL"
                self.login_status["message"] = "No input"
            elif self.__check_match(user_name, password):
                self.login_status["status"] = "SUCCESS"
                self.login_status["message"] = "Yay! Successfully login."
            else:
                self.login_status["status"] = "FAIL"
                self.login_status["message"] = "Invalid Credential"

            self.__display_message(self.login_status["status"], self.login_status["message"])

    def run(self) -> None:
        print(
            """
Welcome user. Please enter your login credential.
You'll only have 3 attempts. 
*Case sensitive*
            """
        )
        self.__login()


login = Login()
login.run()
