class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        interpret = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interpret = interpret + "G"
                i = i + 1
            elif command[i: i + 2] == "()":
                interpret = interpret + "o"
                i = i + 2
            elif command[i: i + 4] == "(al)":
                interpret = interpret + "al"
                i = i + 4
        return interpret

        