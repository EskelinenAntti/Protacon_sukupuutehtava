"""
A class that contains person's data.
"""

class Person:

    def __init__(self, id, first_name, last_name, mother, father):
        """A Constructor that takes person's name, id, as age."""
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__mother_id = self.__to_int(mother)
        self.__father_id = self.__to_int(father)

    def __str__(self):
        """Returns persons full name when asked as a string."""
        return self.__first_name + " " + self.__last_name

    def get_id(self):
        return self.__id

    def get_last_name(self):
        """Returns persons last_name"""
        return self.__last_name

    def get_mother(self, people_dict, return_format="object"):
        """
        Find person's mother from a dict containing all person-objects. Return
        the object or it's id. If mother is not found from the dict or
        the return_format is no defined, return "Unknown".
        string "Unknown"
        :param people_dict: A dict containing all Person-objects as values.
        :param return_format: Return type. If "object" the whole object is
        returned. If "id" only the id-attribute of that object is returned.
        :return: Person-object or it's id or "Unknown" if it cannot be found
        from the dict or the return_format is undefined.
        """
        if self.__mother_id != -1:
            for person in people_dict:
                if people_dict[person].get_id() == self.__mother_id:
                    if return_format == "object":
                        return people_dict[person]
                    elif return_format == "id":
                        return people_dict[person].get_id()

            # If person not in people_dict return "Unknown"
            return "Unknown"

        else:
            return "Unknown"

    def get_father(self, people_dict, return_format="object"):
        """
        Find person's father from a dict containing all person-objects. Return
        the object or it's id. If father is not found from the dict or
        the return_format is no defined, return "Unknown".
        string "Unknown"
        :param people_dict: A dict containing all Person-objects as values.
        :param return_format: Return type. If "object" the whole object is
        returned. If "id" only the id-attribute of that object is returned.
        :return: Person-object or it's id. "Unknown" if it cannot be found
        from the dict or the return_format is undefined.
        """
        if self.__father_id != -1:
            for person in people_dict:
                if people_dict[person].get_id() == self.__father_id:
                    if return_format == "object":
                        return people_dict[person]
                    elif return_format == "id":
                        return people_dict[person].get_id()

            # If person is not in people_dict return "Unknown"
            return "Unknown"

        else:
            return "Unknown"

    def get_siblings(self, people_dict):
        """
        Find siblings and return them as objects in a list.
        :param people_dict: A dict containing all Person-objects as values.
        :return: List of People-objects that have same parent/s. If there
        aren't any return an empty list.
        """

        siblings = []
        for person in people_dict:
            # Search for common mothers
            if people_dict[person].get_mother(people_dict, return_format="id")\
                    == self.__mother_id:
                sibling = people_dict[person]
                if sibling not in siblings and sibling != self:
                    siblings.append(sibling)
            # Search for common fathers
            if people_dict[person].get_father(people_dict, return_format="id")\
                    == self.__father_id:
                sibling = people_dict[person]
                if sibling not in siblings and sibling != self:
                    siblings.append(sibling)
        return siblings

        # If person not in people_dict return "Unknown"
        return "Unknown"

    def __to_int(self, value):
        """
        Check if value is an int and returns it if it is. Otherwise, return
        -1.
        :param value: Value to check.
        :return: @value if it's an int. -1 if it's not.
        """
        try:
            return int(value)
        except TypeError:
            return -1

