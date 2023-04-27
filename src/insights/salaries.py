from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salaries_set = set()
    for job in jobs_list:
        if job["max_salary"].isdigit():
            salaries_set.add(int(job["max_salary"]))

    maximum_salary = max(salaries_set)
    return maximum_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salaries_set = set()
    for job in jobs_list:
        if job["min_salary"].isdigit():
            salaries_set.add(int(job["min_salary"]))

    minimum_salary = min(salaries_set)
    return minimum_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
        if min_salary > max_salary:
            raise ValueError("min_salary greater than max_salary")
    except (ValueError, TypeError, KeyError):
        raise ValueError("Invalid values in min_salary, max_salary or salary")
    else:
        return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_in_range = []
    for job in jobs:
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            salary = int(salary)
            if min_salary <= salary <= max_salary:
                jobs_in_range.append(job)
        except (ValueError, TypeError, KeyError):
            print("Error")
    return jobs_in_range
