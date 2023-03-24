import timeit
import random

class Calculator:
    def __addition(self, first_num, second_num) -> int:
        """Adding numbers

        Args:
            first_num (int): first number to pass in
            second_num (int): second number to pass in

        Returns:
            int: total sum
        """
        return first_num + second_num
    
    
    def __substraction(self, first_num, second_num) -> int:
        """Additing numbers

        Args:
            first_num (int): first number to pass in
            second_num (int): second number to pass in

        Returns:
            int: substraction result
        """
        return first_num - second_num
    
    
    def __multiplication(self, first_num, second_num) -> float:
        """Multiplying numbers

        Args:
            first_num (int): first number to pass in
            second_num (int): second number to pass in

        Returns:
            float: multiplied product
        """
        return first_num * second_num
    
    
    def __division(self, first_num, second_num) -> float:
        """Dividing numbers

        Args:
            first_num (int): first number to pass in
            second_num (int): second number to pass in

        Returns:
            float: divided number
        """
        return first_num / second_num
        

    def run(
        self,
        choice = 0,
        first_num = 0,
        second_num = 0,
        test = False
    ) -> None:
        while True:
            try:
                if not test:
                    choice = int(
                        input(
                            """
Calculator
        
    1: addition (+)
    2: substraction (-)
    3: multiplication (*)
    4: division (/)
    
Select calculator operation:"""
                        )
                    )
                    
                    first_num = int(
                        input(
                            "First number: "
                        )
                    )
                    second_num = int(
                        input(
                            "Second Number: "
                        )
                    )
                
            except:
                raise Exception("Calculation input error, something went wrong")
            
            
            starttime = timeit.default_timer()
            print("The start time for match case :",starttime)
            match choice:
                case 1:
                    print("Addition processing for number " + str(first_num) + " and " + str(second_num))
                    
                    sum_num = self.__addition(first_num, second_num)
                    print(f"\nSum: {sum_num}\n\n")
                case 2:
                    print(f"Substraction processing for number {first_num} and {second_num}")
                                        
                    substracted_num = self.__substraction(first_num, second_num)
                    print(f"\nMinus result: {substracted_num}\n\n")
                case 3:
                    print("Multiplication processing for number {} and {}".format(first_num, second_num))
                                        
                    multiplied_num = self.__multiplication(first_num, second_num)
                    print(f"\nmultiplied: {multiplied_num}\n\n")
                case 4:
                    print("Division processing for number {1} and {0}".format(second_num, first_num))
                                        
                    divided_num = self.__division(first_num, second_num)
                    print(f"\nDivision: {divided_num}\n\n")
                case _:
                    print("Invalid choice")           
            print("The time difference for match case is :", timeit.default_timer() - starttime)

            if test:
                break

            starttime = timeit.default_timer()
            print("The start time for if else :",starttime)
            if choice == 1:
                print("Addition processing for number " + str(first_num) + " and " + str(second_num))                
            elif choice == 2:
                print(f"Substraction processing for number {first_num} and {second_num}")
            elif choice == 3:
                print("Multiplication processing for number {} and {}".format(first_num, second_num))          
            elif choice == 4:
                print("Division processing for number {} and {}".format(first_num, second_num))               
            else:
                print("Invalid choice")      
            print("The time difference for if else is :", timeit.default_timer() - starttime)
    
    def test_run(self) -> None:
        choice = random.choice([1, 2, 3, 4])
        first_num = int(random.random() * 100)
        second_num = int(random.random() * 100)
        
        self.run(
            choice = choice,
            first_num = first_num,
            second_num = second_num,
            test = True
        )
        
        
        

calculator = Calculator()
calculator.test_run()
calculator.run()
# Can make it more user friendly using tkinter or kivy library to create GUI
# Web library - flask, django