import readline

class Autocomplete:
    def __init__(self, commands):
        self.commands = commands
        self.results = None
        self.state = None

    def complete(self, text, state):
        results =  [x for x in self.commands if x.startswith(text)] + [None]
        self.results = results
        self.state = state
        return results[state]

words = ['echo', 'exit']
completer = Autocomplete(words)

#readline.set_completer_delims(' ')
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

line = input()

print(completer.results)
print(completer.state)