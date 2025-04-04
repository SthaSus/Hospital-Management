from Common import Common
import matplotlib.pyplot as plt
from collections import Counter

class Doctor(Common):
    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name, surname)  # Initialize Common class
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    # FOR GUI starts   ################ 
    def assigned_patients(self, patient):
        if patient not in self.__patients:
            self.__patients.append(patient)

    def get_assigned_patients(self):
        return self.__patients
    
    def remove_patient(self, patient):
        """Remove a patient from the doctor's list."""
        if patient in self.__patients:
            self.__patients.remove(patient)

    # For GUI ends #######################

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
    
    def add_patient(self, patient):
        """Adds a patient to the doctor's list and links the patient to this doctor."""
        if patient not in self.__patients:  # Avoid duplicates
            self.__patients.append(patient)
            self.__patients.sort(key=lambda p: p.full_name())  # Sort by name
            patient.link(self)  # Link the patient to this doctor
            
    def get_patients(self):
        """Returns a list of patient names assigned to this doctor."""
        return [patient.full_name() for patient in self.__patients]  # Returns names
    
    def add_appointments(self, appointment):
        self.__appointments.append(appointment)
        self.__appointments.sort()
        print(self.__appointments)

    def __str__(self):
        patient_names = ', '.join(self.get_patients()) if self.__patients else "No patients"
        return f'{self.full_name():^30}|{self.__speciality:^15}| Patients: {patient_names}'

    def save_to_file(self, filename="doctor.txt"):
        """Saves the doctor's details to a text file."""
        with open(filename, 'a') as file:  # Open the file in append mode
            file.write(f"Doctor Information:\n")
            file.write(f"Full Name: {self.full_name()}\n")
            file.write(f"Specialty: {self.get_speciality()}\n")
            file.write(f"Patients: {', '.join(self.get_patients()) if self.get_patients() else 'None'}\n")
            file.write(f"Appointments: {', '.join(self.__appointments) if self.__appointments else 'None'}\n")
            file.write("-" * 50 + "\n")  # Add a separator between doctor records

    # In doctor.py, inside the Doctor class
    def get_appointments(self):
        return self.__appointments

    def plot_doctor_specializations(doctors):
        # Count the number of doctors per specialization
        specializations = [doctor.get_speciality() for doctor in doctors]
        specialization_counts = Counter(specializations)

        # Extract labels and values for the pie chart
        labels = specialization_counts.keys()
        sizes = specialization_counts.values()

        # Plot the pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        plt.title('Distribution of Doctors by Specialization')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()

    def plot_patients_per_doctor(doctors):
        doctor_names = [doctor.full_name() for doctor in doctors]
        patient_counts = [len(doctor.get_patients()) for doctor in doctors]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(doctor_names, patient_counts, color='skyblue')

        plt.xlabel('Doctors')
        plt.ylabel('Number of Patients')
        plt.title('Number of Patients Per Doctor')
        plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

        # Add labels on top of bars
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    str(int(bar.get_height())), ha='center', va='bottom', fontsize=12)

        plt.show()

    def plot_appointments_per_doctor(doctors):
        doctor_names = [doctor.full_name() for doctor in doctors]
        appointment_counts = [len(doctor.get_appointments()) for doctor in doctors]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(doctor_names, appointment_counts, color='skyblue')

        plt.xlabel('Doctor')
        plt.ylabel('Number of Appointments')
        plt.title('Number of Appointments per Doctor')
        plt.xticks(rotation=45, ha='right')  # Rotate labels for readability

        # Add labels on top of bars
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    str(int(bar.get_height())), ha='center', va='bottom', fontsize=12)

        plt.tight_layout()
        plt.show()
