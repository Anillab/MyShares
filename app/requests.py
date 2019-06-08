
import urllib.request,json,time
from .models import *
from . import db
# from .data import get_chart
base_url='https://abacus.co.ke/api/v2/{}'
'''
{
  "SecurityID": "ARM.O0000",
  "high_trade": 3.2,
  "low_trade": 3.2,
  "last_traded_price": 3.35,
  "close": 3.35,
  "previous_close": 3.05,
  "volume": 122700,
  "year_low_price": 2.4,
  "year_high_price": 23,
  "name": "ARM Cement Limited",
  "companyid": "ARM",
  "identifier": "",
  "type": "O",
  "shortname": "ARM Cement"
}
  "company_id": "BAMB",
  "name": "Bamburi Cement Limited",
  "details": "Bamburi Cement Limited is primarily engaged in the manufacture and sale of cement and cement related products. It also owns and manages a world class nature and environmental park developed from rehabilitated quarries. The company was Founded in 1951",
  "logo": "http://abacus.co.ke/wp-content/uploads/2015/05/Bamburi.jpg",
  "location": "Kenya-Re Towers, Upper Hill,",
  "auditors": "Ernst & Young LLP",
 6 "incorporation_date": "1951",
 7 "listing_date": "1970",
 8 "listing_price": "",
  "shares_issued": 362959275,
  "financial_year": "12/31/2016",
  "par_value": 5,
 12 "parent_company": "Lafarge of France",
  "address": "P .O. Box 10921 – 00100 GPO Nairobi, Kenya",
  "website": "http://www.lafarge.co.ke/",
  "dps": 12,
  "eps": 14.44,
  "staff_population": 936,
  "shortname": "Bamburi",
  "short_name": "Bamburi",
  "indices": "ASI, NSE20",
  "sector": "Construction and Allied",
  "beta": -0.21
}
'''

def parsestocks(obj,today):
    for company in obj:
        id=company["companyid"]
        high=company["high_trade"]
        low=company["low_trade"]
        last=company["last_traded_price"]
        prev=company["previous_close"]
        close=company["close"]
        volume=company["volume"]
        yrlow=company["year_low_price"]
        yrhigh=company["year_high_price"]
        saveobject(Stock_Info(
            Company_id=id,
            High_trade=high,
            Low_trade=low,
            Last_traded_price=last,
            Close_price=close,
            Prev_close=prev,
            Vol_traded=volume,
            Year_low_price=yrlow,
            Year_high_price=yrhigh,
            day=today))
    return Stock_Info.query.filter(Stock_Info.day==today).all()

def parsecompanies(obj):
    for comp in obj:
        saveobject(Company(Company_id=comp["company_id"],
        Logo=comp["logo"],
        Name=comp["name"],
        Details=comp["details"],
        Location=comp["location"],
        Auditors=comp["auditors"],
        Incorporation_date=comp["incorporation_date"],
        Listing_Price=comp["listing_price"],
        Shares_Issued=comp["shares_issued"],
        Financial_Year=comp["financial_year"],
        Par_value=comp["par_value"],
        Parent_Company=comp["parent_company"],
        Address=comp["address"],
        Website=comp["website"],
        Indices=comp["indices"],
        Sector=comp["sector"]))
    print(len(obj))

def get_companies():
    url=base_url.format('companies/')
    with urllib.request.urlopen(url) as rsp:
        resp=json.loads(rsp.read())
    return parsecompanies(resp["data"])


def get_todays():
    today=time.strftime('%d-%m-%Y')
    if Stock_Info.query.filter(Stock_Info.day==today).first():
        return Stock_Info.query.filter(Stock_Info.day==today).all()
    url=base_url.format('instruments')
    with urllib.request.urlopen(url) as rsp:
        resp=json.loads(rsp.read())
    return parsestocks(resp["data"],today)
