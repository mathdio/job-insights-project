from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)

    industries_set = set()
    for job in jobs_list:
        industries_set.add(job["industry"])

    industries_list = []
    for industry in industries_set:
        if industry != "":
            industries_list.append(industry)
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industries.append(job)
    return filtered_industries
