def add_years_to_date(date, years):
    result = date.replace(year=date.year + years)
    return result
