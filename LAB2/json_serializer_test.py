import unittest
from json_serializer import to_json
import json


class Worker:
    def __init__(self, name, surname, year, pay):
        self.name = name
        self.surname = surname
        self.year = year
        self.pay = pay

class TestJSONSerialiser(unittest.TestCase):
    def test_int(self):
        type_int = 5304
        self.assertTrue(to_json(type_int) == json.dumps(type_int) )

    def test_float(self):
        type_float = 327.59
        self.assertTrue(to_json(type_float) == json.dumps(type_float))

    def test_bool_true(self):
        type_bool_true = True
        self.assertTrue(to_json(type_bool_true) == json.dumps(type_bool_true))

    def test_bool_falce(self):
        type_bool_falce = False
        self.assertTrue(to_json(type_bool_falce) == json.dumps(type_bool_falce))

    def test_none(self):
        type_none = None
        self.assertTrue(to_json(type_none) == json.dumps(type_none))

    def test_string(self):
        type_string = "some string"
        self.assertTrue(to_json(type_string) == json.dumps(type_string))

    def test_tuple(self):
        type_tuple = (12.00, 34.85, 78.05)
        self.assertTrue(to_json(type_tuple) == json.dumps(type_tuple))

    def test_dict(self):
        type_dict = {"Tom": 2003, "John": 1999, "Bob": 2012}
        self.assertTrue(to_json(type_dict) == json.dumps(type_dict))

    def test_list(self):
        type_list = [1000, 1845, 3061]
        self.assertTrue(to_json(type_list) == json.dumps(type_list))

    def test_user_class(self):
        worker = Worker("Tom", "Jonson", 23, 5000)
        self.assertTrue(to_json(worker) == json.dumps(worker.__dict__))

    def test_list_nesting(self):
        list_list_nesting = [[10, 6.88, "Tom"], [4, 5], [3, 6, 0.56]]
        tuple_list_nesting=[(0, 6.88, "Tom"), (4, 5), (3, 6, 0.56)]
        dict_list_nesting =[{"Tom": 2003, "John": 1999},{"Bob": 2012,"Adam": 2005}]
        ll_nestings_equal=to_json(list_list_nesting) == json.dumps(list_list_nesting)
        tl_nestings_equal=to_json(tuple_list_nesting) == json.dumps(tuple_list_nesting)
        dl_nestings_equal = to_json(dict_list_nesting) == json.dumps(dict_list_nesting)
        self.assertTrue(ll_nestings_equal and tl_nestings_equal and dl_nestings_equal)

    def test_tuple_nestin(self):
        tuple_tuple_nesting = ((10, 6.88, "Tom"), (4, 5), (3, 6, 0.56))
        list_tuple_nesting = ((0, 6.88, "Tom"), (4, 5), (3, 6, 0.56))
        dict_tuple_nesting = ({"Tom": 2003, "John": 1999}, {"Bob": 2012, "Adam": 2005})
        tt_nestings_equal = to_json(tuple_tuple_nesting) == json.dumps(tuple_tuple_nesting)
        lt_nestings_equal = to_json(list_tuple_nesting) == json.dumps(list_tuple_nesting)
        dt_nestings_equal = to_json(dict_tuple_nesting) == json.dumps(dict_tuple_nesting)
        self.assertTrue(tt_nestings_equal and lt_nestings_equal and dt_nestings_equal)

    def test_dict_nestin(self):
        dict_dict_nesting = {"more that 18": {"Tom": 2000, "John": 1999}, "less that 18": {"Bob": 2012, "Adam": 2007}}
        tuple_dict_nesting = {'integer numbers': (4, 5), "real numbers": (3.0, 6.1, 0.56), "strings": ("Bob", "Tom")}
        list_dict_nesting = {"integer numbers": [4, 5], "real numbers": [3.0, 6.1, 0.56], "strings": ["Bob", "Tom"]}
        dd_nestings_equal = to_json(dict_dict_nesting) == json.dumps(dict_dict_nesting)
        td_nestings_equal = to_json(tuple_dict_nesting) == json.dumps(tuple_dict_nesting)
        ld_nestings_equal = to_json(list_dict_nesting) == json.dumps(list_dict_nesting)
        self.assertTrue(dd_nestings_equal and td_nestings_equal and ld_nestings_equal)

if __name__ == '__main__':
    unittest.main()
