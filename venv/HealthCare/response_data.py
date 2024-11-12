from pymongo import MongoClient
import re

# Connect to MongoDB (adjust URI and database details as needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["Healthcare"]
patients_collection = db["patients"]
pharmacies_collection = db["pharmacies"]
hospitals_collection = db["hospitals"]

# Function to extract Patient ID or other IDs from the user input
def extract_id(user_input):
    match = re.search(r'\b\d{5,}\b', user_input)  # Adjust as per ID length requirement
    return match.group(0) if match else None

# Define the actions for each context
def perform_action(context, entity_id=None):
    if context == "search_blood_pressure_by_patient_id":
        return search_blood_pressure(entity_id)
    elif context == "search_medical_history_by_patient_id":
        return search_medical_history(entity_id)
    elif context == "search_allergies_by_patient_id":
        return search_allergies(entity_id)
    elif context == "search_medication_by_patient_id":
        return search_medication(entity_id)
    elif context == "search_appointment_history_by_patient_id":
        return search_appointments(entity_id)
    elif context == "search_lab_results_by_patient_id":
        return search_lab_results(entity_id)
    elif context == "search_pharmacy_by_name":
        return search_pharmacy(entity_id)
    elif context == "search_hospital_by_type":
        return search_hospital(entity_id)
    else:
        return "No action found for the current context."

# Context-specific functions for each context
def search_blood_pressure(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"blood_pressure": 1})
    return result["blood_pressure"] if result else "No blood pressure data found."

def search_medical_history(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"medical_history": 1})
    return result["medical_history"] if result else "No medical history found."

def search_allergies(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"allergies": 1})
    return result["allergies"] if result else "No allergy information found."

def search_medication(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"medications": 1})
    return result["medications"] if result else "No medication records found."

def search_appointments(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"appointments": 1})
    return result["appointments"] if result else "No appointment history found."

def search_lab_results(patient_id):
    result = patients_collection.find_one({"patient_id": patient_id}, {"lab_results": 1})
    return result["lab_results"] if result else "No lab results found."

def search_pharmacy(pharmacy_name):
    result = pharmacies_collection.find_one({"name": pharmacy_name})
    return result if result else "No pharmacy information found."

def search_hospital(hospital_type):
    result = hospitals_collection.find_one({"type": hospital_type})
    return result if result else "No hospital details found."
