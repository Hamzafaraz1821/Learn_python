def find_missing_ids(first_ids, second_ids):
    set1 = set(first_ids)
    set2 = set(second_ids)

    set1 = set1 - set2

    return list(set1)