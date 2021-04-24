import calendar

months = calendar.month_abbr[1:]

print(f"\n{months}")

months_nums_to_names = dict(enumerate(months, start=1))

print(months_nums_to_names)

new_months = {v: k for k, v in months_nums_to_names.items()}

print(new_months)