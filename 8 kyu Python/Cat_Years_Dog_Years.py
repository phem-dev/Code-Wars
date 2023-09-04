"""
Instructions:
I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that

"""


# Solution:
def human_years_cat_years_dog_years(human_years):
    yr_1 = 15
    h_yr = human_years
    if human_years == 1:
        return [h_yr, yr_1, yr_1]
    elif human_years > 1 and human_years < 3:
        yr_1 = yr_1 + 9
        return [h_yr, yr_1, yr_1]
    else:
        c_yr = 24 + (4 * 8)
        d_yr = 24 + (5 * 8)
        return [h_yr, c_yr, d_yr]
