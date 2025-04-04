from Doctor import Doctor
from Patient import Patient

class Admin:

    def __init__(self, username, password, address = ''):
        self.__username = username
        self.__password = password
        self.__address =  address  
        # FOR GUI starts
        self.name = username
        self.password = password
        self.address = address
        # For GUI ends
    
    # For GUI starts here
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address
    # For GUI ends here

    def view(self, a_list):
        """Print a list of items with index."""
        for index, item in enumerate(a_list):
            if item is not None:
                print(f'{index+1:3}|{item}')
            else:
                print(f'{index+1:3}|[Empty or Invalid Item]')

    def login(self) :
        print("---------Login---------")
        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        while username != self.__username or password != self.__password:
            print("Incorrect username or password please try again.")
            username = input('Enter the username: ')
            password = input('Enter the password: ')
            
    def save_to_file(self, filename="admin.txt"):
        """Saves the admin's details to a text file."""
        with open(filename, 'a') as file:  # Open the file in append mode
            file.write(f"Admin Information:\n")
            file.write(f"Username: {self.get_name()}\n")
            file.write(f"Password: {self.get_password()}\n")
            file.write(f"Address: {self.get_address()}\n")
            file.write("-" * 50 + "\n")  # Add a separator between doctor records

    def find_index(self,index,doctors):
            
        if index in range(0,len(doctors)):
            return True

        else:
            return False
            
    def get_doctor_details(self,doctors) :

        print("-----Update Doctor`s Details-----")
        print('ID |          Full name           |  Speciality')
        self.view(doctors)
        

    def doctor_management(self, doctors):
        while True:
            print("-----Doctor Management-----")

            # menu
            print('Choose the operation:')
            print(' 0 - Back')
            print(' 1 - Register Doctor')
            print(' 2 - View Doctor Details')
            print(' 3 - Edit Doctor Info')
            print(' 4 - Remove Doctor')
            op = input('Option: ')

            # register
            if op == '0':
                break
            
            elif op == '1':
                print("-----Registering Doctor-----")

                print('Enter the doctor\'s details:')
                first_name = input("Enter first name:")
                surname = input("Enter surname:")
                specs = input("Enter specification:")
                name_exist=False
                
                for doctor in doctors:
                    if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                        print('Name already exists.')
                        name_exist = True
                        
                if not name_exist:
                    doctors.append(Doctor(first_name,surname,specs))
                    # for doctor in doctors:
                    #     a = open('doctors.txt','a+')
                    #     a.write(Doctor(first_name,surname,specs))
                    #     a.close()
                    print('Doctor registered.')
                    
            elif op == '2':
                print("-----List of Doctors-----")
                print('ID |          Full name           |  Speciality   |     Patients')
                self.view(doctors)
                print('\n')
                

            # Update
            elif op == '3':
                next = True
                while next == True:
                    print("-----Update Doctor`s Details-----")
                    print('ID |          Full name           |  Speciality   |     Patients')
                    self.view(doctors)
                    new = input("Do you wish to continue y/n ")
                    if new.lower() == 'n':
                        break
                    elif new.lower() == 'y':
                        try:
                            index = int(input('Enter the ID of the doctor: ')) - 1
                            doctor_index=self.find_index(index,doctors)
                            if doctor_index == True:
                                # menu 
                                print('Choose the field to be updated:')
                                print(' 0 Back')
                                print(' 1 First name')
                                print(' 2 Surname')
                                print(' 3 Speciality')
                                op = int(input('Input: ')) # make the user input lowercase
                                
                                if op == '0':
                                    continue
                                
                                elif op == 1:
                                    first_name = input("Enter first name ")
                                    doctors[index].set_first_name(first_name)
                                
                                elif op == 2:
                                    surname = input("Enter Surname: ")
                                    doctors[index].set_surname(surname)

                                elif op ==3:
                                    spec = input("Enter Speciality: ")
                                    doctors[index].set_speciality(spec)
                                    
                                else:
                                    print("Invalid option")
                                
                            else:
                                print("Doctor not found")

                        except ValueError: # the entered id could not be changed into an int
                            print('The ID entered is incorrect')
                    else:
                        print("Invalid option. ")


            # Delete
            elif op == '4':
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)

                try:
                    doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1

                    if self.find_index(doctor_index, doctors):  # Check if the doctor exists
                        confirmation = input(f"Are you sure you want to delete Dr. {doctors[doctor_index].full_name()}? (yes/no): ").lower()
                        if confirmation.lower() == 'yes':
                            del doctors[doctor_index]  # Delete the doctor from the list
                            print('Doctor deleted successfully.')
                        else:
                            print('Deletion cancelled.')

                    else:
                        print('Doctor not found.')

                except ValueError:
                    print('Invalid ID format. Please enter a valid number.')

            else:
                print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        Print a list of patients
        Args:
            patients (list<Patient>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patient>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        self.view_patient(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1  # Adjust for 0-based indexing

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return

        except ValueError:
            print('The id entered is incorrect')
            return

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms()
        
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        for idx, doctor in enumerate(doctors, 1):
            print(f"{idx:^3}| {doctor.full_name():<30} | {doctor.get_speciality():<12}")

        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1  # Adjust for 0-based indexing

            if doctor_index not in range(len(doctors)):
                print('The ID entered was not found.')
                return
            
            # Link the patient to the selected doctor
            selected_patient = patients[patient_index]
            selected_doctor = doctors[doctor_index]

            selected_doctor.add_appointments(selected_patient.full_name())  # Store patient name instead of object

            selected_patient.link(selected_doctor)  # Assign doctor to patient
            selected_doctor.add_patient(selected_patient)  # Assign patient to doctor
            print(f'The patient {selected_patient.full_name()} is now assigned to Dr. {selected_doctor.full_name()}.')


        except ValueError:
            print('The id entered is incorrect')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patient>): the list of all the active patients
            discharge_patients (list<Patient>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        try:
            patient_index = int(patient_index) - 1  # Adjust for 0-based indexing

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return

            discharged_patient = patients.pop(patients[patient_index])
            discharge_patients.append(discharged_patient)
            print(f"Patient {discharged_patient.full_name()} has been discharged.")

        except ValueError:
            print('The id entered is incorrect')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharged_patients (list<Patient>): the list of all the non-active patients
        """
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details(self, admin):
        """
        Allows the user to update and change username, password and address
        """
        while(True):
            print('Choose the field to be updated:')
            print(' 1 Username')
            print(' 2 Password')
            print(' 3 Address')
            op = int(input('Input: '))

            if op == 1:
                username = input('Enter the new username: ')
                admin.set_name(username)
                break

            elif op == 2:
                password = input('Enter the new password: ')
                if password == input('Enter the new password again: '):
                    admin.set_password(password)
                    break
            elif op == 3:
                address = input('Enter the new address: ')
                admin.set_address(address)
                break
    
            else:
                print("Invalid option")