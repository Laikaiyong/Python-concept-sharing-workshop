class Login:
    def __validate_username(self, username) -> bool:
        """Username validation

        Args:
            username (str): Inserted username

        Returns:
            bool: validated result
        """
        return username == "Vandyck"
    
    def __validate_password(self, password) -> bool:
        """Password Validation

        Args:
            password (str): Inserted password

        Returns:
            bool: validated result
        """
        return password == "12345"
    
    def run(self) -> None:
        for attempt in range(1, 4):
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            
            if self.__validate_username(username) and self.__validate_password(password):
                print("Login successfully")
                break
            
            if attempt == 3:
                print("Attempt exhausted, please try again after 1937297392971 years")

loginController = Login()
loginController.run()