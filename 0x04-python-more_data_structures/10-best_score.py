#!/usr/bin/python3


def best_score(a_dictionary):
    scores = []
    if not a_dictionary:
        return None
    for key in a_dictionary:
        scores.append(a_dictionary[key])
    max_score = max(scores)
    for key in a_dictionary:
        if a_dictionary[key] == max_score:
            return key
