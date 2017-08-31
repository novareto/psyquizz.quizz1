# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight
import tempfile

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import (SimpleDocTemplate, Spacer)
from tempfile import NamedTemporaryFile
from reportlab.lib.units import cm
from svglib.svglib import svg2rlg

from .quizz1 import IQuizz1
from nva.psyquizz.browser.reports import GeneratePDF


class PDFPL(GeneratePDF):
    uvclight.context(IQuizz1)
    uvclight.name('pdf')
    uvclight.auth.require('zope.Public')

    def headerfooter(self, canvas, doc):
        canvas.setFont("Helvetica", 9)
        canvas.drawString(1 * cm, 2 * cm, u"Gemeinsam zu gesunden Arbeitsbedingungen")
        canvas.drawString(1 * cm, 1.6 * cm, u"Psychische Belastungen online erfassen")
        canvas.drawString(1 * cm, 1.2 * cm, u"Ein Programm der BG ETEM")
        canvas.drawString(18 * cm, 2 * cm, u"Grundlage der Befragung:  Prüfliste Psychische")
        canvas.drawString(18 * cm, 1.6 *cm, u"Belastung")
        canvas.drawString(18 * cm, 1.2 * cm, u"Unfallversicherung Bund und Bahn")
        canvas.line(0.5 * cm , 2.5 * cm, 26 * cm, 2.5 * cm)
        canvas.setFont("Helvetica", 12)
        canvas.drawString(1 * cm, 20 * cm, self.context.course.company.name)
        canvas.drawString(1 * cm, 19.5 * cm, self.context.course.title)
        try:
            canvas.drawString(1 * cm, 19.0 * cm, u"Befragungszeitraum %s - %s" % (
                self.context.startdate.strftime('%d.%m.%Y'),
                self.context.enddate.strftime('%d.%m.%Y')))
        except:
            print "ERROR"
        canvas.line(0.5 * cm , 18.5 * cm, 26 * cm, 18.5 * cm)

    def render(self):
        doc = SimpleDocTemplate(
            NamedTemporaryFile(), pagesize=landscape(letter))
        parts = []
        pSVG = self.request.form.get('pSVG1')
        tf = tempfile.NamedTemporaryFile()
        tf.write(unicode(pSVG).encode('utf-8'))
        tf.seek(0)
        drawing = svg2rlg(tf.name)
        drawing.width = 900.0
        drawing.renderScale = 0.55
        ## Page1
        parts.append(Spacer(0, 2*cm))
        self.frontpage(parts)
        parts.append(Spacer(0, 0.4*cm))
        parts.append(drawing)
        doc.build(parts, onFirstPage=self.headerfooter, onLaterPages=self.headerfooter)
        pdf = doc.filename
        pdf.seek(0)
        return pdf.read()
