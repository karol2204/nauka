"""
+ dodawanie
- odejmowanie
* mnożenie
/ dzielenie

() - jak w matematyce kierują kolejnością działania

** potęgowanie
// dzielenie w "dół"
% - modulo (reszta z dzielenia)


"""

VAT = 23
ObliczonyVAT = (1 + VAT / 100)

CenaNettoJava = 930
CenaNettoAjax = 540
CenaNettoCaptureOne = 1530
CenaNettoPhotoshop = 3230
CenaNettoCanon = 12300



CenaBruttoJava = CenaNettoJava * ObliczonyVAT
CenaBruttoAjax = CenaNettoAjax * ObliczonyVAT
CenaBruttoCaptureOne = CenaNettoCaptureOne * ObliczonyVAT
CenaBruttoPhotoshop = CenaNettoPhotoshop * ObliczonyVAT
CenaBruttoCanon = CenaNettoCanon * ObliczonyVAT

