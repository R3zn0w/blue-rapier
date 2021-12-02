class Content:
    def __init__(self, channels, users) -> None:
        self.channels = channels  # kanały i content
        self.users = users  # userzy i suby

    def validate(self, channel: str, user: str) -> tuple[bool, str]:
        if not channel in self.channels:
            return (False, "This is not a legal channel!")
        elif not user in self.users:
            return (False, "This is not a legal user!")
        return (True, "NONE")

    def subscribe(self, channel: str, user: str) -> str:
        try:
            if not self.validate(channel, user)[0]:
                return self.validate(channel, user)[1]
            elif channel in self.users[user]:
                return "You are already subscribing to this channel!"
            else:
                self.users[user].append(channel)
                return "Subscribed succesfully"
        except:
            return "Fatal error while subscribing"

    def unsubscribe(self, channel: str, user: str) -> str:
        try:
            if not self.validate(channel, user)[0]:
                return self.validate(channel, user)[1]
            elif not channel in self.users[user]:
                return "You are not subscribing to this channel!"
            else:
                self.users[user].remove(channel)
                return "Unsubscribed succesfully"
        except:
            return "Fatal error while unsubscribing"

    def edit_content(self, channel: str, user: str, content: str) -> str:
        try:
            if not self.validate(channel, user)[0]:
                return self.validate(channel, user)[1]
            elif not channel in self.users[user]:
                return "You are not subscribing to this channel!"
            else:
                self.channels[channel] = content
                return "Content changed succesfully"
        except:
            return "Fatal error while editing"

    def show_info(self):
        for channel in self.channels:
            print(channel, "content: ", self.channels[channel])
        for user in self.users:
            print(user, "subscribes to channels: ", self.users[user])


class CmdHandler():
    def __init__(self, contentInstance: Content) -> None:
        self.contentInstance = contentInstance
        self.operations = ['subscribe', 'unsubscribe',
                           'edit', 'info']

    def print_help(self):
        print("Use:")
        print("Legal operations:")
        print("*subscribe [userName] [channelName] - subscribes to channel")
        print(
            "*unsubscribe [userName] [channelName] - unsubscribes from channel")
        print(
            "*edit [userName] [channelName] [newContent] - edits contents of channel")
        print("*info - prints information about everything")

    def do_operation(self, command: str):
        commands = command.split(" ")
        if not commands[0] in self.operations:
            return "Illegal operation"
        return{
            'subscribe': lambda commands: self.contentInstance.subscribe(commands[2], commands[1]),
            'unsubscribe': lambda commands: self.contentInstance.unsubscribe(commands[2], commands[1]),
            'edit': lambda commands: self.contentInstance.edit_content(commands[2], commands[1], commands[3]),
            'info': lambda commands: self.contentInstance.show_info(),
        }[commands[0]](commands)


content = Content({'Channel1': [], 'Channel2': [],
                   'Channel3': [], 'Channel4': []}, {'User1': [], 'User2': [], "User3": []})
handler = CmdHandler(content)
handler.print_help()
while True:
    try:
        operation = input("Next operation: ")
        response = handler.do_operation(operation)
        print(response)
    except EOFError:
        print("Exiting")
        break
    except KeyboardInterrupt:
        print("Exiting")
        break
