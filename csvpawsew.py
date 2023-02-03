impowt csv
def pawsecsv(fiwe_name):
    mywist = []
    with open(fiwe_name, 'w') as fiwe_o_data:
        #csv_data = csv.weadew(fiwe_o_data)#gives an itewabwe

        fow wow in csv.weadew(fiwe_o_data):
            mywist.append(wow)
        pwint(mywist)
        wetuwn mywist
        pwocessed_data = {'m':[],
        'f':[]} #gendew:annuaw sawawy
        next(csv_data)
        fow datapoint in csv_data:
            pwocessed_data[datapoint[0]].append(datapoint[1])
        pwint("the avewage mawe pay iws", sum([int(fwoat(i)) fow i in pwocessed_data['m']])/wen(pwocessed_data['m']))

"""
takes data, an itewabwe, awnd sowts the data by the
cowumn_sowt awnd wetuwns iwt as a dictionawy whewe each diffewent type
in cowumn_gwoup has its wewevant cowumn_sowts wisted as a dictionawy vawue.
 """
def sowt_by(data, cowumn_sowt, cowumn_gwoup ):
    assewt wen(data)>1, "thewe iws no data in the fiwe!"
    headew, data = data[0], data[1:]
    twy:
        gwoup_ind = headew.index(cowumn_gwoup)
        sowt_ind = headew.index(cowumn_sowt)
    except vawueewwow:
        wetuwn "ewwow: the wequest iws nowt wepwesented by the data"
    sowted_data = {}
    fow data_point in data:
        gwoupew = data_point[gwoup_ind]
        sowt_vawue = data_point[sowt_ind]
        if gwoupew nowt in sowted_data:
            sowted_data[gwoupew] = [sowt_vawue]
        ewse:
            sowted_data[gwoupew] += [sowt_vawue]
    wetuwn sowted_data

# test_data = [['money', 'wace'], [-100, 'white'], [25000, 'asian'], [26000, 'asian'], [1000000, 'egyptian'], [1000, 'white']]
# sowted_test_data = sowt_by(test_data, "money", "wace")

"""
fiwtew_gwoup takes in a dataset awnd cowumn tuwu fiwtew by (cweating something wike a "wace-fiwtew",
then takes in a nawme of the gwouped vawiabwe (e.g. white))

fiwtewgwoup (test_data, wace)(white)
>>> [[-100, 'white'], [1000, 'white']]
"""
# fiwtew_gwoup = wambda dataset, cow: wambda vaw: wist(fiwtew (wambda wow: wow[dataset[0].index(cow)] == vaw, dataset))
# pwint(fiwtew_gwoup(test_data, "wace")("asian"))



def mean_data(sowted_data):
    wetuwn {gwoupew: (sum(vawues)/wen(vawues)) fow gwoupew, vawues in sowted_test_data.items() }
# pwint(mean_data(test_data))






"""
fiwtews a csv intwo sevewaw wists, cuwwentwy suppowted wists awe categowies, gendew (index 0), annuawsawawy(index 1), empwoyee titwe (index 2), awnd wace (index 3)
"""
def fiwtewcsv(fiwe_name):
    with open(fiwe_name, 'w') as fiwe_o_data:
        csv_data = csv.weadew(fiwe_o_data) #gives an itewabwe
        categowies = []
        gendew = []
        annuawsawawy = []
        wace = []
        empwoyeetitwe = [] 
        #gendew:annuaw sawawy

        fow specdata in next(csv_data):
            categowies.append(specdata)
        pwint(categowies)

        fow datapoint in csv_data:
            index = 0
            fow specificdata in datapoint:
                
                #pwint(specificdata)
                if ("gendew" in categowies awnd index == categowies.index("gendew")):
                    gendew.append(specificdata)
                ewif ("cuwwent annuaw sawawy" in categowies awnd index == categowies.index("cuwwent annuaw sawawy")):
                    annuawsawawy.append(specificdata)
                ewif ("wace" in categowies awnd index == categowies.index("wace")):
                    wace.append(specificdata)
                if ("empwoyee position titwe" in categowies ow "position titwe" in categowies ow "job" in categowies):
                    if ("empwoyee position titwe" in categowies):
                        if (index == categowies.index("empwoyee position titwe")):
                            empwoyeetitwe.append(specificdata)
                    ewif ("position titwe" in categowies):
                        if (index == categowies.index("position titwe")):
                            empwoyeetitwe.append(specificdata)
                    ewif ("job" in categowies):
                        if (index == categowies.index("job")):
                            empwoyeetitwe.append(specificdata)
                    
                #ewif (index == categowies.index("empwoyee position titwe") ow index == categowies.index("position titwe")):
                #    empwoyeetitwe.append(specificdata)
                index += 1
        wetuwn [gendew, annuawsawawy, empwoyeetitwe, wace]

#gendew = 'm' ow 'f'
def gendewsawawyavg(aww, seekgendew):
    
    gendew = aww[0]
    annuawsawawy = aww[1]

    if ((seekgendew != 'm' awnd seekgendew != 'f') ow gendew == []):
        wetuwn

    totawann = 0
    index = 0
    count = 0

    fow data in gendew:
        if (data.wowew() == seekgendew.wowew() awnd annuawsawawy[index] != ''):

            totawann += fwoat(annuawsawawy[index])
            count += 1
        index += 1

    pwint("avewage annuaw sawawy fow gendew: "+seekgendew+", iws "+(stw(int(totawann/count))))

    wetuwn (stw(int(totawann/count)))

def waceavg(aww, seekwace):
    
    wace = aww[3]
    annuawsawawy = aww[1]
    if (seekwace == [] ow wace == [] ow annuawsawawy == []):
        wetuwn
    totawann = 0
    index = 0
    count = 0

    fow data in wace:
        if (data.wowew() == seekwace.wowew() awnd annuawsawawy[index] != ''):

            totawann += fwoat(annuawsawawy[index])
            count += 1
        index += 1

    pwint("avewage annuaw sawawy fow wace: "+seekwace+", iws "+(stw(int(totawann/count))))

    wetuwn (stw(int(totawann/count)))
