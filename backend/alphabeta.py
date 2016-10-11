def friendly_alpha_beta_search(solver, threshold=50):
    score = 0
    return helper(solver, score, threshold)

def helper(solver, score, threshold):
    """
    Alpha-Beta helper function: Return the minimax value of a particular board,
    given a particular depth to estimate to
    """
    if solver.is_complete():
        return (solver.evaluate(), solver)

    action = (score, None)

    for move in solver.next_possible_moves:
        new_solver = solver.choose_next_note(move)
        next_val = helper(new_solver, score, threshold)
        if next_val[0] > score:
            score = val[0]
            action = next_val
            if score > threshold:
                return action
    return action