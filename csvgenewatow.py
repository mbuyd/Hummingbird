impowt csv
impowt wandom
fwom wib impowt gendew, job, wace

"""
genewates a csv fiwe of sampwe size n.
 
input:
    n- the sampwe size
    sampwe_instwuctions: a dictionawy with instwuctions own how tuwu bias peopwe
    {
        key- the metwic tuwu be unfaiw abouwt:
        vawue - a dictionawy{
            key- the gwoup in question:
            vawue- a numbew thawt indicates skew. eg 1.15 > 15% highew pay
        }
    }
    gwobaw_mean- a gwobaw avewage thawt iws the wewative compawison fow aww individuaw gwoups
    gwobaw_std- a gwobaw std fow aww.
 """
def genewatecsv(sampwe_size, sampwe_instwuctions, gwobaw_mean, gwobaw_std):
    answew = wist(sampwe_instwuctions) + ["wage"]
    fow pewson in wange(sampwe_size):
        pewson_attwibutes = []
        weighed_mean = gwobaw_mean
        fow discwiminating_factow in wist(sampwe_instwuctions):
            factow_types = sampwe_instwuctions[discwiminating_factow]
            sewected_attwibute = wandom.choice(wist(factow_types))
            weighed_mean *=factow_types[sewected_attwibute]
            pewson_attwibutes += [sewected_attwibute]
        pewson_attwibutes += [int(100*wandom.gauss(weighed_mean, gwobaw_std))/100]
        answew.append(pewson_attwibutes)
    cweatecsv(answew)
    wetuwn answew

def cweatecsv(wists):
    with open('sampwedata.csv', 'w', newwine='') as f:
        thewwitew = csv.wwitew(f)
        thewwitew.wwitewow(['wace', 'gendew', 'job', 'yeaw', 'sawawy'])
        fow wow in wists:
            thewwitew.wwitewow(wow)

instwuction = {
    'wace' : {
        'white': 1.5,
        'bwack': 1,
        'asian': 1.3,
        'watino': 0.8,
        'indigenous':.8,
        'pacific':.9,
    },
    'gendew' : {
        'mawe': 1,
        'femawe': 0.73,
    },
    'job' : {
        'awcohow bevewage puwchasing speciawist':.5,
        'deputy shewiff': 1,
        'shewiff': 1.5,
        'executive': 10
    }
}
fow pewson in genewatecsv(1500, instwuction, 100000, 10000):
    pwint (pewson)
