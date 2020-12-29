#! /usr/bin/env python
# coding: utf-8
#

"""TBATS1 Model: Trend, Seasonal (one), and Box Cox"""

from tbats import TBATS

from base import BaseModel

class TBATS1_Model(BaseModel):
    """TBATS1 Model Class"""

    def __init__(self):
        raise NotImplementedError

    def dataframe(self):
        raise NotImplementedError

    def train(self):
        bat = TBATS(
            seasonal_periods=[seasons],
            use_arma_errors=False,
            use_box_cox=True,
            use_trend=True,
        )
        self.model = bat.fit(train)

    def forecast(self):
        self.forecast = model.forecast(forecast_len)