from interval import *
from scale import *
import random
import math
from alphabeta import friendly_alpha_beta_search

def checkContrary(cf1, cf2, counter1, counter2):
    """
    Checks if the notes in the cantus firmus and counterpoint move in contrary motion
    @param cf1:str the base note of the cantus firmus
    @param cf2:str the note of the cantus firmus moved into
    @param counter1:str the base note of the counterpoint
    @param counter2:str the note of the counterpoint moved into
    @return True if the motion was in opposite directions
    """
    cfup = isFirstNoteHigher(cf1, cf2)
    counterup = isFirstNoteHigher(counter1, counter2)
    return (cfup and not counterup) or (not cfup and counterup) # xor


# Checks the rules of first species counterpoint, requires cf and counter to have the same length
# @param cf:list<str> the cantus firmus, a list of notes
# @param counter:list<str> the counterpoint, a list of notes
# @return (boolean, list<str) True if all of the rules are followed, incidents
#   where the rules are broken
def checkFirstSpeciesRules(cf, counter):
    errors = []
    verticalIntervals = []

    # check for crossing
    for i in range(len(cf)):
        if not isFirstNoteHigher(counter[i], cf[i]):
            errors.append("Crossing over of notes into CF at position " + str(i))

    # fill out the vertical intervals
    for i in range(len(cf)):
        verticalInterval = findInterval(cf[i], counter[i])
        verticalIntervals.append(verticalInterval)
        if verticalInterval in ["P4", "A4", "d5"] or verticalInterval[1] in ["2", "7"]:
            errors.append("Vertical Interval of " + verticalInterval + " between " + cf[i] + " and " + counter[i] + " at position " + str(i))

    # fill out the horizontal intervals
    for i in range(len(counter)-1):
        horizontalInterval = findInterval(counter[i], counter[i+1])
        if horizontalInterval in ["A4", "d5"] or horizontalInterval[1] == "7":
            errors.append("Horizontal Interval of " + horizontalInterval + " between " + counter[i] + " and " + counter[i+1] + " at position " + str(i))

    # check for direct/parallel intervals
    for i in range(len(counter)-1):
        contrary = checkContrary(cf[i], cf[i+1], counter[i], counter[i+1])
        if not contrary and ((verticalIntervals[i] == "P5" and verticalIntervals[i+1] == "P5") or 
        (verticalIntervals[i] == "P8" and verticalIntervals[i+1] == "P8") or 
        (verticalIntervals[i] == "P1" and verticalIntervals[i+1] == "P1")):
            errors.append("Parallel " + verticalIntervals[i+1][1] + "th at position " + str(i+1))
        elif not contrary and verticalIntervals[i+1] in ["P5", "P8"]:
            errors.append("Direct " + verticalIntervals[i+1][1] + "th at position " + str(i+1))

    # check start
    if not verticalIntervals[0] in ["M3", "P1", "P5", "P8"]:
        errors.append("Incorrect start of a " + verticalIntervals[0] + " at position 0")

    # check end
    if not verticalIntervals[len(verticalIntervals)-1] in ["P1", "P8"]:
        errors.append("Incorrect ending of a " + verticalIntervals[len(verticalIntervals)-1] + " at position " + str(len(counter)-1))

    correct = len(errors) == 0
    return correct, errors


class CounterpointSolver(object):

    def __init__(self, cf, species=1, cp=None):
        """
        @param cf:list<str> the cantus firmus, a list of notes
        """
        self.cf = cf
        self.species = species

        if cp is None:
            # cp stands for counterpoint
            self.cp = []
        else:
            self.cp = cp

    def next_possible_moves(self):
        """
        Gets all of the next possible moves that can be made for the next note
        """
        # gets the possibilities to be the first note
        if len(self.cp) == 0:
            return self._first_note_moves()

        # gets the possibilities to be the last note
        elif len(self.cp) == len(self.cf) - 1:
            return self._last_note_moves()

        # gets all intermediate notes
        else:
            previous_note = self.cp[-1]
            match_note = self.cf[len(self.cp)]
            return self._note_step(previous_note, match_note)

    def _first_note_moves(self):
        """
        @return list of all possible notes to be the first note
        """
        pass

    def _last_note_moves(self):
        """
        @return list of all possible notes to be the final note
        """
        pass

    def _note_step(self, previous_note, match_note):
        """
        @param previous_note the last note that was matched
        """
        pass

    def is_complete(self):
        """
        @return True if the counterpoint is complete
        """
        # TODO make generic to work for every species
        return len(self.cp) == len(self.cf)

    def get_counterpoint(self):
        """
        @return copy of the notes in the counterpoint
        """
        return [i for i in self.cp]

    def get_cantus_firmus(self):
        """
        @return copy of the notes in the cantus firmus
        """
        return [i for i in self.cf]
        
    def evaluate(self):
        """
        Gives a score to determine how good the counterpoint is
        """
        return 5 + len(checkFirstSpeciesRules(self.cf, self.cp)[1])

    def choose_next_note(self, note):
        """
        TODO make work for more than just first species
        @return new CounterpointSolver with the move made
        """
        new_cp = self.get_counterpoint()
        new_cp.append([note])

        return CounterpointSolver(self.cf, self.species, new_cp)


if __name__ == '__main__':
    cf = ["C2", "D2", "E2", "A2", "F2", "E2", "F2", "D2", "D2", "C2"]

    solver = CounterpointSolver(cf)

    done = friendly_alpha_beta_search(solver, )












