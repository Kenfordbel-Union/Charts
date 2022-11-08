import pymongo

mongo = pymongo.MongoClient()
charts_db = mongo["charts"]

spotify_col = charts_db["spotify"]
deezer_col = charts_db["deezer"]
youtube_col = charts_db["youtube"]
general_col = charts_db["general"]
general_list = []
def scrap_data(service, service2, region):
    calc = 0
    calc2 = 0
    for i in service.find():
        for g in service2.find():
            if region+str(calc) in i and region+str(calc) in g:
                sortted = sorted(i[region+str(calc)].split())
                sortted2 = sorted(g[region + str(calc)].split())
                sortted = sortted[-3:]
                sortted2 = sortted2[-3:]
                print(sortted)
                print(sortted2)
                if len(sortted) >= 3:
                    check_case = sortted[0].lower() + sortted[1].lower() + sortted[2].lower()
                    if check_case not in general_list:
                        general_list.append(check_case)
                        general_col.insert_one(i)
                        calc += 1
                        print(sortted)
                    else:
                        calc += 1
                if len(sortted2) >= 3:
                    check_case2 = sortted2[0].lower() + sortted2[1].lower() + sortted2[2].lower()
                    if check_case2 not in general_list:
                        general_list.append(check_case2)
                        general_col.insert_one(g)
                        calc2 += 1
                        print(sortted2)
                    else:
                        calc2 += 1
                if len(sortted) <= 2:
                    check_case = sortted[0].lower() + sortted[1].lower()
                    if check_case not in general_list:
                        general_list.append(check_case)
                        general_col.insert_one(i)
                        calc += 1
                        print(sortted)
                    else:
                        calc += 1
                if len(sortted2) <= 2:
                    check_case2 = sortted2[0].lower() + sortted2[1].lower()
                    if check_case2 not in general_list:
                        general_list.append(check_case2)
                        general_col.insert_one(g)
                        calc2 += 1
                        print(sortted2)
                    else:
                        calc2 += 1
                else:
                    calc += 1
                    calc2 += 1
    print(len(general_list))




scrap_data(spotify_col, deezer_col, "song-")
print("Done")








