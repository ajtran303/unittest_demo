import unittest
from classes.imaginary_friend import ImaginaryFriend


class SmokeTest(unittest.TestCase):
    def setUp(self):
        self.friend = ImaginaryFriend()

    def test_it_exists(self):
        self.assertIsInstance(self.friend, ImaginaryFriend)

    def test_it_has_default_attributes(self):
        self.assertEqual(self.friend.name, 'Yet Un-named')
        self.assertEqual(self.friend.type, 'Imaginary Friend')

    def test_it_has_a_dunder_repr(self):
        expected = f'<ImaginaryFriend(name={self.friend.name},type={self.friend.type})>'
        self.assertEqual(repr(self.friend), expected)

    def test_it_has_a_dunder_str(self):
        expected = f'{self.friend.name}, The {self.friend.type}'
        self.assertEqual(str(self.friend), expected)


class SmokeTest2(unittest.TestCase):
    def setUp(self):
        self.friend_2 = ImaginaryFriend(name='Casper', type='Friendly Ghost')

    def test_it_exists_with_kwargs(self):
        self.assertIsInstance(self.friend_2, ImaginaryFriend)
        self.assertEqual(self.friend_2.name, 'Casper')
        self.assertEqual(self.friend_2.type, 'Friendly Ghost')

    def test_it_has_a_different_dunder_repr(self):
        expected = f'<ImaginaryFriend(name={self.friend_2.name},type={self.friend_2.type})>'
        self.assertEqual(repr(self.friend_2), expected)

    def test_it_has_a_different_dunder_str(self):
        expected = f'{self.friend_2.name}, The {self.friend_2.type}'
        self.assertEqual(str(self.friend_2), expected)


class SmokeTest3(unittest.TestCase):
    def test_it_exists_with_some_kwargs_1(self):
        new_friend = ImaginaryFriend(name='Casper')
        self.assertIsInstance(new_friend, ImaginaryFriend)
        self.assertEqual(new_friend.name, 'Casper')
        self.assertEqual(new_friend.type, 'Imaginary Friend')

    def test_it_exists_with_some_kwargs_2(self):
        new_friend = ImaginaryFriend(type='Spooky Ghost')
        self.assertIsInstance(new_friend, ImaginaryFriend)
        self.assertEqual(new_friend.name, 'Yet Un-named')
        self.assertEqual(new_friend.type, 'Spooky Ghost')


class SmokeTest4(unittest.TestCase):
    def setUp(self):
        self.friend_params = {'name': 'Casper', 'type': 'Friendly Ghost'}
        self.new_friend = ImaginaryFriend(**self.friend_params)

    def test_it_can_init_with_params(self):
        self.assertIsInstance(self.new_friend, ImaginaryFriend)
        self.assertEqual(self.new_friend.name, self.friend_params['name'])
        self.assertEqual(self.new_friend.type, self.friend_params['type'])
       
    def test_it_has_dunders(self):
        expected_str = f'{self.new_friend.name}, The {self.new_friend.type}'
        expected_repr = f'<ImaginaryFriend(name={self.new_friend.name},type={self.new_friend.type})>'
        self.assertEqual(str(self.new_friend), expected_str)
        self.assertEqual(repr(self.new_friend), expected_repr)


class ValidationsTest(unittest.TestCase):
    def test_it_raises_type_error_1(self):
        with self.assertRaises(TypeError):
            wrong_params = {'nombre': 'Casper'}
            ImaginaryFriend(**wrong_params)

    def test_it_raises_type_error_2(self):
        with self.assertRaises(TypeError):
            ImaginaryFriend(nombre='Casper')


if __name__ == '__main__':
    unittest.main()
