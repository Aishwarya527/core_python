def search_patients(patients, disease):
    result = [patient["Name"] for patient in patients if patient["Disease"] == disease]
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
patients_with_disease = search_patients(patients, search_disease)
print(f"Patients with {search_disease}: {patients_with_disease}")