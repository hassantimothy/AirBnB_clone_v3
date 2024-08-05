#!/usr/bin/python3

# test_get_count.py
#!/usr/bin/python3

# test_get_count.py
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

def test_get_count():
    # Print the count of all objects and State objects
    print("All objects: {}".format(storage.count()))
    print("State objects: {}".format(storage.count(State)))

    # Try to get the first state object
    states = list(storage.all(State).values())
    if states:
        first_state_id = states[0].id
        print("First state: {}".format(storage.get(State, first_state_id)))
    else:
        print("No State objects found.")

if __name__ == "__main__":
    test_get_count()
