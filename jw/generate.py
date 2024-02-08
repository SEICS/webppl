import json
# Generate code for Flights 1B dataset (distribution definitions from BayesAQP)
# /Users/jw/Desktop/bayes-aqp/Benchmarks/flights/pgmpyCPD.json
cpds_path = "/Users/jw/Desktop/bayes-aqp/Benchmarks/flights/pgmpyCPD.json"
with open(cpds_path, "r") as cpds_f:
    cpds_json = json.load(cpds_f)
    
# print(f"cpds: {cpds_json}")
# for 