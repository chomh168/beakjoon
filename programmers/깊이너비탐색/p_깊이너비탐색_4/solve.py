tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	#["ICN", "JFK", "HND", "IAD"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	#["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]

result = []
def solve(tickets):
    tickets.sort(key=lambda x:[x[0],x[1]])
    subResult = []
    dfs(tickets,subResult,"ICN")


def dfs(tickets,subResult,check):
    subResult.append(check)
    if len(tickets) == 0:
        global result
        result.append(subResult)
        return

    itr = False
    for each in tickets:
        if check == each[0]:
            itr = True
            newTickets = tickets.copy()
            newTickets.remove(each)
            dfs(newTickets,subResult.copy(),each[1])
    if itr == False:
        return

def solution(tickets):
    solve(tickets)
    return result[0]

print(solution(tickets))