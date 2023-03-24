import timeit

class Calculator():
    def __addition(self, first_num, second_num) -> int:
        """Addition Function

        Args:
            first_num (int): the first number
            second_num (int): the second number

        Returns:
            int: result of addition
        """
        return first_num + second_num

    def __substraction(self,first_num, second_num) -> int:
        return first_num - second_num

    def __multiplication(self,first_num, second_num) -> int:
        return first_num * second_num

    def __division(self, first_num, second_num) -> float:
        return first_num / second_num

    def run(self):
        while True:
            # User Inputs
            choice = int(
                input("""
Enter your choice

1 - Addition
2 - Substraction
3 - Multiplication
4 - Division

Your choice: """)
            )

            first_num = int(
                input(
                    "Enter first number: "
                )
            )
            second_num = int(
                input(
                    "Enter second number: "
                )
            )


            # starttime = timeit.default_timer()
            match choice:
                # Addition
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
            # print("The time difference for match case is :", timeit.default_timer() - starttime)  


calculator = Calculator()
calculator.run()
