# HOSPITAL MANAGEMENT SYSTEM WITH GUI

import tkinter as tk
from tkinter import messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        
        # Create Admin, Doctors, and Patients
        self.admin = Admin('admin', '123', 'B1 1AB')
        self.doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone', 'Carlos', 'Cardiology')]
        self.patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'), 
                         Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'), 
                         Patient('Daivd', 'Smith', 15, '07123456789', 'C1 ABC')]
        self.discharged_patients = []

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Main Menu
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="--------- Welcome ---------", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.main_frame, text="1 - Admin : Register Doctor / View Doctor Details", command=self.manage_doctors).pack(fill=tk.X)
        tk.Button(self.main_frame, text="2 - View Patient / Discharge Patients", command=self.manage_patients).pack(fill=tk.X)
        tk.Button(self.main_frame, text="3 - Assign or Relocate Doctor to a Patient", command=self.assign_doctor).pack(fill=tk.X)
        tk.Button(self.main_frame, text="4 - Update Admin Details", command=self.update_admin).pack(fill=tk.X)
        tk.Button(self.main_frame, text="5 - Patient Family", command=self.view_patient_family).pack(fill=tk.X)
        tk.Button(self.main_frame, text="6 - Doctor: View Assigned Patients", command=self.view_doctor_patients).pack(fill=tk.X)
        tk.Button(self.main_frame, text="7 - Save to file and exit", command=self.save_and_exit).pack(fill=tk.X)

    # OPT1: Admin : Register Doctor / View Doctor Details
    def manage_doctors(self):
        # Create a new window for doctor management
        doctor_window = tk.Toplevel(self.root)
        doctor_window.title("Manage Doctors")

        def register_doctor():
            register_window = tk.Toplevel(doctor_window)
            register_window.title("Register Doctor")

            tk.Label(register_window, text="First Name:").pack(pady=5)
            first_name_entry = tk.Entry(register_window)
            first_name_entry.pack(pady=5)

            tk.Label(register_window, text="Surname:").pack(pady=5)
            surname_entry = tk.Entry(register_window)
            surname_entry.pack(pady=5)

            tk.Label(register_window, text="Speciality:").pack(pady=5)
            speciality_entry = tk.Entry(register_window)
            speciality_entry.pack(pady=5)

            def confirm_register():
                first_name = first_name_entry.get()
                surname = surname_entry.get()
                speciality = speciality_entry.get()
                if first_name and surname and speciality:
                    new_doctor = Doctor(first_name, surname, speciality)
                    self.doctors.append(new_doctor)
                    messagebox.showinfo("Success", f"Doctor {new_doctor.full_name()} has been registered.")
                    register_window.destroy()
                else:
                    messagebox.showerror("Error", "All fields are required.")

            tk.Button(register_window, text="Register", command=confirm_register).pack(pady=10)
            tk.Button(register_window, text="Back", command=register_window.destroy).pack(pady=5)

        def view_doctors():
            for widget in doctor_window.winfo_children():
                widget.destroy()

            tk.Label(doctor_window, text="----- Doctor List -----", font=("Arial", 14)).pack(pady=10)

            if not self.doctors:
                tk.Label(doctor_window, text="No doctors registered.").pack(pady=10)
            else:
                for idx, doctor in enumerate(self.doctors):
                    tk.Label(doctor_window, text=f"{idx + 1} - {doctor.full_name()} | Speciality: {doctor.get_speciality()}").pack()

            tk.Button(doctor_window, text="Back", command=doctor_window.destroy).pack(pady=10)

        def update_doctor():
            update_window = tk.Toplevel(doctor_window)
            update_window.title("Update Doctor")

            tk.Label(update_window, text="Enter Doctor ID to update:").pack(pady=10)
            doctor_id_entry = tk.Entry(update_window)
            doctor_id_entry.pack(pady=5)

            tk.Label(update_window, text="New Speciality:").pack(pady=5)
            new_speciality_entry = tk.Entry(update_window)
            new_speciality_entry.pack(pady=5)

            def confirm_update():
                doctor_id = doctor_id_entry.get()
                new_speciality = new_speciality_entry.get()
                try:
                    doctor_index = int(doctor_id) - 1
                    if 0 <= doctor_index < len(self.doctors):
                        doctor = self.doctors[doctor_index]
                        doctor.set_speciality(new_speciality)
                        messagebox.showinfo("Success", f"Doctor {doctor.full_name()}'s speciality has been updated to {new_speciality}.")
                        update_window.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid Doctor ID.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid ID.")

            tk.Button(update_window, text="Update", command=confirm_update).pack(pady=10)
            tk.Button(update_window, text="Back", command=update_window.destroy).pack(pady=5)

        def delete_doctor():
            delete_window = tk.Toplevel(doctor_window)
            delete_window.title("Delete Doctor")

            tk.Label(delete_window, text="Enter Doctor ID to delete:").pack(pady=10)
            doctor_id_entry = tk.Entry(delete_window)
            doctor_id_entry.pack(pady=5)

            def confirm_delete():
                doctor_id = doctor_id_entry.get()
                try:
                    doctor_index = int(doctor_id) - 1
                    if 0 <= doctor_index < len(self.doctors):
                        doctor_to_delete = self.doctors.pop(doctor_index)
                        messagebox.showinfo("Success", f"Doctor {doctor_to_delete.full_name()} has been deleted.")
                        delete_window.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid Doctor ID.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid ID.")

            tk.Button(delete_window, text="Delete", command=confirm_delete).pack(pady=10)
            tk.Button(delete_window, text="Back", command=delete_window.destroy).pack(pady=5)

        # Create buttons for each functionality
        tk.Button(doctor_window, text="Register Doctor", command=register_doctor).pack(pady=5)
        tk.Button(doctor_window, text="View Doctors", command=view_doctors).pack(pady=5)
        tk.Button(doctor_window, text="Update Doctor", command=update_doctor).pack(pady=5)
        tk.Button(doctor_window, text="Delete Doctor", command=delete_doctor).pack(pady=5)
        tk.Button(doctor_window, text="Back", command=doctor_window.destroy).pack(pady=10)

    # OPT2: View Patient / Discharge Patients
    def manage_patients(self):
        # Create a new window for managing patients
        patient_window = tk.Toplevel(self.root)
        patient_window.title("Manage Patients")

        def view_patients():
            for widget in patient_window.winfo_children():
                widget.destroy()

            tk.Label(patient_window, text="----- Active Patients -----", font=("Arial", 14)).pack(pady=10)

            for idx, patient in enumerate(self.patients):
                tk.Label(patient_window, text=f"{idx + 1} - {patient.full_name()}").pack()

            tk.Button(patient_window, text="Back", command=patient_window.destroy).pack(pady=10)

        def discharge_patient():
            discharge_window = tk.Toplevel(patient_window)
            discharge_window.title("Discharge Patient")

            tk.Label(discharge_window, text="Enter Patient ID to discharge:").pack(pady=10)
            patient_id_entry = tk.Entry(discharge_window)
            patient_id_entry.pack(pady=5)

            def confirm_discharge():
                patient_id = patient_id_entry.get()
                try:
                    patient_index = int(patient_id) - 1
                    if 0 <= patient_index < len(self.patients):
                        discharged_patient = self.patients.pop(patient_index)
                        self.discharged_patients.append(discharged_patient)
                        messagebox.showinfo("Success", f"Patient {discharged_patient.full_name()} has been discharged.")
                        discharge_window.destroy()
                    else:
                        messagebox.showerror("Error", "Invalid Patient ID.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid ID.")

            tk.Button(discharge_window, text="Discharge", command=confirm_discharge).pack(pady=10)
            tk.Button(discharge_window, text="Back", command=discharge_window.destroy).pack(pady=5)

        tk.Button(patient_window, text="View Patients", command=view_patients).pack(pady=5)
        tk.Button(patient_window, text="Discharge Patient", command=discharge_patient).pack(pady=5)

    def assign_doctor(self):
        # Create a new window for assigning doctor to patient
        assign_window = tk.Toplevel(self.root)
        assign_window.title("Assign Doctor to Patient")

        # Create doctor selection dropdown
        tk.Label(assign_window, text="Select Doctor:").pack(pady=10)
        doctor_names = [doctor.full_name() for doctor in self.doctors]
        doctor_var = tk.StringVar()
        doctor_dropdown = tk.OptionMenu(assign_window, doctor_var, *doctor_names)
        doctor_dropdown.pack(pady=5)

        # Create patient selection dropdown
        tk.Label(assign_window, text="Select Patient:").pack(pady=10)
        patient_names = [patient.full_name() for patient in self.patients]
        patient_var = tk.StringVar()
        patient_dropdown = tk.OptionMenu(assign_window, patient_var, *patient_names)
        patient_dropdown.pack(pady=5)

        # Confirm button to assign doctor
        def confirm_assignment():
            selected_doctor_name = doctor_var.get()
            selected_patient_name = patient_var.get()

            # Find the selected doctor and patient objects
            selected_doctor = next((doctor for doctor in self.doctors if doctor.full_name() == selected_doctor_name), None)
            selected_patient = next((patient for patient in self.patients if patient.full_name() == selected_patient_name), None)

            if selected_doctor and selected_patient:
                # You can assign the doctor to the patient here
                # This can be done by adding a method to assign a doctor, for example:
                selected_patient.assign_doctor(selected_doctor)

                messagebox.showinfo("Success", f"Doctor {selected_doctor.full_name()} has been assigned to patient {selected_patient.full_name()}.")
                assign_window.destroy()
            else:
                messagebox.showerror("Error", "Failed to assign doctor. Please ensure all fields are selected.")

        tk.Button(assign_window, text="Assign Doctor", command=confirm_assignment).pack(pady=10)
        tk.Button(assign_window, text="Back", command=assign_window.destroy).pack(pady=5)

    def update_admin(self):
        # Create a new window for updating admin details
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Admin Details")

        # Display current admin details
        tk.Label(update_window, text="Current Admin Details", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(update_window, text=f"Name: {self.admin.get_name()}").pack(pady=5)
        tk.Label(update_window, text=f"Password: {self.admin.get_password()}").pack(pady=5)
        tk.Label(update_window, text=f"Address: {self.admin.get_address()}").pack(pady=5)

        tk.Label(update_window, text="--- Update Admin Details ---", font=("Arial", 12)).pack(pady=10)

        # Input fields to update admin details
        tk.Label(update_window, text="New Name:").pack(pady=5)
        new_name_entry = tk.Entry(update_window)
        new_name_entry.pack(pady=5)

        tk.Label(update_window, text="New Password:").pack(pady=5)
        new_password_entry = tk.Entry(update_window, show="*")
        new_password_entry.pack(pady=5)

        tk.Label(update_window, text="New Address:").pack(pady=5)
        new_address_entry = tk.Entry(update_window)
        new_address_entry.pack(pady=5)

        def confirm_update():
            new_name = new_name_entry.get()
            new_password = new_password_entry.get()
            new_address = new_address_entry.get()

            if new_name and new_password and new_address:
                # Update admin details
                self.admin.set_name(new_name)
                self.admin.set_password(new_password)
                self.admin.set_address(new_address)

                messagebox.showinfo("Success", "Admin details updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(update_window, text="Update", command=confirm_update).pack(pady=10)
        tk.Button(update_window, text="Back", command=update_window.destroy).pack(pady=5)


    def view_patient_family(self):
        # Show family details for each patient
        for patient in self.patients:
            patient.get_family1(self.patients)
        messagebox.showinfo("Info", "Patient family details displayed in console")

    def view_doctor_patients(self):
        # Create a new window for viewing doctor patients
        doctor_patients_window = tk.Toplevel(self.root)
        doctor_patients_window.title("View Doctor Patients")

        # Create doctor selection dropdown
        tk.Label(doctor_patients_window, text="Select Doctor:").pack(pady=10)
        doctor_names = [doctor.full_name() for doctor in self.doctors]
        doctor_var = tk.StringVar()
        doctor_dropdown = tk.OptionMenu(doctor_patients_window, doctor_var, *doctor_names)
        doctor_dropdown.pack(pady=5)

        def view_assigned_patients():
            # Clear previous patient list if any
            for widget in doctor_patients_window.winfo_children():
                widget.destroy()

            # Get selected doctor
            selected_doctor_name = doctor_var.get()
            selected_doctor = next((doctor for doctor in self.doctors if doctor.full_name() == selected_doctor_name), None)

            if selected_doctor:
                tk.Label(doctor_patients_window, text=f"----- Patients Assigned to {selected_doctor.full_name()} -----", font=("Arial", 14)).pack(pady=10)

                if not selected_doctor.assigned_patients:
                    tk.Label(doctor_patients_window, text="No patients assigned.").pack(pady=10)
                else:
                    assign = []
                    assign = selected_doctor.get_assigned_patients()
                    for idx, patient in enumerate(assign):
                        tk.Label(doctor_patients_window, text=f"{idx + 1} - {patient.full_name()}").pack()

            tk.Button(doctor_patients_window, text="Back", command=doctor_patients_window.destroy).pack(pady=10)

        tk.Button(doctor_patients_window, text="View Assigned Patients", command=view_assigned_patients).pack(pady=5)


    def save_and_exit(self):
        # Save data to files
        for patient in self.patients:
            patient.save_to_file()
        for doctor in self.doctors:
            doctor.save_to_file()

        messagebox.showinfo("Exiting", "Data saved. Exiting the system...")
        self.root.quit()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.mainloop()
