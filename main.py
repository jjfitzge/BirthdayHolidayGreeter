import datetime
import readCSV
# holiday dictionary to match holiday name with date
# Edit to fit specified holidays
holidays = {"25-12": "Christmas", "31-12": "New Year's Eve", "01-01": "New Year"}
suffix = {"0": "th", "1": "st", "2": "nd", "3": "rd", "4": "th", "5": "th", "6": "th", "7": "th", "8": "th", "9": "th"}
prev_day = ""
csv = "person_list.csv"

if __name__ == '__main__':
    now = datetime.datetime.now().isoformat().split('T')
    year, date, time = now[0][:4], now[0][5:], now[1]
    # date = "25-12"
    date = date[3:] + "-" + date[:2]
    # Don't want to check CSV again if we're at the same day
    holiday = ""
    if date != prev_day:
        holiday_dates = holidays.keys()
        if date in holiday_dates:
            holiday = holidays[date]
        dataframe = readCSV.parse_csv(csv)
        for entry, series in dataframe.iterrows():
            birthday = series[2][:5]
            if birthday == date:
                # send info to helper function
                year_int, birth_year = int(year), series[2][6:]
                age = year_int - int(birth_year)
                # age = 20
                message = f"wising you a happy {age}{suffix[str(age)[1]]} birthday, {series[0]}!"
                print(message)
            if holiday != "":
                # need to check if person has certain holiday == True
                if bool(series[holiday]):
                    # send message with holiday greeting
                    message = f"wising you a great {holiday}, {series[0]}!"
                    print(holiday)
        # prev_date = date






