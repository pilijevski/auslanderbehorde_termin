import json


def get_id_by_citizenship(citizenship):
    nationalities = json.load(open("nationalities.json","r"))
    try:
        _id = nationalities[citizenship]
        return _id
    except KeyError:
        return Exception("Please input a correct citizenship. Doublecheck the nationalities from the page.")


def get_id_family_member(answer):
    if answer == "yes":
        return "1"
    elif answer == "no":
        return "2"
    else:
        raise AttributeError("Please provide a valid answer (yes/no)")
