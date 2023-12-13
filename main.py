# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - main file
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# LBatista, 12.1.2023, created script
# LBatista, 12.3.2023, edited script for readability
# ------------------------------------------------------------------------------------------------- #
from data_classes import FILE_NAME, MENU, employees, Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Beginning of the main body of this script
try:
    employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name (ignore the warning)
except Exception as e:
    IO.output_error_messages("Got an exception reading from file", e)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)

        except Exception as e:
            IO.output_error_messages("Got an exception displaying employee data.", e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages("Got an exception inputting employee data.", e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages("Got an exception writing the data to file.", e)
        continue

    elif menu_choice == "4":  # End the program
        print("Goodbye! ")
        break  # out of the while loop
    else:
        IO.output_error_messages("I did not understand that command.")