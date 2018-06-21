import os
from Bio.PDB import PDBParser

__author__ = 'Pawel'

class Solution():
    def __init__(self, problem, problemId, fileName):
        self.problem = problem
        self.problemId = problemId
        self.fileName = fileName
        self.isSolution = "solution" in fileName
        self.commonAtomThisSolution = []
        self.commonAtomRealSolution = []

        parser = PDBParser(QUIET=True)
        self.structure = parser.get_structure('PHA-L', os.path.join("data", self.problemId, self.fileName))
        if self.problem.showProgress:
            print("Loaded:", os.path.join("data", self.problemId, self.fileName))