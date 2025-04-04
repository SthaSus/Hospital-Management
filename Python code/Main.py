# Hospital Management System Project
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():

    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC'),Patient('Tarr','Carlos', 21, '07087345678','B1 934')]
    discharged_patients = []

    while True:
        admin.login()
        print("---------Welcome---------")
        running = True 
        break
        
    while running:
        print('\nChoose the operation:')
        print(' 1- Admin : Register Doctor / View Doctor Details / Update doctor / Delete doctor')
        print(' 2- View Patient / Discharge patients / View discharged patients')
        print(' 3- Assign or Relocate Doctor to a Patient')
        print(' 4- Update admin details')
        print(' 5- Patient Family')
        print(' 6- Doctor: View Assigned Patients')
        print(' 7- Generate management report')
        print(' 8- Save to file and exit')

        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)  # Doctor management functionality

        elif op == '2':  
            while True:
                print("-----Active Patients-----")
                print("0 : Back")
                print("1 : View Patients and their assigned doctors")
                print("2 : Discard Patients")
                print("3 : View Discard Patients")
                op = input("Option:")

                if op == "0":
                    break
                
                elif op == '1':
                    print('ID |         Patient Name         |        Assigned Doctor       | Age |  Phone Number | Post Code')
                    admin.view(patients)
                        
                elif op == '2':    
                    op = input('Do you want to discharge a patient (Y/N): ').lower()
                    if op == 'yes' or op == 'y':
                        admin.view(patients)
                        patient_index = input('Please enter the patient ID to discharge: ')
                        try:
                            patient_index = int(patient_index) - 1  # Adjust for 0-based index
                            if 0 <= patient_index < len(patients):
                                discharged_patient = patients.pop(patient_index)
                                discharged_patients.append(discharged_patient)
                                print(f"Patient {discharged_patient.full_name()} has been discharged.")
                            else:
                                print('The id entered was not found.')
                        except ValueError:
                            print('The id entered is incorrect')

                    elif op == 'no' or op == 'n':
                        break 

                    else:
                        print('Please answer by yes or no.')
                        

                elif op == '3':
                    print("-----Discharged Patients-----")
                    if discharged_patients:
                        admin.view_discharge(discharged_patients)

                    else:
                        print("No patients have been discharged yet.")
                else:
                    print("Invalid option!! ")


        elif op == '3':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '4':
            admin.update_details(admin) 

        elif op == '5':
            for patient in patients:  # Loop through each patient in the list
                print(patient.get_surname(),)
                patient.get_family(patients)  # Call get_family for each patient

        elif op == '6':  # Doctor views assigned patients
            print("\n----- View Doctor's Patients -----")
            admin.view(doctors)
        
        elif op == '7':
            print("Choose Options")
            print("1- Total no of doctors")
            print("2- Total no of patients per doctor")
            print("3- Total no of patients based on illness")
            print("4- Number of appointment per month per doctor")
            op = input("Option: ")
            if op == '1':
                print(f'Total no of doctors are {len(doctors)}.')
                Doctor.plot_doctor_specializations(doctors)
                
            elif op == '2':
                print(f'Total no of patients per doctors are {len(patients)/len(doctors)}.')
                Doctor.plot_patients_per_doctor(doctors)

            elif op =='3':
                symptom_count = {}  # Dictionary to store symptom frequency
                for patient in patients:
                    for symptom in patient.get_symptoms():
                        if symptom in symptom_count:
                            symptom_count[symptom] += 1
                        else:
                            symptom_count[symptom] = 1
                # Print the results in "symptom : count" format
                for symptom, count in symptom_count.items():
                    print(f"{symptom} : {count}")
                Patient.plot_patients_per_illness(patients)

            elif op == '4':
                for doctor in doctors:
                    print(f"Doctor: {doctor.full_name()}")
                    print(f"Number of appointments: {len(doctor.get_appointments())}")
                Doctor.plot_appointments_per_doctor(doctors)
                
            else:
                print("wrong command")
                
        elif op == '8':
            # Save each patient's data to file
            for patient in patients:
                patient.save_to_file()  # Save patient data to file
            
            # Save each doctor's data to file
            for doctor in doctors:
                doctor.save_to_file()  # Save doctor data to file
                
            admin.save_to_file()
                
            print("Exiting the system...")
            running = False 

        else:
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
