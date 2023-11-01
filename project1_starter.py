class Person:
    def __init__(self, schedule, daily_act):

        #data correction code to make sure the codes are in the correct format
        for interval in schedule:
            for i in range(2):  
                time_str = interval[i]
                if len(time_str) < 5:
                    # Add '0' to the beginning if the element has less than 5 characters
                    interval[i] = '0' + time_str

        #same code for other list
        for interval in daily_act:
            for i in range(2):  
                time_str = interval[i]
                if len(time_str) < 5:
                    interval[i] = '0' + time_str

        self.schedule = schedule
        self.daily_act = daily_act


#the person class has a schedule meeting function which will take an input with another person object and see when they will be available to meet.
#input: 2 people objects
#output: a list of lists showing the intersecting free times of the two comparing people
def schedule_meeting(prsn1, prsn2, duration):
    available = []

    #finding optimal range
    earliest = max([prsn1.daily_act[0][0], prsn2.daily_act[0][0]])
    latest = min([prsn1.daily_act[0][1], prsn2.daily_act[0][1]])
    
    # Combine both lists of occupied times
    all_occupied_times = prsn1.schedule + prsn2.schedule

    # Sort the occupied times by their start time
    all_occupied_times.sort(key=lambda x: x[1], reverse = True)

    # Initialize the start and end times
    prev_end = latest

    for interval in all_occupied_times:
        # Extract the start and end times from the interval
        interval_start, interval_end = interval

        # Compare the current interval's start time with the end time of the previous interval
        if prev_end > interval_end and interval_end > earliest:
            available.append([interval_end, prev_end])
        prev_end = interval_start

#verification code to check if the available times can accomodate for the desired duration of the meeting

    product = []
    for interval in available:
        time2, time1 = interval
        
        hours1, minutes1 = map(int, time1.split(':'))
        hours2, minutes2 = map(int, time2.split(':'))

        # Subtract hours and minutes
        result_hours = hours1 - hours2
        result_minutes = minutes1 - minutes2

        # Handle borrow/overflow
        if result_minutes < 0:
            result_hours -= 1
            result_minutes += 60
        result = result_minutes + result_hours*60

        if(result > duration):
            product.append(interval)
        
    return product

#todo: create output method
#       write 10 different inputs in inputs.txt
#       write a readme

# Example usage
person1_booked_times = [['07:00', '08:30'], ['12:00', '13:00'], ['16:00', '18:00']]
person1_available_times = [['07:30', '18:00']]

person2_booked_times = [['07:30', '09:00'], ['12:30', '13:30'], ['17:00', '19:00']]
person2_available_times = [['07:00', '19:00']]

person1 = Person(person1_booked_times, person1_available_times)
person2 = Person(person2_booked_times, person2_available_times)

common_free_times = schedule_meeting(person1, person2, 30)
print(common_free_times)

