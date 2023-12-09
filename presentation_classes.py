# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - presentation classes module
# # Description: A collection of classes for presenting data to the user
# ChangeLog: (Who, When, What)
# LBatista, 12.1.2023, created script
# LBatista, 12.8.2023, eliminated module dependencies
# ------------------------------------------------------------------------------------------------- #


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list[object]) -> list[object]:
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        LBatista,12.3.2023, Edited function for user readability

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list[object], employee_type: object) -> list[object]:
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        LBatista,12.3.2023, Edited function for user readability
        LBatista, 12.8.2023, Edited funtion to allow for name hyphens

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            while True:
                try:
                    employee_object.first_name = input("What is the employee's first name? ")
                    break
                except ValueError:
                    IO.output_error_messages("Employee's first name should not contain numbers. ")
            while True:
                try:
                    employee_object.last_name = input("What is the employee's last name? ")
                    break
                except ValueError:
                    IO.output_error_messages("Employee's last name should not contain numbers. ")
            while True:
                try:
                    employee_object.review_date = input("What is their review date? Please use YYYY-MM-DD formatting. ")
                    break
                except ValueError:
                    IO.output_error_messages("Please use correct date format: YYYY-MM-DD ")
            employee_object.review_rating = int(input("What is their review rating? Please chose a number 1-5. "))
            employee_data.append(employee_object)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data


if __name__ == '__main__':
    print("This file is not meant to be run; please run main.py")