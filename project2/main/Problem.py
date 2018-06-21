import os
from Bio import PDB
from project2.main.Result import Result
from project2.main.ResultSet import ResultSet
from project2.main.Solution import Solution

__author__ = 'Pawel'

def atomIsSame(a, b):
    if a.name != b.name:
        return False
    if a.get_parent().get_parent().id != b.get_parent().get_parent().id:
        return False
    return True

def getCommonAtoms(aList, bList):
    r1 = []
    r2 = []

    y = 0
    n = 0
    used1 = {}
    used2 = {}

    for i in aList:
        if i in used1:
            continue
        for j in bList:
            if i in used1:
                continue
            if j in used2:
                continue
            if atomIsSame(i, j):
                y += 1
                used1[i] = i
                used2[j] = j
                r1.append(i)
                r2.append(j)
            else:
                n += 1

    return r1, r2

class Problem():
    def __init__(self, problemId, showProgress=True):
        self.problemId = problemId
        self.currentMainSolution = None
        self.mainSolutions = []
        self.solutions = []
        self.showProgress = showProgress

        self._load(problemId)

    def setMainSolution(self, index):
        self.currentMainSolution = self.mainSolutions[index]

    def _load(self, problemId):
        dir = "data"
        subdirectories = os.listdir(dir)

        for subdir in subdirectories:
            if problemId != subdir:
                continue
            for root, dirs, files in os.walk(os.path.join(dir, subdir)):
                for fileName in files:
                    fullPath = os.path.join("data", subdir, fileName)
                    if fileName.endswith(".pdb") and not fileName.startswith("."):
                        if "solution" in fileName:
                            solution = Solution(self, subdir, fileName)
                            self.currentMainSolution = solution
                            self.mainSolutions.append(solution)
                        else:
                            solution = Solution(self, subdir, fileName)
                            if not solution.isSolution:
                                self.solutions.append(solution)

    def _calculateCommonAtoms(self):
        for solution in self.solutions:
            commonAtomThisSolution, commonAtomRealSolution = getCommonAtoms(list(self.currentMainSolution.structure.get_atoms()), list(solution.structure.get_atoms()))
            solution.commonAtomThisSolution = commonAtomThisSolution
            solution.commonAtomRealSolution = commonAtomRealSolution
            if self.showProgress:
                print("Calculated atoms:", os.path.join("data", solution.problemId, solution.fileName))

    def generateResults(self):
        self._calculateCommonAtoms()
        resultSet = ResultSet(self.problemId, self.currentMainSolution)

        #prepare results
        for solution in self.solutions:
            result = Result(resultSet, solution)
            resultSet.results.append(result)

        #rmsd
        for i in resultSet.results:
            solution = i.solution
            try:
                sup = PDB.Superimposer()
                sup.set_atoms(solution.commonAtomRealSolution , solution.commonAtomThisSolution)
                sup.apply(solution.commonAtomThisSolution)
                i.rmsd = sup.rms
            except ZeroDivisionError:
                pass

        #INF
        for i in resultSet.results:
            solution = i.solution

            solutionCount = len(list(solution.structure.get_atoms()))
            realSolutionCount = len(list(self.currentMainSolution.structure.get_atoms()))
            commonCount = len(solution.commonAtomRealSolution)

            i.inf = (commonCount)/(solutionCount+realSolutionCount-commonCount)

        #DI
        for i in resultSet.results:
            solution = i.solution

            try:
                i.di = i.rmsd / i.inf
            except (ZeroDivisionError, TypeError) as e:
                pass

        return resultSet
