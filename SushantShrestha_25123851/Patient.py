from Common import Common
import matplotlib.pyplot as plt
from collections import Counter

class Patient(Common):
    def __init__(self, first_name, surname, age, mobile, postcode):
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms = ['depression']
        self.__familylst = []
        self.__symptom_family = []
        
        # For GUI starts ###########
        self.first_name = first_name
        self.last_name = surname
        self.age = age
        self.contact = mobile
        self.address = postcode
        self.assigned_doctor = None  # Initialize as None
        # FOR GUI ends ###############

    # For GUI  ##################
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor  # Assign the doctor to the patient

    def get_assigned_doctor(self):
        return self.assigned_doctor  # Return the assigned doctor, if any

    def get_family1(self, patient):
        # Example function to show family details for the patient
        print(f"Family details for {self.full_name()}:")
        for family_member in patient:
            if family_member.get_surname() == self.get_surname():
                self.__familylst.append(family_member.get_first_name() + ", " + family_member.get_surname())
        print(self.__familylst)  # Placeholder for family details
    # For GUI ends ################

    def get_family(self,patients):
        for patient in patients:
            if patient.get_surname() == self.get_surname():  # Check if surnames match and it's not the same patient
                self.__familylst.append(patient.get_first_name() + ", " + patient.get_surname())
        print(self.__familylst)
         
    def get_symptomsfamily(self):
        return self.__symptom_family
    
    def sort_symptoms(self,patient):
        if self.__symptoms == patient.get_symptoms():
            self.__symptom_family.append(self.full_name())
        return self.get_symptomsfamily()
    

    def add_symptoms(self,symptom):
        self.__symptoms.append(symptom)

    def get_symptoms(self):
        return self.__symptoms
    
    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def add_doctor(self,doctor):
        self.__doctor = doctor
    
    def get_doctor(self): # CHECK
        return self.__doctor if isinstance(self.__doctor, str) else self.__doctor.full_name()

    def full_name(self):
        return f"{self.get_first_name()} {self.get_surname()}"
    
    def link(self, doctor):
        self.__doctor = doctor

    def print_symptoms(self):
        if self.__symptoms == None:
            print(f"{self.full_name()} has no recorded symptoms.")
            
        elif self.__symptoms:
            print(f"Symptoms of {self.full_name()}: {', '.join(self.__symptoms)}")
            
        else:
            print(f"{self.full_name()} has no recorded symptoms.")

    def __str__(self):
        return f'{self.full_name():^30}|{self.get_doctor():^30}|{self.get_age():^5}|{self.get_mobile():^15}|{self.get_postcode():^10}'
    
    def save_to_file(self, filename="patient.txt"):
        with open(filename, 'a') as file:  # Open the file in append mode
            file.write(f"Patient Information:\n")
            file.write(f"Full Name: {self.full_name()}\n")
            file.write(f"Doctor: {self.get_doctor()}\n")
            file.write(f"Age: {self.get_age()}\n")
            file.write(f"Mobile: {self.get_mobile()}\n")
            file.write(f"Postcode: {self.get_postcode()}\n")
            file.write(f"Symptoms: {', '.join(self.get_symptoms())}\n")
            file.write(f"Family Members: {', '.join(self.__familylst) if self.__familylst else 'None'}\n")
            file.write("-" * 50 + "\n")  # Add a separator between patient records

    def plot_patients_per_illness(patients):
        illness_counts = Counter([illness for patient in patients for illness in patient.get_symptoms()])
        # Extract illness names and counts
        illnesses = list(illness_counts.keys())
        counts = list(illness_counts.values())
        plt.figure(figsize=(10, 6))
        bars = plt.bar(illnesses, counts, color='lightcoral')

        plt.xlabel('Illness')
        plt.ylabel('Number of Patients')
        plt.title('Total Number of Patients Per Illness')
        plt.xticks(rotation=45, ha='right')  # Rotate labels for readability
        # Add labels on top of bars
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    str(int(bar.get_height())), ha='center', va='bottom', fontsize=12)
        plt.show()
