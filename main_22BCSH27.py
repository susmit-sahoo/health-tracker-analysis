from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
        with open(fileName, 'r') as file:
            for line in file:
                line = line.strip()

                # Splitting the line based on comma
                fields = line.split(',')

                # Check for correct number of fields
                if len(fields) != 8:
                    print(f"Invalid number of fields ({len(fields)}) in line: {line}")
                    continue

                # Extracting values
                try:
                    patientId = int(fields[0])
                    date = fields[1]
                    temperature = float(fields[2])
                    heart_rate = int(fields[3])
                    respiratory_rate = int(fields[4])
                    systolic_bp = int(fields[5])
                    diastolic_bp = int(fields[6])
                    oxygen_saturation = int(fields[7])
                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue

                # Validating the values
                if not (35 <= temperature <= 42):
                    print(f"Invalid temperature value ({temperature}) in line: {line}")
                    continue

                if not (30 <= heart_rate <= 180):
                    print(f"Invalid heart rate value ({heart_rate}) in line: {line}")
                    continue

                if not (5 <= respiratory_rate <= 40):
                    print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line}")
                    continue

                if not (70 <= systolic_bp <= 200):
                    print(f"Invalid systolic blood pressure value ({systolic_bp}) in line: {line}")
                    continue

                if not (40 <= diastolic_bp <= 120):
                    print(f"Invalid diastolic blood pressure value ({diastolic_bp}) in line: {line}")
                    continue

                if not (70 <= oxygen_saturation <= 100):
                    print(f"Invalid oxygen saturation value ({oxygen_saturation}) in line: {line}")
                    continue

                # Storing values into the dictionary
                if patientId not in patients:
                    patients[patientId] = []

                patients[patientId].append([date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation])

    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    except Exception:
        print("An unexpected error occurred while reading the file.")

    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    # If patientId is not 0 and not found in patients, display error message
    if patientId != 0 and patientId not in patients:
        print(f"Patient with ID {patientId} not found.")
        return

    # Display data for the required patients
    for id, visits in patients.items():
        if patientId == 0 or patientId == id:
            print(id)
            for visit in visits:
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart Rate:", visit[2], "bpm")
                print("  Respiratory Rate:", visit[3], "bpm")
                print("  Systolic Blood Pressure:", visit[4], "mmHg")
                print("  Diastolic Blood Pressure:", visit[5], "mmHg")
                print("  Oxygen Saturation:", visit[6], "%")



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        # Errors to handle
        patientId = int(patientId)

        # Check if the patientId is 0 (display stats for all patients)
        if patientId == 0:
            all_temperatures = []
            all_heart_rates = []
            all_respiratory_rates = []
            all_systolic_bps = []
            all_diastolic_bps = []
            all_oxygen_saturations = []

            for key,value in patients.items():
                for visit in value:
                    all_temperatures.append(visit[1])
                    all_heart_rates.append(visit[2])
                    all_respiratory_rates.append(visit[3])
                    all_systolic_bps.append(visit[4])
                    all_diastolic_bps.append(visit[5])
                    all_oxygen_saturations.append(visit[6])

            total_visits = len(all_temperatures)
            average_temperature = sum(all_temperatures) / total_visits
            average_heart_rate = sum(all_heart_rates) / total_visits
            average_respiratory_rate = sum(all_respiratory_rates) / total_visits
            average_systolic_bp = sum(all_systolic_bps) / total_visits
            average_diastolic_bp = sum(all_diastolic_bps) / total_visits
            average_oxygen_saturation = sum(all_oxygen_saturations) / total_visits

            print("Vital Signs for All Patients:")
            print(f"  Average Temperature: {average_temperature:.2f}°C")
            print(f"  Average Heart Rate: {average_heart_rate:.2f} bpm")
            print(f"  Average Respiratory Rate: {average_respiratory_rate:.2f} bpm")
            print(f"  Average Systolic Blood Pressure: {average_systolic_bp:.2f} mmHg")
            print(f"  Average Diastolic Blood Pressure: {average_diastolic_bp:.2f} mmHg")
            print(f"  Average Oxygen Saturation: {average_oxygen_saturation:.2f}%")

        else:

            # Display stats for the specific patientId
            if patientId in patients:
                patient_data = patients[patientId]
                total_visits = len(patient_data)
                if total_visits == 0:
                    print("No data found.")
                    return

                total_temperature = sum(visit[1] for visit in patient_data)
                total_heart_rate = sum(visit[2] for visit in patient_data)
                total_respiratory_rate = sum(visit[3] for visit in patient_data)
                total_systolic_bp = sum(visit[4] for visit in patient_data)
                total_diastolic_bp = sum(visit[5] for visit in patient_data)
                total_oxygen_saturation = sum(visit[6] for visit in patient_data)

                average_temperature = total_temperature / total_visits
                average_heart_rate = total_heart_rate / total_visits
                average_respiratory_rate = total_respiratory_rate / total_visits
                average_systolic_bp = total_systolic_bp / total_visits
                average_diastolic_bp = total_diastolic_bp / total_visits
                average_oxygen_saturation = total_oxygen_saturation / total_visits

                print(f"Vital Signs for Patient ID {patientId}:")
                print(f"  Average Temperature: {average_temperature:.2f}°C")
                print(f"  Average Heart Rate: {average_heart_rate:.2f} bpm")
                print(f"  Average Respiratory Rate: {average_respiratory_rate:.2f} bpm")
                print(f"  Average Systolic Blood Pressure: {average_systolic_bp:.2f} mmHg")
                print(f"  Average Diastolic Blood Pressure: {average_diastolic_bp:.2f} mmHg")
                print(f"  Average Oxygen Saturation: {average_oxygen_saturation:.2f}%")
            else:
                print("No data found.")

    except ValueError:
        print("Error: 'patientId' should be an integer.")
    except AssertionError:
        print("Error: 'patients' should be a dictionary.")



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    # Check for invalid inputs

    # Check date format
    parts = date.split('-')
    if len(parts) != 3:
        print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
        return
    try:
        year, month, day = map(int, parts)
    except ValueError:
        print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’.")
        return

    if not (1 <= month <= 12) or not (1 <= day <= 31) or year < 1900:
        print("Invalid date. Please enter a valid date.")
        return

    # Check temperature
    if not (35.0 <= temp <= 42.0):
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return

    # Check heart rate
    if not (30 <= hr <= 180):
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return

    # Check respiratory rate
    if not (5 <= rr <= 40):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return

    # Check systolic blood pressure
    if not (70 <= sbp <= 200):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return

    # Check diastolic blood pressure
    if not (40 <= dbp <= 120):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return

    # Check oxygen saturation level
    if not (70 <= spo2 <= 100):
        print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        return

    # Add patient data to dictionary
    if patientId in patients:
        patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])
    else:
        patients[patientId] = [[date, temp, hr, rr, sbp, dbp, spo2]]

    # Append data to the text file
    try:
        with open(fileName, 'a') as file:
            file.write(f"{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")
        print(f"Visit is saved successfully for Patient #{patientId}")
    except Exception:
        print("An unexpected error occurred while adding new data.")



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    # Ensure month is only provided when year is also provided
    if month and not year:
        return []

    # Validate month and year input
    if month and (month < 1 or month > 12):
        return []

    result = []
    for patient_id, visits in patients.items():
        for visit in visits:
            # Parse date information
            date_info = visit[0].split('-')
            if len(date_info) != 3:
                # Ignore invalid date formats
                continue
            visit_year, visit_month, visit_day = map(int, date_info)

            # Check if year or month are provided and match with the visit data
            if year and year != visit_year:
                continue
            if month and month != visit_month:
                continue
            result.append((patient_id, visit))
    return result
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []

    # Check each patient
    for patient_id, visits in patients.items():
        for visit in visits:
            _, _, heart_rate, _, systolic, diastolic, oxygen_saturation = visit

            # Check for abnormal vital signs
            if (
                heart_rate > 100 or heart_rate < 60 or
                systolic > 140 or diastolic > 90 or
                oxygen_saturation < 90
            ):
                followup_patients.append(patient_id)
                break  # Once we find one abnormal visit, no need to check the rest for this patient

    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    # Check if the patient ID exists in the dictionary
    if patientId in patients:
        # Delete the patient's data from the dictionary
        del patients[patientId]
        print(f"Data for patient {patientId} has been deleted.")
    '''else:
        # Print error message if patient ID not found
        print(f"No data found for patient with ID {patientId}")
        return'''

    # Open the file in write mode
    with open(filename, 'w') as file:
        # Iterate over the patients and their visits in the dictionary
        for pid, visits in patients.items():
            for visit in visits:
                # Extract details from each visit
                date, temp, hr, rr, sbp, dbp, spo2 = visit
                # Write the visit details in the specified format to the file
                file.write(f"{pid},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}\n")




###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()