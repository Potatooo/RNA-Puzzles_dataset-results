import os
from Bio import PDB
from project2.main.Solution import Solution

__author__ = 'Pawel'

class ResultSet():
    def __init__(self, problemId, mainSolution):
        self.problemId = problemId
        self.mainSolution = mainSolution
        self.results = []

    def _print_header(self, title):
        print(title)
        print("PROBLEM:", self.problemId)
        print("SOLUTION:", self.mainSolution.fileName)

    def print_RMSD(self):
        self._print_header("RMSD")
        sortedList = sorted(self.results, key=lambda x: (x.rmsd is None, x.rmsd), reverse=False)
        for i in sortedList:
            print(i.solution.fileName, i.rmsd)

    def print_INF(self):
        self._print_header("INF")
        sortedList = sorted(self.results, key=lambda x: (x.inf is None, x.inf), reverse=True)
        for i in sortedList:
            print(i.solution.fileName, i.inf)

    def print_DI(self):
        self._print_header("DI")
        sortedList = sorted(self.results, key=lambda x: (x.di is None, x.di), reverse=False)
        for i in sortedList:
            print(i.solution.fileName, i.di)