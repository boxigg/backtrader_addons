# Copyright (c) 2018 ab-trader

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt


class DrawdownPercents(bt.Observer):
    """Reversed drawdown in %s"""

    lines = ('dd', 'maxdd',)

    plotinfo = dict(plot=True, subplot=True, plotname='Drawdown %')

    plotlines = dict(zero=dict(_plotskip=True,),
                     dd=dict(ls='-', linewidth=1.0, color='red'),
                     maxdd=dict(ls='--', linewidth=1.0, color='black',))


    def __init__(self):

        self._dd = self._owner._addanalyzer_slave(bt.analyzers.DrawDown)


    def next(self):

        self.lines.dd[0] = self._dd.rets.drawdown
        self.lines.maxdd[0] = self._dd.rets.max.drawdown
        self.lines.dd[0] = (-1) * self.lines.dd[0]
        self.lines.maxdd[0] = (-1) * self.lines.maxdd[0]


class DrawdownDollars(bt.Observer):
    """Reversed drawdown in $s"""

    lines = ('dd', 'maxdd',)

    plotinfo = dict(plot=True, subplot=True, plotname='Drawdown $')

    plotlines = dict(zero=dict(_plotskip=True,),
                     dd=dict(ls='-', linewidth=1.0, color='red'),
                     maxdd=dict(ls='--', linewidth=1.0, color='black',))


    def __init__(self):

        self._dd = self._owner._addanalyzer_slave(bt.analyzers.DrawDown)


    def next(self):

        self.lines.dd[0] = self._dd.rets.moneydown
        self.lines.maxdd[0] = self._dd.rets.max.moneydown
        self.lines.dd[0] = (-1) * self.lines.dd[0]
        self.lines.maxdd[0] = (-1) * self.lines.maxdd[0]


class DrawdownLength(bt.Observer):
    """Modified drawdown length"""

    lines = ('L', 'maxL',)

    plotinfo = dict(plot=True, subplot=True, plotname='Drawdown Length')

    plotlines = dict(L=dict(ls='-', linewidth=1.0, color='blue'),
                     maxL=dict(ls='--', linewidth=1.0, color='black',))


    def __init__(self):

        self._dd = self._owner._addanalyzer_slave(bt.analyzers.DrawDown)


    def next(self):

        self.lines.L[0] = self._dd.rets.len
        self.lines.maxL[0] = self._dd.rets.max.len