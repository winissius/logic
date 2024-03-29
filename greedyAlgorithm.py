states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # set don't accept duplications

stations = {}
stations["k1"] = set(["id", "nv", "ut"])
stations["k2"] = set(["wa", "id", "mt"])
stations["k3"] = set(["or", "nv", "ca"])
stations["k4"] = set(["nv", "ut"])
stations["k5"] = set(["ca", "az"])
final_stations = set()

best_station = None

states_to_cover = states.copy()
while states_to_cover:
    best_station = None
    covered_states = set()
    for station, states_by_stations in stations.items():
        covered = states_to_cover & states_by_stations # intersection
        if len(covered) > len(covered_states):
            best_station = station
            covered_states = covered
        if best_station != None:  final_stations.add(best_station)
        states_to_cover -= covered_states

print(final_stations)