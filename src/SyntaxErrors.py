from antlr4.error.ErrorListener import ErrorListener

class CustomSyntaxError(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax error on {}:{} ~> {}".format(line, column, msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass