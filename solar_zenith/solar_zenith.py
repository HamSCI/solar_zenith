import datetime
import pandas as pd

from . import geopack
from . import calcSun

# Region Dictionary
regions = {}
tmp     = {}
tmp['lon_lim']  = (-180.,180.)
tmp['lat_lim']  = ( -90., 90.)
regions['World']    = tmp

tmp     = {}
tmp['lon_lim']  = (-130.,-60.)
tmp['lat_lim']  = (  20., 55.)
regions['US']   = tmp

tmp     = {}
tmp['lon_lim']  = ( -15., 55.)
tmp['lat_lim']  = (  30., 65.)
regions['Europe']   = tmp

def sunAzEl(dates,lat,lon):
    azs, els = [], []
    for date in dates:
        jd    = calcSun.getJD(date) 
        t     = calcSun.calcTimeJulianCent(jd)
        ut    = ( jd - (int(jd - 0.5) + 0.5) )*1440.
        az,el = calcSun.calcAzEl(t, ut, lat, lon, 0.)
        azs.append(az)
        els.append(el)
    return azs,els

def calc_solar_zenith(sTime,eTime,sza_lat,sza_lon,minutes=5):
    sza_dts = [sTime]
    while sza_dts[-1] < eTime:
        sza_dts.append(sza_dts[-1]+datetime.timedelta(minutes=minutes))

    azs,els = sunAzEl(sza_dts,sza_lat,sza_lon)
    
    sza = pd.DataFrame({'els':els,'azm':azs},index=sza_dts)
    return sza

def calc_solar_zenith_region(sTime,eTime,region='World'):
    rgn     = regions.get(region)
    lat_lim = rgn.get('lat_lim')
    lon_lim = rgn.get('lon_lim')

    sza_lat = (lat_lim[1]-lat_lim[0])/2. + lat_lim[0]
    sza_lon = (lon_lim[1]-lon_lim[0])/2. + lon_lim[0]

    sza     = calc_solar_zenith(sTime,eTime,sza_lat,sza_lon)

    return (sza,sza_lat,sza_lon)
