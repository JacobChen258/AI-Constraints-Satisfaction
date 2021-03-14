from .csp import CSP
from .csp_util import CSPUtil
from .variable import Variable


class CSPAlgorithms:

    # Here you will implement all the Constraint Solving Algorithms. Below are functions we think
    # will be helpful in your implementations. Please read the handout for specific instructions
    # for each algorithm.

    # Helpful Functions:
    # CSP.unassigned_variables() --> returns a list of the unassigned variables left in the CSP
    # CSP.assignments() --> returns a dictionary which holds variable : value pairs
    # CSP.extract_unassigned() --> returns the next unassigned variable in line
    # CSP.assign(variable, value) --> assigns the given value to the given variable
    # CSP.unassign(variable) --> unassigns the given variable (value = None)
    # CSP.constraints() --> returns a list of constraints for the CSP
    # CSP.num_unassigned() --> returns the number of unassigned variables
    # Variable.domain() --> returns the domain of the variable instance
    # Constraint.check(variables, assignments) --> returns True iff the given variables and their assignments
    #                                              satisfy the constraint instance

    @staticmethod
    def backtracking(csp):
        # Qustion 3, your backtracking algorithm goes here.

        # Returns an assignment of values to the variables such that the constraints are satisfied. None
        # if no assignment is found.
        assignments, solution_found = CSPAlgorithms.backtracking_helper(csp, False)
        if solution_found:
            return assignments
        return None

    @staticmethod
    def backtracking_helper(csp, solution_found):
        if not csp.unassigned_variables():
            return csp.assignments(), True
        var = csp.extract_unassigned()
        assignments = csp.assignments()
        solution = solution_found
        for val in var.domain():
            csp.assign(var, val)
            constraintOK = True
            for constraint in csp.constraints():
                if csp.num_unassigned() == 0:
                    if not constraint.check(csp.variables(), csp.assignments()):
                        constraintOK = False
                        break
            if constraintOK:
                assignments, solution = CSPAlgorithms.backtracking_helper(csp, solution_found)
        return assignments, solution

    @staticmethod
    def forward_checking(csp):
        # Question 4, your foward checking algorithm goes here.

        # Returns an assignment of values to the variables such that the constraints are satisfied. None
        # if no assignment is found.

        # Helpful Functions:
        # CSPUtil.forward_check(csp, constraint, var) --> returns True iff there is no DWO when performing
        #                                                 a forward check on the given constraint and variable.
        # CSPUtil.undo_pruning_for(var) --> undoes all pruning that was caused by forward checking the given variable.

        assignments, solution_found = CSPAlgorithms.forwardchecking_helper(csp, False)
        if solution_found:
            return assignments
        return None

    @staticmethod
    def forwardchecking_helper(csp, solution_found):
        if not csp.unassigned_variables():
            return csp.assignments(), True
        var = csp.extract_unassigned()
        assignments = csp.assignments()
        solution = solution_found
        for val in var.active_domain():
            csp.assign(var, val)
            noDWO = True
            for constraint in csp.constraints():
                if csp.num_unassigned() == 1:
                    if not CSPUtil.forward_check(csp, constraint, var):
                        noDWO = False
                        break
            if noDWO:
                assignments, solution = CSPAlgorithms.forwardchecking_helper(csp, solution_found)
            CSPUtil.undo_pruning_for(var)
        return assignments, solution

    @staticmethod
    def gac(csp):
        # Question 6, your gac algorithm goes here.

        # Returns an assignment of values to the variables such that the constraints are satisfied. None
        # if no assignment is found.

        # Helpful Functions:
        # CSPUtil.gac_enfore(csp, var) --> returns True iff there is no DWO when attempting to enforce consistency
        #                                  on the constraints of the csp for the given variable.
        # CSPUtil.undo_pruning_for(var) --> undoes all pruning that was caused by forward checking the given variable.

        assignments, solution_found = CSPAlgorithms.gac_helper(csp, False)
        print(solution_found)
        if solution_found:
            return assignments
        return None

    @staticmethod
    def gac_helper(csp, solution_found):
        if not csp.unassigned_variables():
            return csp.assignments(), True
        var = csp.extract_unassigned()
        assignments = csp.assignments()
        solution = solution_found
        for val in var.active_domain():
            csp.assign(var, val)
            noDWO = True
            if not CSPUtil.gac_enforce(csp, var):
                noDWO = False
            if noDWO:
                assignments, solution = CSPAlgorithms.gac_helper(csp, solution_found)
            CSPUtil.undo_pruning_for(var)
        return assignments, solution