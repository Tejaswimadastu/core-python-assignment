# Function to add a patient to the list
def add_patient(patients, name, age, disease):
    patients.append({"Name": name, "Age": age, "Disease": disease})
# Function to search patients by disease
def search_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    return result if result else ["No patients found"]
# List to store all patient records
patients = []
# Input number of patients
n = int(input("Enter number of patients to add: "))
# Loop to input patient details
for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    add_patient(patients, name, age, disease)  # Add patient record
search_disease = input("\nEnter disease to search patients: ")
found_patients = search_by_disease(patients, search_disease)
print(f"\nPatients with {search_disease}: {found_patients}")
