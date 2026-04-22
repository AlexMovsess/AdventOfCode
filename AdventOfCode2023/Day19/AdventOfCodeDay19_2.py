# --- Part Two ---

# Even with your help, the sorting process still isn't fast enough.
# One of the Elves comes up with a new plan: rather than sort parts individually through all of these workflows, maybe you can figure out in advance which combinations of ratings will be accepted or rejected.
# Each of the four ratings (x, m, a, s) can have an integer value ranging from a minimum of 1 to a maximum of 4000. Of all possible distinct combinations of ratings, your job is to figure out which ones will be accepted.
# In the above example, there are 167409079868000 distinct combinations of ratings that will be accepted.
# Consider only your list of workflows; the list of part ratings that the Elves wanted you to sort is no longer relevant. How many distinct combinations of ratings will be accepted by the Elves' workflows?

import os
import re
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay19.txt"))

conditionStr, _ = f.read().split("\n\n")
conditionDict = {}
for line in conditionStr.split("\n"):
    for name, conditions in re.findall(r"(\w+)\{(.+)\}", line):
        conditionDict[name] = conditions.split(",")

resultDict = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
# C'est le dictionnaire de base, avec toutes les combinaisons possibles.
# Il va être envoyé dans splitDictByRule avec la règle d'entrée, soit 'in'.
# Il sera alors divisé en plusieurs dictionnaires selon les différents cas.
# ex :  rule = [x<216:vcd,gmx]
# A chaque condition, le dictionnaire d'entrée est divisé en deux si nécessaire :
# splitDict = {'x':[1,215],'m':[1,4000],'a':[1,4000],'s':[1,4000]} est envoyé dans la condition vcd
# myDict = {'x':[216,4000],'m':[1,4000],'a':[1,4000],'s':[1,4000]} est envoyé dans la condition gmx


def splitDictByRule(myDict, rule, count):
    # Divise le dictionnaire en plusieurs sous-dictionnaires selon les conditions dans rule.
    for condition in rule[0:-1]:
        splitDict = copy.deepcopy(
            myDict
        )  # Immportant ! Sinon, les deux dictionnaires pointent vers la même entité.
        [(conditionName, operator, conditionValue, transition)] = re.findall(
            r"(\w{1})(.)(\d+)\:(\w+)", condition
        )
        if operator == ">" and myDict[conditionName][1] > int(conditionValue):
            splitDict[conditionName][0] = int(conditionValue) + 1
            myDict[conditionName][1] = int(conditionValue)
        elif operator == "<" and myDict[conditionName][0] < int(conditionValue):
            splitDict[conditionName][1] = int(conditionValue) - 1
            myDict[conditionName][0] = int(conditionValue)
        if transition == "A":
            count += countCombinationInDict(splitDict)
        elif transition == "R":
            pass
        else:
            count += splitDictByRule(
                splitDict, conditionDict[transition], 0
            )  # Rien de tel qu'une bonne récurence
    if rule[-1] == "A":
        count += countCombinationInDict(myDict)
    elif rule[-1] == "R":
        pass
    else:
        count += splitDictByRule(myDict, conditionDict[rule[-1]], 0)
    return count


def countCombinationInDict(myDict):
    combinationValue = 1
    for item in myDict.values():
        combinationValue *= item[1] - item[0] + 1
    return combinationValue


print("----- Total :", splitDictByRule(resultDict, conditionDict["in"], 0), "-----")
