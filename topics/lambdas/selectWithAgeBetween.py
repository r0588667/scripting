def select_with_age_between(persons, min, max):
    result = []

    for p in persons:
        if min <= p.age and p.age <= max:
            result.append(p)

    return result
