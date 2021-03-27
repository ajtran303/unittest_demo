import unittest


class TestImaginaryFriend(unittest.TestCase):

    def test_it_exists(self):
        friend = ImaginaryFriend()
        self.assertIsInstance(friend, ImaginaryFriend)

    def test_it_has_attributes(self):
        friend = ImaginaryFriend()
        self.assertEqual(friend.name, 'Yet Un-named')
        self.assertEqual(friend.type, 'Imaginary Friend')

    def test_it_has_a_dunder_repr(self):
        friend = ImaginaryFriend()
        expected = f'<{ImaginaryFriend.__name__}(name={friend.name},type={friend.type})>'
        self.assertEqual(repr(friend), expected)

    def test_it_has_a_dunder_str(self):
        friend = ImaginaryFriend()
        expected = f'{friend.name}, The {friend.type}'
        self.assertEqual(str(friend), expected)

    def test_it_can_be_a_different_friend(self):
        new_friend = ImaginaryFriend(name='Casper', type='Friendly Ghost')
        self.assertIsInstance(new_friend, ImaginaryFriend)

    def test_it_can_have_different_attributes(self):
        # use double splat in dunder init
        friend_params = {'name': 'Casper', 'type': 'Friendly Ghost'}
        new_friend = ImaginaryFriend(friend_params)
        # new_friend = ImaginaryFriend(name='Casper', type='Friendly Ghost')
        self.assertEqual(new_friend.name, friend_params['name'])
        self.assertEqual(new_friend.type, friend_params['type'])

    def test_it_has_a_different_dunder_repr(self):
        new_friend = ImaginaryFriend(name='Casper', type='Friendly Ghost')
        expected = f'<{ImaginaryFriend.__name__}(name={new_friend.name},type={new_friend.type})>'
        self.assertEqual(repr(new_friend), expected)

    def test_it_has_a_different_dunder_str(self):
        friend = ImaginaryFriend()
        expected = f'{friend.name}, The {friend.type}'
        self.assertEqual(str(friend), expected)


if __name__ == '__main__':
    unittest.main()
