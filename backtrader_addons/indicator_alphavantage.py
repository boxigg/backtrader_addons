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

import backtrader as bt

class Dividends(bt.Indicator):
    """
    Dividend indicator for alphavantage adjusted daily time series data feed
    (AlphavantageCSVData)
    """

    lines = ('value', )

    def __init__(self):

        self.lines.value = self.data.div


class Splits(bt.Indicator):
    """
    Split indicator for alphavantage adjusted daily time series data feed
    (AlphavantageCSVData)
    """

    lines = ('ratio', )

    def __init__(self):

        self.lines.ratio = self.data.split


class SplitAdjustedClose(bt.Indicator):
    """
    Split adjusted close indicator for alphavantage adjusted daily time series data feed
    (AlphavantageCSVData)
    """

    lines = ('adj_close', )

    def __init__(self):

        self.lines.adj_close = self.data.adjclose