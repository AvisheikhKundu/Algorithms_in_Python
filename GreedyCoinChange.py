def GreedyCC(notes,target):
    res = 0
    notes.sort(reverse=True)
    for note in notes:
        if target//note > 0:
            r = target//note
            res += r
            target = target - r*note
    if target == 0:
        return res
    else:
        return "Not Possible"

notes = [50,20,10,5,2]
target = 165
print("Minimum Notes Needed: ", GreedyCC(notes, target))
