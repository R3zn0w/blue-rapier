import domowe
import unittest


class Test_domowe(unittest.TestCase):
    channels = {'Channel1': [], 'Channel2': [],
                'Channel3': [], 'Channel4': []}
    users = {'User1': [], 'User2': [], "User3": []}
    testContent = domowe.Content(channels, users)
    testHandler = domowe.CmdHandler(testContent)

    def test_validation_correct(self):
        self.assertEqual(self.testContent.validate(
            "Channel2", "User1")[0], True)

    def test_validation_invalid_user(self):
        self.assertEqual(self.testContent.validate(
            "Channel2", "User9")[1], "This is not a legal user!")

    def test_validation_invalid_channel(self):
        self.assertEqual(self.testContent.validate(
            "Channel7", "User1")[1], "This is not a legal channel!")

    def test_content_subscribe(self):
        self.assertEqual(self.testContent.subscribe(
            "Channel1", "User1"), "Subscribed succesfully")
        self.assertEqual(self.testContent.subscribe(
            "Channel1", "User1"), "You are already subscribing to this channel!")

    def test_content_unsubscribe(self):
        self.testContent.subscribe(
            "Channel1", "User1")
        self.assertEqual(self.testContent.unsubscribe(
            "Channel1", "User1"), "Unsubscribed succesfully")
        self.assertEqual(self.testContent.unsubscribe(
            "Channel1", "User1"), "You are not subscribing to this channel!")

    def test_content_edit(self):
        self.testContent.subscribe(
            "Channel1", "User1")
        self.assertEqual(self.testContent.edit_content(
            "Channel1", "User1", "kukuryku"), "Content changed succesfully")

    def test_content_edit_fail(self):
        self.testContent.unsubscribe(
            "Channel1", "User1")
        self.assertEqual(self.testContent.edit_content(
            "Channel1", "User2", "kukuryku"), "You are not subscribing to this channel!")


if __name__ == '__main__':
    unittest.main()
