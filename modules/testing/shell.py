import argparse
import testing
import testing.run
import testing.tests
import testing.printers
import dyn


def parseSettings():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', help='Verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-s', '--statistics', help='Statistics verbosity level (0=silent, 1=default)', default=1, type=int)
    parser.add_argument('-n', '--count', help='Number of tests to run', default=float('inf'), type=int)
    args = parser.parse_args()

    return dict(printer=testing.printers.Printer(), verbosity=args.verbosity, maxTests=args.count)


def printStatistics():
    printer = testing.environment.settings.printer

    with testing.environment.settings.let(verbosity=args.statistics):
        printer.log(1, "Passed tests: {}", len(environment.run.passed))
        printer.log(1, "Failed tests: {}", len(environment.run.failed))
        printer.log(1, "Skipped tests: {}", len(environment.run.skipped))
        
        printer.log(1, "Score: {}", format(score))


def main():
    root = testing.tests.CumulativeTestSuite()
    settings = parseSettings()
    
    with testing.environment.let(tests = dyn.create(), settings = dyn.create(), run = dyn.create()), \
         testing.environment.tests.let(top=root, context=[], path="", condition = testing.conditions.limitTestCount()), \
         testing.environment.settings.let( **settings ):
        testing.run.loadTestsRecursively()
        testing.run.runTests()
