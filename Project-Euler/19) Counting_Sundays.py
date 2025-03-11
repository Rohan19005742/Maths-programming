


def solve():
    months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
    ]
    months_days = {
    "January": 31,
    "February": { "normal": 28, "leap": 29 },
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
    }

    
    year = 1900
    month = "January"
    date = 7
    answer = 0

    for x in range(101):
        for y in range(12):
            if y == 1:
                if year % 4 == 0:
                    if year % 100 == 0:
                        days_in_months = 28
                    else:
                        days_in_months = 29
                else:
                    days_in_months = 28
            else:
                days_in_months = months_days[months[y]]
            while date < days_in_months:
                if year > 1900:
                    if date == 1:
                        answer+=1
                date+=7
            date -= days_in_months
        year+=1
    
    print(answer)

solve()