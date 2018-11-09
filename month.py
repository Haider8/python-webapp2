# month.py


# -----------
# User Instructions
#
# Modify the valid_month() function to verify
# whether the data a user enters is a valid
# month. If the passed in parameter 'month'
# is not a valid month, return None.
# If 'month' is a valid month, then return
# the name of the month with the first letter
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
month_abbvs = dict((m[:3].lower(), m) for m in months)
#print('hello'.capitalize())


def valid_month(month):
    short_month = month[:3].lower()
    new_month = month_abbvs.get(short_month)
    for i in range(0, 12):
        if months[i] == new_month:
            return True
            break
        elif i == 11:
            return False




#print valid_month('janffff')

# print valid_month("january")
# => "January"
# print valid_month("January")
# => "January"
# print valid_month("foo")
# => None
# print valid_month("")
# => Non