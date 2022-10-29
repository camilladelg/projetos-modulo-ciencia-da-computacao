from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    teste = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    words = ["title", "salary", "type"]

    for word in words:
        assert word in teste[0]
