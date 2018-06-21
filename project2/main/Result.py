import os
from Bio import PDB
from project2.main.Solution import Solution

__author__ = 'Pawel'

class Result():
    def __init__(self, resultSet, solution):
        self.resultSet = resultSet
        self.solution = solution

        self.rmsd = None
        self.inf = None
        self.di = None