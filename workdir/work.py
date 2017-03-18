import datetime
import random

from hyperopt import hp, fmin, tpe
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

import workdir.classes.config # loads local config
from qml.cv import QCV
from qml.helpers import get_engine
from qml.models import QXgb, QAvg, QRankedAvg, QStackModel, QPostProcessingModel, QRankedByLineAvg
from workdir.classes.models import qm


# results = list([[2014, x] for x in range(1, 14)])
# cv = QCV(qm)
#
#
# for i in range(2000):
#     random.shuffle(results)
#     models = list(results[:random.randint(2, 7)])
#     models = sorted(models, key=lambda x: (x[0], x[1]))
#     print(models)
#
#     model_id = qm.add_by_params(
#         QAvg(models)
#     )
#     print(cv.cross_val(model_id, 1))
#     model_id = qm.add_by_params(
#         QAvg(models, is_geom=True)
#     )
#     print(cv.cross_val(model_id, 1))
#     model_id = qm.add_by_params(
#         QRankedAvg(models)
#     )
#     print(cv.cross_val(model_id, 1))
#     model_id = qm.add_by_params(
#         QRankedByLineAvg(models)
#     )
#     print(cv.cross_val(model_id, 1))



cv = QCV(qm)

def to1(X, res):
    ind1 = X[X['numberOfDaysActuallyPlayed'] >= 14].index.values
    for i in ind1:
        res.set_value(i, 'res', 1)
    return list(res['res'])


qm.add(
    45,
    QPostProcessingModel(
        1001331, -1, to1
    ),
    'days14 to res 1'
)