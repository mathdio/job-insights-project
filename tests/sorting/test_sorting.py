from src.pre_built.sorting import sort_by

list_to_sort = [
    {"min_salary": 10, "max_salary": 50, "date_posted": "2020-12-01"},
    {"min_salary": 30, "max_salary": 40, "date_posted": "2020-01-01"},
    {"min_salary": 20, "max_salary": 60, "date_posted": ""},
    {"min_salary": 20, "max_salary": 60, "date_posted": "2020-06-01"},
]

max_salary_sort = [
    {"min_salary": 20, "max_salary": 60, "date_posted": ""},
    {"min_salary": 20, "max_salary": 60, "date_posted": "2020-06-01"},
    {"min_salary": 10, "max_salary": 50, "date_posted": "2020-12-01"},
    {"min_salary": 30, "max_salary": 40, "date_posted": "2020-01-01"},
]

min_salary_sort = [
    {"min_salary": 10, "max_salary": 50, "date_posted": "2020-12-01"},
    {"min_salary": 20, "max_salary": 60, "date_posted": ""},
    {"min_salary": 20, "max_salary": 60, "date_posted": "2020-06-01"},
    {"min_salary": 30, "max_salary": 40, "date_posted": "2020-01-01"},
]

date_posted_sort = [
    {"min_salary": 10, "max_salary": 50, "date_posted": "2020-12-01"},
    {"min_salary": 20, "max_salary": 60, "date_posted": "2020-06-01"},
    {"min_salary": 30, "max_salary": 40, "date_posted": "2020-01-01"},
    {"min_salary": 20, "max_salary": 60, "date_posted": ""},
]


def test_sort_by_criteria():
    sort_by(list_to_sort, "max_salary")
    assert list_to_sort == max_salary_sort
    sort_by(list_to_sort, "min_salary")
    assert list_to_sort == min_salary_sort
    sort_by(list_to_sort, "date_posted")
    assert list_to_sort == date_posted_sort
