# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import json
import uvclight

from grokcore.component import name
from nva.psyquizz import hs

from ..quizz1 import Quizz1
from uvclight.auth import require
from zope.schema import getFieldsInOrder


class Quizz1Charts(uvclight.Page):
    require('manage.company')
    name('charts')
    uvclight.context(Quizz1)

    template = uvclight.get_template('cr1.pt', __file__)

    def jsonify(self, da):
        return json.dumps(da)

    def update(self, stats, general_stats=None):
        hs.need()
        self.stats = stats
        self.general_stats = general_stats

        good = dict(name="Eher Ja", data=[], color="#62B645")
        bad = dict(name="Eher Nein", data=[], color="#D8262B")

        xAxis = []
        percents = {}

        self.descriptions = json.dumps(self.context.__schema__.getTaggedValue('descriptions'))
        self.xAxis_labels = {k.title: k.description for id, k in getFieldsInOrder(self.context.__schema__)}

        for key, answers in self.stats.statistics['raw'].items():
            xAxis.append(key)
            yesses = 0
            noes = 0
            total = 0
            for answer in answers:
                total += 1
                if answer.result is True:
                    yesses += 1
                else:
                    noes +=1 

            good['data'].append(float(yesses)/total * 100)
            bad['data'].append(float(noes)/total * 100)

        self.xAxis = json.dumps(xAxis)
        self.series = json.dumps([good, bad])
