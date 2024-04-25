from datetime import datetime 

def break_habit(goal, habit_name, start_date, cost_per_day, minutes_wasted): 

    # total time elapsed in seconds
    start_date = datetime.strptime(start_date,  "%d.%m.%Y")
    time_elapsed = (datetime.now() - start_date).total_seconds()

    # convert timestamp into hours/days
    hours = round(time_elapsed / 60 / 60)
    days = round(hours / 24)

    # some details
    minutes_saved = round(days*minutes_wasted)
    money_saved = cost_per_day*days
    money_saved = f'₺{round(money_saved ,2)}'

    # days to go
    days_to_go = round(goal - days)

    # change hours
    if hours > 24:
        hours = str(days) + ' days'
    else:
        hours = str(hours) + ' hours'
    return {
        'Habit': habit_name, 'Time Since': hours, 'Days Remaining': days_to_go,
        'Minutes Saved': minutes_saved, 'Money Saved': money_saved
    }


def gain_habit(goal, habit_name, start_date):

    # total time elapsed in seconds
    start_date = datetime.strptime(start_date,  "%d.%m.%Y")
    time_elapsed = (datetime.now() - start_date).total_seconds()

    # convert timestamp into hours/days
    hours = round(time_elapsed / 60 / 60)
    days = round(hours / 24)

    # days to go
    days_to_go = round(goal-days)

    # change hours
    if hours > 24:
        hours = str(days) + ' days'
    else:
        hours = str(hours) + ' hours'
    return {
        'Habit': habit_name, 'Time Since': hours, 'Days Remaining': days_to_go
    }
