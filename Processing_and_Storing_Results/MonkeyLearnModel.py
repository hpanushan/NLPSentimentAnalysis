from monkeylearn import MonkeyLearn

class MonkeyLearnModel(object):
    
    def sentimentValue(self, tweet):
        ml = MonkeyLearn('aeafaa0aa014ed56b663c49fa20ac81a68f2d194')
        model_id = 'cl_TWmMTdgQ'
        data = []
        data.append(tweet)
        result = ml.classifiers.classify(model_id, data)
        return result.body[0]['classifications'][0]

obj = MonkeyLearnModel()

print(obj.sentimentValue("downgrade"))