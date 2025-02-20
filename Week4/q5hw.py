class StringReverser:
    def __init__(self, s):
        self.s = s

    def reverse_words(self):
        words = self.s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

s = "Hello world from Python"
reverser = StringReverser(s)
result = reverser.reverse_words()
print("Reversed string:", result)