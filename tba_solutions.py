import tbapy

api_key = "6qOZ9uAEsb4CDrOBNG6ZnIdi9cWBaZ6DHnCSato97Qfo7bBeUwT9NfFt4Gi5sHFN"

tba = tbapy.TBA(api_key)
print("Loaded secret solutions successfully")

def where_is(team_name):
    return tba.team(team_name)['city']

def which_events(team, year):
    res = []
    for event in tba.team_events(team, year):
        res.append(event['short_name'])
    return res

def attendance_count(team):
    res = {}
    for event in tba.team_events(team):
        name = event['name']
        if name not in res:
            res[name] = 0
        res[name] += 1
    return res

def winning_alliances(team):
    res = []
    for award in tba.team_awards(team):
        if award['award_type'] == 1:
            res.append([x['team_key'] for x in award['recipient_list']])
    return res

def co_win_count(team):
    res = {}
    for alliance in winning_alliances(team):
        for team in alliance:
            if team not in res:
                res[team] = 0
            res[team] += 1
    return res
