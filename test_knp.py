import unittest
import knp


class TestKnp(unittest.TestCase):
    def test_Choice(self):
        self.assertEqual(knp.Choice.Rock.name, 'Rock')
        self.assertEqual(knp.Choice.Rock.value, 'r')
        self.assertEqual(knp.Choice.Scissors.name, 'Scissors')
        self.assertEqual(knp.Choice.Scissors.value, 's')
        self.assertEqual(knp.Choice.Paper.name, 'Paper')
        self.assertEqual(knp.Choice.Paper.value, 'p')
        self.assertEqual(knp.Choice.Quit.name, 'Quit')
        self.assertEqual(knp.Choice.Quit.value, 'q')

    def test_get_user_sel(self):
        pass

    def test_get_computer_sel(self):
        pass

    def test_determine_winner(self):
        self.assertTrue(knp.determine_winner(knp.Choice.Rock, knp.Choice.Scissors))
        self.assertIsNone(knp.determine_winner(knp.Choice.Rock, knp.Choice.Rock))
        self.assertFalse(knp.determine_winner(knp.Choice.Rock, knp.Choice.Paper))

    def test_print_winner(self):
        pass

    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()
