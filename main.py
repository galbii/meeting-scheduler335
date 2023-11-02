import project1_starter as meeting
from project1_starter import Person
import ast

def schedule_planner():
    people = []
    duration = 30

    while True:
        print("\n\nMenu:\n")
        print("1. Add a schedule")
        print("2. Adjust duration")
        print("3. Calculate")
        print("4. Clear")
        print("5. List buffer\n\n")
        print("q. Quit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a schedule
            schedule = ast.literal_eval(input("\nPlease enter the booked hours of the person: \n"))
            logger = ast.literal_eval(input("\nPlease enter the clock in and clock out time:\n"))
            people.append(Person(schedule, logger))

        elif choice == "2":
            # Adjust duration
            duration = int(input("\nEnter the duration of the meeting you are looking for: \n"))

        elif choice == "3":
            # Calculate
            if people == []:
                print("\n\n[error] list is empty")
            else:
                result = meeting.schedule_meeting(people, duration)
                print("\nAvailable meeting times have been stored in the 'Outputs.txt' file:")
                print(result, "\n\n")

        elif choice == "4":
            # Clear the schedule
            people = []
            print("\n\nSchedule cleared.")

        elif choice == "5":
            if people == []:
                print("\n\n[error] list is empty")
            for person in people:
                print(person.schedule, person.daily_act)

            print("Duration: ", duration)


        elif choice.lower() == "q":
            # Quit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    schedule_planner()


