import csv

class patient:

    # 1] adding new patient
    def add_patient(self):
        new=[]

        id=int(input('Enter the patient id : '))
        name=input('Enter the name of Patient : ')
        age=int(input('Enter the age : '))
        gender=input('Enter the gender Male / Female : ')
        disease=input('Enter the disease name : ')
        d_name=input('Enter the doctor name : ')
        a_date=input('Enter the date (yyyy-mm-dd) : ')
        bill=int(input('Enter the bill amount : '))
        status=input('Enter the status : ')

        new.extend([id,name,age,gender,disease,d_name,a_date,bill,status])
        with open ('data.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(new)

    # 2] display all patients
    def view_patient(self):
        with open ('data.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                print(row)

    # 3] Search particular patient by patient id 
    def search_patient(self, id):
        with open ('data.csv','r') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0] == id:
                    print(row)

    # 4] update patient detail using patient id
    def update_patient(self, search_id):
        updated_rows=[]
        record=False

        with open ('data.csv','r') as file:
            reader=csv.reader(file)
            header = next(reader)
            updated_rows.append(header)

            for row in reader:
                if search_id == row[0]:
                    record=True
                    print('Record Found..')
                    print('Enter the details to update...')
                    id=int(input('Enter the patient id : '))
                    name=input('Enter the name of Patient : ')
                    age=int(input('Enter the age : '))
                    gender=input('Enter the gender Male / Female : ')
                    disease=input('Enter the disease name : ')
                    d_name=input('Enter the doctor name : ')
                    a_date=input('Enter the date (yyyy-mm-dd) : ')
                    bill=int(input('Enter the bill amount : '))
                    status=input('Enter the status : ') 
                    updated_rows.append([id,name,age,gender,disease,d_name,a_date,bill,status])
                else:
                    updated_rows.append(row)

        if record:
            with open ('data.csv','w',newline='') as file:
                writer =csv.writer(file)
                writer.writerows(updated_rows)
            print('Patient record updated successfully...')
        else:
            print('Record not found...')

    # 5] delete the record of patient using patient id
    def delete_patient(self, id):
        with open ('data.csv','r') as file:
            reader = csv.reader(file)
            header = next(reader)

            record=False
            update_row=[]
            update_row.append(header)
            for row in reader:
                if id == row[0]:
                    record=True
                    continue
                else:
                    update_row.append(row)
        if record:
            print('Record found')
            print('Record deleted successfully...')
            with open ('data.csv','w',newline='') as file:
                writer=csv.writer(file)
                writer.writerows(update_row)
        else:
            print('Record not found...')

    # 6] calculate bill using patient id
    def bill(self, patient_id):
        with open ('data.csv','r') as file:
            reader=csv.reader(file)
            record=False
            p_bill=''

            for row in reader:
                if patient_id == row[0]:
                    record=True
                    p_bill=row[7]
                    break
            if record:
                print('Record found..')
                print(f'Your total bill is : {p_bill}')
            else:
                print('Record not found!!!')

    # 7] discharge the patient using patient id
    def dp_discharge(self, pid):
        with open ('data.csv','r',newline='') as file:
            reader=csv.reader(file)
            updated_rows = []
            record=False

            header= next(reader)
            updated_rows.append(header)

            for row in reader:
                if pid == row[0]:
                    record=True
                    print('Record found...')
                    if row[8].strip().lower() == 'discharged':
                        print('Patient is already discharged !!!')
                        updated_rows.append(row)
                    else:
                        row[8]='Discharged'
                        updated_rows.append(row)
                else:
                    updated_rows.append(row)

            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if record:
                print('Patient discharged successfully...')

    # 8] count all patients 
    def counting(self):
        with open ('data.csv','r') as file:
            reader=csv.reader(file)
            next(reader) # Skip header
            count=0
            for row in reader:
                count+=1
            print(f'Total patients are : {count}')
            return count

    # 9] Show patients with doctor wise
    def doc_wise(self):
        with open ('data.csv','r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            record = list(reader)

            doc_name=list(set(row[5] for row in record))

            for doc in doc_name:
                print('-'*50)
                print(f'Doctor Name : {doc}')
                print('-'*50)
                for row in record:
                    if row[5] == doc:
                        print(row)
                print()

    # 10] show patient with disease wise
    def disp(self):
        with open ('data.csv','r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            record = list(reader)

            dis_name=list(set(row[4] for row in record))

            for dis in dis_name:
                print('-'*50)
                print(f'Disease Name : {dis}')
                print('-'*50)
                for row in record:
                    if row[4] == dis:
                        print(row)
                print()

    # 11] Highest bill payment
    def hb(self):
        with open ('data.csv','r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            record=list(reader)
            if not record:
                return

            h = -1
            for row in record:
                if int(row[7]) > h:
                    h = int(row[7])

            for row in record:
                if int(row[7]) == h:
                    print(f'The highest bill is : {h}')
                    print(row)

    # 12] Average bill payment
    def ab(self):
        with open ('data.csv','r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            
            total_sum=0
            record=list(reader)
            if not record: 
                return
            
            for row in record:
                total_sum = total_sum + int(row[7])

            avg = total_sum / len(record)
            print(f'The average bill is : {avg}')

    # 13] export summary
    def summary(self):
        print("\n======= SYSTEM SUMMARY REPORT =======")
        self.counting()
        self.doc_wise()
        self.disp()
        self.hb()
        self.ab()


class Hospital(patient):
    
    def hospital_info(self):
        print("\n" + "="*40)
        print("     CITY GENERAL HEALTHCARE CENTER     ")
        print("="*40)
        print("Location : 404 Med Street, Sector 2")
        print("Services : 24/7 Trauma, ICU, Pediatrics")
        print("="*40)

    def total_revenue(self):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            revenue = sum(int(row[7]) for row in reader)
            print(f"\nTotal Accrued Revenue from Bills: Rs. {revenue}")

    def doctor_wise_patient_count(self):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            counts = {}
            for row in reader:
                doc = row[5]
                counts[doc] = counts.get(doc, 0) + 1
            
            print("\n--- Patient Load Per Doctor ---")
            for doc, count in counts.items():
                print(f"Doctor: {doc} -> Active Patients: {count}")

    def generate_daily_report(self):
        print("\n================ DAILY MANAGEMENT REPORT ================")
        self.hospital_info()
        self.total_revenue()
        self.doctor_wise_patient_count()
        print("=========================================================")

    def menu(self):
            while True:
                print("\n" + "=" * 60)
                print("        HOSPITAL MANAGEMENT SYSTEM")
                print("=" * 60)
                print("1.  Add New Patient")
                print("2.  View All Patients")
                print("3.  Search Patient by ID")
                print("4.  Update Patient Details")
                print("5.  Delete Patient Record")
                print("6.  Display Patient Bill")
                print("7.  Discharge Patient")
                print("8.  Count Total Patients")
                print("9.  Show Doctor Wise Patients")
                print("10. Show Disease Wise Patients")
                print("11. Show Highest Bill")
                print("12. Show Average Bill")
                print("13. Show Complete Summary")
                print("14. Hospital Information")
                print("15. Total Revenue")
                print("16. Doctor Wise Patient Count")
                print("17. Generate Daily Report")
                print("18. Exit")
                print("=" * 60)

                choice = input("Enter your choice (1-18): ")

                if choice == '1':
                    self.add_patient()

                elif choice == '2':
                    self.view_patient()

                elif choice == '3':
                    pid = input("Enter Patient ID: ")
                    self.search_patient(pid)

                elif choice == '4':
                    pid = input("Enter Patient ID to Update: ")
                    self.update_patient(pid)

                elif choice == '5':
                    pid = input("Enter Patient ID to Delete: ")
                    self.delete_patient(pid)

                elif choice == '6':
                    pid = input("Enter Patient ID: ")
                    self.bill(pid)

                elif choice == '7':
                    pid = input("Enter Patient ID: ")
                    self.dp(pid)

                elif choice == '8':
                    self.counting()

                elif choice == '9':
                    self.doc_wise()

                elif choice == '10':
                    self.disp()

                elif choice == '11':
                    self.hb()

                elif choice == '12':
                    self.ab()

                elif choice == '13':
                    self.summary()

                elif choice == '14':
                    self.hospital_info()

                elif choice == '15':
                    self.total_revenue()

                elif choice == '16':
                    self.doctor_wise_patient_count()

                elif choice == '17':
                    self.generate_daily_report()

                elif choice == '18':
                    print("\nThank you for using Hospital Management System.")
                    print("Program Terminated Successfully.")
                    break

                else:
                    print("\nInvalid Choice! Please select a valid option.")

H=Hospital()
H.menu()