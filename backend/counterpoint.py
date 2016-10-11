from interval import *
from scale import *
import random
import math
import time

counter = 0

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
def checkFirstSpeciesRules(cf, cp):
    """
    TODO make this an actual scoring mechanism
    """
    errors = []
    vertical_intervals = []

    # TODO get rid of hacky quick fix
    counter = [x[0] for x in cp]

    # check for crossing
    for i in range(len(cf)):
        if not isFirstNoteHigher(counter[i], cf[i]):
            errors.append("Crossing over of notes into CF at position " + str(i))

    # fill out the vertical intervals
    for i in range(len(cf)):
        vertical_interval = findInterval(cf[i], counter[i])
        vertical_intervals.append(vertical_interval)
        if vertical_interval in ["P4", "A4", "d5"] or vertical_interval[1] in ["2", "7"]:
            errors.append("Vertical Interval of " + vertical_interval + " between " + cf[i] + " and " + counter[i] + " at position " + str(i))

    # fill out the horizontal intervals
    for i in range(len(counter)-1):
        horizontalInterval = findInterval(counter[i], counter[i+1])
        if horizontalInterval in ["A4", "d5"] or horizontalInterval[1] == "7":
            errors.append("Horizontal Interval of " + horizontalInterval + " between " + counter[i] + " and " + counter[i+1] + " at position " + str(i))

    # check for direct/parallel intervals
    for i in range(len(counter)-1):
        contrary = checkContrary(cf[i], cf[i+1], counter[i], counter[i+1])
        if not contrary and ((vertical_intervals[i] == "P5" and vertical_intervals[i+1] == "P5") or 
        (vertical_intervals[i] == "P8" and vertical_intervals[i+1] == "P8") or 
        (vertical_intervals[i] == "P1" and vertical_intervals[i+1] == "P1")):
            errors.append("Parallel " + vertical_intervals[i+1][1] + "th at position " + str(i+1))
        elif not contrary and vertical_intervals[i+1] in ["P5", "P8"]:
            errors.append("Direct " + vertical_intervals[i+1][1] + "th at position " + str(i+1))

    # check start
    if not vertical_intervals[0] in ["M3", "P1", "P5", "P8"]:
        errors.append("Incorrect start of a " + vertical_intervals[0] + " at position 0")

    # check end
    if not vertical_intervals[len(vertical_intervals)-1] in ["P1", "P8"]:
        errors.append("Incorrect ending of a " + vertical_intervals[len(vertical_intervals)-1] + " at position " + str(len(counter)-1))

    correct = len(errors) == 0
    return correct, errors


class CounterpointState(object):

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

        # TODO actually find scale a legit way
        tonic = cf[-1]
        # put it up an octave
        tonic = tonic[:-1] + str(int(tonic[-1]) + 1)
        self.scale = majorScale(tonic)

    def next_possible_notes(self):
        """
        Gets all of the next possible moves that can be made for the next note
        """
        # gets the possibilities to be the first note
        if len(self.cp) == 0:
            possible = self._get_first_note_choices()

        # gets the possibilities to be the last note
        elif len(self.cp) == len(self.cf) - 1:
            possible = self._get_last_note_choices()

        # gets all intermediate notes
        else:
            previous_note = self.cp[-1][0]
            match_note = self.cf[len(self.cp)]
            possible = self._get_next_note_choices(previous_note, match_note)
        # scramble possible notes in order to get different solutions on different runs
        # TODO scramble
        return possible

    def _get_first_note_choices(self):
        """
        @return list of all possible notes to be the first note
        """
        possible = []
        for note in self.scale:
            vertical_interval = findInterval(self.cf[0], note)

            if vertical_interval in ["M3", "P1", "P5", "P8"]:
                possible.append(note)
        return possible

    def _get_last_note_choices(self):
        """
        @return list of all possible notes to be the final note
        """
        possible = []
        for note in self.scale:
            vertical_interval = findInterval(self.cf[-1], note)

            if vertical_interval in ["P1", "P8"]:
                possible.append(note)
        return possible

    def _get_next_note_choices(self, previous_note, match_note):
        """
        @param previous_note the last note that was matched
        """
        # TODO make work for every species
        possible = []
        for note in self.scale:
            vertical_interval = findInterval(self.cf[-1], note)
            previous_interval = findInterval(previous_note, note)

            if vertical_interval in ["P1", "m3", "M3", "P5", "m6", "M6", "P8"] and previous_interval not in ["P1", 'A4', "d5"]:
                possible.append(note)
        return possible

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
        if not self.is_complete():
            return -10
        return 5 - len(checkFirstSpeciesRules(self.cf, self.cp)[1])

    def choose_next_note(self, note):
        """
        TODO make work for more than just first species
        @return new CounterpointState with the move made
        """
        new_cp = self.get_counterpoint()
        new_cp.append([note])

        return CounterpointState(self.cf, self.species, new_cp)


class CounterPointSolver(object):

    def __init__(self, cf, species=1):
        self.base_state = CounterpointState(cf, species)

        self.final_state = None

    def _friendly_alpha_beta_search(self, threshold=50):
        """
        Helper function that runs a friendly version of Alpha-Beta Search
        where the two people are "collaborating".
        """
        starting_score = 0
        solution = self._helper(self.base_state, starting_score, threshold)
        print "Final Score:", solution[0]
        self.final_state = solution[1]

    def _helper(self, state, score, threshold):
        """
        Alpha-Beta helper function: Return the minimax value of a particular state

        TODO multi-threading to speed up answer
        """
        global counter
        counter += 1
        if state.is_complete():
            return (state.evaluate(), state)

        action = (score, None)

        for note in state.next_possible_notes():
            new_state = state.choose_next_note(note)
            next_val = self._helper(new_state, score, threshold)
            if next_val[0] > score:
                score = next_val[0]
                action = next_val
                if score > threshold:
                    return action

        return action

    def get_solution(self):
        """
        @return a solution to the cantus firmus
        """
        if self.final_state is None:
            self._friendly_alpha_beta_search()

        return self.final_state.get_counterpoint()


if __name__ == '__main__':
    cf = ["C2", "D2", "E2", "A2", "F2", "E2", "F2", "D2", "D2", "C2"]

    start = time.time()

    solver = CounterPointSolver(cf)

    print cf
    print solver.get_solution()

    print "Explored", counter, "paths!"

    print "Took", time.time() - start, "seconds!"










