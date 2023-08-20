import unittest
from oper_trans import is_valid


class TestOperTrans(unittest.TestCase):
    def test_1(self):
        print("")
        print("test_1 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "Repl.it uses operational transformations.",
            '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]',
        )
        print("")
        # true

    def test_2(self):
        print("test_2 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "Repl.it uses operational transformations.",
            '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]',
        )
        print("")
        # false, delete past end

    def test_3(self):
        print("test_3 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "Repl.it uses operational transformations.",
            '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]',
        )
        print("")
        # false, skip past end

    def test_4(self):
        print("test_4 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "We use operational transformations to keep everyone in a multiplayer repl in sync.",
            '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]',
        )
        print("")
        # true

    def test_5(self):
        print("test_5 => ")
        is_valid(
            "Nice",
            "Nicez",
            '[{"op": "insert", "chars": "z"}]',
        )
        print("")
        # false

    def test_6(self):
        print("test_6 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "We can use operational transformations to keep everyone in a multiplayer repl in sync.",
            '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]',
        )
        print("")
        # false

    def test_7(self):
        print("test_7 => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "[]",
        )
        print("")
        # true

    def test_insert(self):
        print("test_insert => ")
        stale = ""
        latest = "Hello, human!"
        otjson = '[{"op": "insert", "chars": "Hello, human!"}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_skip(self):
        print("test_skip => ")
        is_valid(
            "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
            "Repl.it uses operational transformations.",
            '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]',
        )
        # false, skip past end

    def test_skip_insert(self):
        print("test_skip insert => ")
        stale = "Nice!"
        latest = "Nice day!"
        otjson = '[{"op": "skip", "count": 4}, {"op": "insert", "chars": " day"}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_skip_delete(self):
        print("test_skip delete => ")
        stale = "What is up?"
        latest = "What is?"
        otjson = '[{"op": "skip", "count": 7}, {"op": "delete", "count": 3}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_1(self):
        print("test_check-1 => ")
        stale = "anashwara"
        latest = "anzwara"
        otjson = '[{"op": "skip", "count": 2}, {"op": "delete", "count": 3}, {"op": "insert", "chars": "z"}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_2(self):
        print("test_check-2 => ")
        stale = "anashwara"
        latest = "anzash"
        otjson = '[{"op": "skip", "count": 2}, {"op": "insert", "chars": "z"}, {"op": "skip", "count": 3}, {"op": "delete", "count": 4}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_3(self):
        print("test_check-3 => ")
        stale = "anashwara"
        latest = "shzwara"
        otjson = '[{"op": "delete", "count": 3}, {"op": "skip", "count": 2},  {"op": "insert", "chars": "z"}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_4(self):
        print("test_check-4 => ")
        stale = "anashwara"
        latest = "zanara"
        otjson = '[{"op": "insert", "chars": "z"}, {"op": "skip", "count": 2}, {"op": "delete", "count": 4}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_5(self):
        print("test_check-5 => ")
        stale = "anashwara"
        latest = "zshwara"
        otjson = '[{"op": "delete", "count": 3}, {"op": "insert", "chars": "z"}, {"op": "skip", "count": 2}]'
        is_valid(stale, latest, otjson)
        print("")
        # True

    def test_check_6(self):
        print("test_check-6 => ")
        stale = "anashwara"
        latest = "zhwara"
        otjson = '[{"op": "insert", "chars": "z"}, {"op": "delete", "count": 4}, {"op": "skip", "count": 10}]'
        is_valid(stale, latest, otjson)
        print("")
        # True


if __name__ == "__main__":
    unittest.main()
