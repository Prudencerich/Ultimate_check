#condition: for schools in Nigeria where all female student wear gown and male sstudent wear pants
female_attire = "gown"
male_attire = "pants"

def female(gown):
    student = gown
    return student

female_count = 0
male_count = 0

while True:
    student_attire = input("Enter the attire of the student (gown/pants): ").lower()
    
    if student_attire == female_attire:
        female_count  =+ 1
    elif student_attire == male_attire:
        male_count =+ 1
    else:
        print("Invalid option. Please enter 'gown' for female or pants for male.")
        continue
    
    choice = input("Do you want to enter another student's attire? (yes/no): ").lower()
    if choice != "yes":
        break
    
    print("\nSummary:")
    print(f"Number of female students wearing gown: {female_count}")
    print(f"Number of male students wearing pants: {male_count}")

