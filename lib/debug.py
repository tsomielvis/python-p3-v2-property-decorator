# lib/test_dog.py

from dog import Dog
import pytest

class TestDogProperties:
    '''Class Dog in dog.py'''

    def test_name_breed_valid(self):
        '''validates name and breed properties are initialized with valid values'''
        try:
            # No exception should be thrown since name and breed are valid
            dog = Dog("Fido", "Corgi")
        except Exception as exc:
            # The assertion fails if an exception is thrown
            assert False, f'Dog("Fido", "Corgi") raised an exception {exc}'

    def test_name_is_string_valid_length(self):
        '''validates name property is assigned a string between 1 and 25 characters'''
        dog = Dog("Fido", "Corgi")
        with pytest.raises(ValueError):
            dog.name = 7  # not a string
        with pytest.raises(ValueError):
            dog.name = ''  # too short
        with pytest.raises(ValueError):
            dog.name = 'Fido the adorable Corgi who likes to steal socks'  # too long

    def test_breed_is_approved_breed(self):
        '''validates breed property is in list of approved choices'''
        dog = Dog("Snoopy", "Beagle")
        with pytest.raises(ValueError):
            dog.breed = "Poodle"  # not an approved breed

# lib/test_person.py

from person import Person
import pytest

class TestPersonProperties:
    '''Class Person in person.py'''

    def test_name_job_valid(self):
        '''validates name and job properties are initialized with valid values'''
        try:
            # No exception should be thrown since name and job are valid
            person = Person("Alice", "ITC")
        except Exception as exc:
            # The assertion fails if an exception is thrown
            assert False, f'Person("Alice", "ITC") raised an exception {exc}'

    def test_name_is_string_valid_length(self):
        '''validates name property is assigned a string between 1 and 25 characters'''
        person = Person("Alice", "ITC")
        with pytest.raises(ValueError):
            person.name = 7  # not a string
        with pytest.raises(ValueError):
            person.name = ''  # too short
        with pytest.raises(ValueError):
            person.name = 'Alice the incredible IT specialist who loves coding'  # too long

    def test_job_is_approved_job(self):
        '''validates job property is in list of approved choices'''
        person = Person("Bob", "Finance")
        with pytest.raises(ValueError):
            person.job = "Actor"  # not an approved job