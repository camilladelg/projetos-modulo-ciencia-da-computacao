def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    count = 0
    for p in permanence_period:
        if type(p[0]) != int or type(p[1]) != int:
            return None

        if p[0] <= target_time <= p[1]:
            count += 1
    return count
