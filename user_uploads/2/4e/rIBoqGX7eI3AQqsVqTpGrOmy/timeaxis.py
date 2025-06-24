#!/usr/bin/env python3

import os
import glob
import numpy as np
import xarray as xr

path = '/glade/scratch/geostrat/archive/b.e21.BW.f09_g17.SSP245-TSMLT-GAUSS-DEFAULT.005/atm/hist/'

files = sorted(glob.glob(path+'*h0*'))

days = [0,31,59,90,120,151,181,212,243,273,304,334,365]

n = 0
for year in range(0,421):

   for month in range(1,13):

      print(year)
      print(month)
      print(files[n])

      ds = xr.open_dataset(files[n], decode_times=False)

      print(ds['time'])
      print(ds['time_bnds'])

      base_day = days[month]
      bnd_day = [days[month-1],days[month]]
      
      ds['time'] = ds['time'] - ds['time'] + base_day + year*365
      ds['time_bnds'] = ds['time_bnds'] - ds['time_bnds'] + bnd_day + year*365

      ds['time'].attrs['units'] = "days since 2035-01-01 00:00:00"

      print(ds['time'])
      print(ds['time_bnds'])

      ds['time'].to_netcdf(files[n],format="NETCDF3_64BIT",mode='a')
      ds['time_bnds'].to_netcdf(files[n],format="NETCDF3_64BIT",mode='a')

      n = n + 1

