import readline

class Autocomplete:
    def __init__(self, commands):
        self.commands = commands

    def complete(self, text, symbol_iter):
        results =  [x for x in self.commands if x.startswith(text)] + [None]
        self.results = results
        return results[symbol_iter]

words = ['echo', 'exit']
completer = Autocomplete(words)

#readline.set_completer_delims(' ')
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

line = input()

print(completer.results)
