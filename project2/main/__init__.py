import os
from project2.main.Problem import Problem

__author__ = 'Pawel'

if __name__ == "__main__":

    # Requires having normalized, unzipped RNA-Puzzles_dataset from:
    # https://github.com/RNA-Puzzles/RNA-Puzzles_dataset in the following directory structure:
    #
    # data
    # - Problem0007
    # - - 7_Adamiak_1.pdb
    # - - 7_Adamiak_2.pdb
    # - - 7_Adamiak_2.pdb
    # - - 7_Adamiak_2.pdb
    # - - 7_solution_0.pdb
    # - - 7_solution_1.pdb
    # - ExampleProblem
    # - - UserAnswer.pdb
    # - - AnotherAnswwer.pdb
    # - - solution.pdb
    #

    if True:
        # Loads a directory "data/Problem0007"
        problem = Problem("Problem0007", showProgress=True)

        # Compare results with the 1st solution
        # Indexing starts from 0, different problems have different amounts of solutions.
        problem.setMainSolution(0)
        # Generates results, by calculating RMSD, INF and DI of pdb files in relation to "solution 0"
        resultSet = problem.generateResults()

        # Prints out pdb fileNames with an RMSD score.
        # Smallest values will be printed first
        # None values will be printed last and are caused by dividing by 0.
        resultSet.print_RMSD()

        # Prints out pdb fileNames with an INF score.
        # Largest values will be printed first
        # None values will be printed last and are caused by not having common atoms
        resultSet.print_INF()

        # Prints out pdb fileNames with an DI score.
        # Largest values will be printed first
        # None values will be printed last and are caused by not having common atoms
        resultSet.print_DI()

        # The following lines create results using another solution.
        problem.setMainSolution(1)
        resultSet = problem.generateResults()

        resultSet.print_RMSD()
        resultSet.print_INF()
        resultSet.print_DI()

    # Calculates all results, but may take a long time (~1 hour)
    if False:
        # directory MUST be called "data"
        subdirectories = os.listdir("data")

        for subdir in subdirectories:
            problem = Problem(subdir)

            for i, solution in enumerate(problem.mainSolutions):
                problem.setMainSolution(i)
                resultSet = problem.generateResults()
                resultSet.print_RMSD()
                resultSet.print_INF()
                resultSet.print_DI()
