"""
A program that get's data from API and shows every person's family to the
user.

The original assigment can be found in
https://www.protacon.com/ohjelmointitehtava/?utm_campaign=IT-Hekuma

Made by Antti Eskelinen.
"""


from Person import Person
import urllib.request
import urllib.error
import json


def main():

    # Save the information about people as People-objects in a dict.
    people = {}

    # Get information from the API.
    try:
        with urllib.request.urlopen(
                "http://it-hekuma.protacon.fi/family_tree.json") as url:
            family_data = json.loads(url.read().decode())
            for object in family_data:
                person = Person(object["id"],
                                object["firstName"],
                                object["lastName"],
                                object["mother"],
                                object["father"])
                people[str(person)] = person

    except (urllib.error.HTTPError, urllib.error.URLError):
        # Stop the program if an error occures.
        print("An error occured")
        return

    # Ask user which persons family s/he wants to use.
    print("Enter person's name or type 'list' to see all names.")
    name = input()
    run_loop = True
    while run_loop:

        if name == "list":
            # Print all names in alphabethical order by last name.
            for i in sorted(people, key=lambda x: people[x].get_last_name()+x):
                print(i)

        elif name in people:
            # Print person's family.
            print("Person:", people[name], end="\n\n")

            # Try to find parents.
            mother = people[name].get_mother(people)
            father = people[name].get_father(people)
            print("Mother:", mother)
            print("Father:", father)

            if not (str(mother) or str(father)) == "Unknown":
                # Try to find siblings.

                siblings = people[name].get_siblings(people)
                if siblings != []:
                    print("\nSiblings:")
                    for sibling in siblings:
                        print(sibling)

                # Try to find grandparents if atleast one of the
                # parents were found.
                print("\nMother's parents")
                print("Grandmother:", mother.get_mother(people))
                print("Grandfather:", mother.get_father(people))
                print("\nFather's parents:")
                print("Grandmother:", father.get_mother(people))
                print("Grandfather:", father.get_father(people))

        else:
            print("Unfortunately, name", name, "was not found.")

        print("\nEnter person's name or type 'list' to see all names.")
        name = input()


main()
