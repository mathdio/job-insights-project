from functools import lru_cache
from typing import List, Dict
import os
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    print(file_dir)
    file_name = os.path.join(file_dir, path)
    print(file_name)
    with open(file_name) as file:
        jobs_reader = csv.reader(file)
        header, *data = jobs_reader

    jobs_list = []
    for row in data:
        job = {}
        for index in range(0, len(header)):
            job[header[index]] = row[index]
        jobs_list.append(job)
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
