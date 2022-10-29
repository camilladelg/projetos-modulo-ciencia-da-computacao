from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "min_salary": 1500,
            "max_salary": 3000,
            "date_posted": "2020-05-02",
        },
        {
            "min_salary": 2000,
            "max_salary": 4000,
            "date_posted": "2020-04-01",
        },
        {
            "min_salary": 500,
            "max_salary": 1200,
            "date_posted": "2020-05-02",
        }
    ]
    criteria = ["min_salary", "max_salary", "date_posted"]

    sort_by(jobs, criteria[0])

    min_salarys = [
        job["min_salary"]
        for job in jobs
    ]

    assert min_salarys[0] == 500
