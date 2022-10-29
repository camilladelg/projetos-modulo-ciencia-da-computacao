from src.counter import count_ocurrences


def test_counter():
    totalWordPython = count_ocurrences("src/jobs.csv", "python")
    totalWordJavaScript = count_ocurrences("src/jobs.csv", "javascript")
    assert totalWordPython == 1639
    assert totalWordJavaScript == 122
