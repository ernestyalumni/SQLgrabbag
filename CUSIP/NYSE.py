## NYSE.py
## NYSE.py has the "fields" for the SQL database, the columns
## 
################################################################################################
## Copyleft 2015, Ernest Yeung <ernestyalumni@gmail.com>                             
##                                                                        
## 20150730   
##                                                                                       
## This program, along with all its code, is free software; you can redistribute it and/or modify  
## it under the terms of the GNU General Public License as published by                         
## the Free Software Foundation; either version 2 of the License, or            
## (at your option) any later version.                                                           
##   
## This program is distributed in the hope that it will be useful,                             
## but WITHOUT ANY WARRANTY; without even the implied warranty of                           
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                              
## GNU General Public License for more details.                                           
##                                                                                        
## You can have received a copy of the GNU General Public License                           
## along with this program; if not, write to the Free Software Foundation, Inc.,           
## S1 Franklin Street, Fifth Floor, Boston, MA                                            
## 02110-1301, USA                                                                        
##                                                                                           
## Governing the ethics of using this program, I default to the Caltech Honor Code:          
## ``No member of the Caltech community shall take unfair advantage of                     
## any other member of the Caltech community.''                                          
##                                                                                          
## Please donate (and help fund Science!) at 
## ernestyalumni.tilt.com                                    
##                                                                                            
## Facebook     : ernestyalumni                                                               
## linkedin     : ernestyalumni                                                            
## Tilt/Open    : ernestyalumni                                                            
## twitter      : ernestyalumni                                                            
## youtube      : ernestyalumni          
## wordpress    : ernestyalumni                                                                 
##  
################################################################################################  
## NYSE.py
## 
## We've always defined ourselves by the ability to overcome the impossible. And we count these 
## moments, these moments when we dared to aim higher, to break barriers, to reach for the stars, 
## to make the unknown known. We count these moments as our proudest achievements, 
## but we've lost all that.
## And perhaps we've just forgotten that we are still pioneers, and we've barely begun, and 
## our greatest accomplishments cannot be behind us, but our destiny lies above us. 
## -Interstellar (2014)
##
## This code is open-source, and
## Use of code is governed by the Caltech Honor Code: 
## ``No member of the Caltech community shall take unfair advantage of 
## any other member of the Caltech community.'' 
##
################################################################################################

import sqlalchemy
from sqlalchemy import Column, String, Date, DateTime

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from toSQL import build1tomany, Row, PutinSQLAlch


Base = declarative_base()

########################################
## ICB Industry Classification Benchmark
########################################
# We can "hardware" the form of the tables for ICB, since it's relatively set in stone and 
# agreed upon as a global standard, with this classification:
########################################
## Industry
## Supersector
## Sector
## Subsector
########################################

IndustryColumndict    = { 
    '__tablename__' : 'Industry',
    'CODE'          : Column('CODE', String, primary_key=True),
    'Name'          : Column('Name', String),
    'Updated'       : Column('Updated', DateTime, default=datetime.utcnow()),
    'NYSEcode'      : Column('NYSEcode',String)
    }

Industryinfo = { 
    'Industry_CODE'     : 'CODE' , 
    'Industry_CODE_str' : IndustryColumndict['__tablename__'] + '.CODE' 
    }

SuperSectorColumndict = { 
    '__tablename__' : 'SuperSector',
    'CODE'          : Column('CODE', String, primary_key=True),
    'Name'          : Column('Name',String),
    'Updated'       : Column('Updated', DateTime, default=datetime.utcnow()),
    'NYSEcode'      : Column('NYSEcode',String)
    }

SuperSectorinfo = {
    'SuperSector_CODE'     : 'CODE',
    'SuperSector_CODE_str' : SuperSectorColumndict['__tablename__'] + '.CODE' 
    }

SectorColumndict = {
    '__tablename__' : 'Sector',
    'CODE'          : Column('CODE', String, primary_key=True),
    'Name'          : Column('Name',String),
    'Updated'       : Column('Updated', DateTime, default=datetime.utcnow()),
    'NYSEcode'      : Column('NYSEcode',String)
    }

Sectorinfo = {
    'Sector_CODE'     : 'CODE',
    'Sector_CODE_str' : SectorColumndict['__tablename__'] + '.CODE' 
    }

SubSectorColumndict = {
    '__tablename__' : 'SubSector',
    'CODE'          : Column('CODE', String, primary_key=True),
    'Name'          : Column('Name',String),
    'Updated'       : Column('Updated', DateTime, default=datetime.utcnow()),
    'NYSEcode'      : Column('NYSEcode',String)
    }

SubSectorinfo = { 
    'SubSector_CODE' : 'CODE', 
    'SubSector_CODE_str' : SubSectorColumndict['__tablename__'] + '.CODE' 
    }


ICBactionColumndict = {
    '__tablename__' : 'ICBaction',
    'SYMBOL'        : Column('SYMBOL',String, primary_key=True),
    'Name'          : Column('Name',String),
    'Market'        : Column('Market',String),
    'Updated'       : Column('Updated',DateTime,default=datetime.utcnow())
    }

ICBactioninfo = { 
    'ICBaction_SYMBOL' : 'SYMBOL' , 
    'ICBaction_SYMBOL_str' : ICBactionColumndict['__tablename__'] + '.SYMBOL' 
    }


def ICBrepr(self):
    return "<ICB Classification(CODE='%s', Name='%s', Updated='%s', NYSEcode='%s'>" % (self.CODE, self.Name, self.Updated, self.NYSEcode)

def ICBactionrepr(self):
    return "<ICB Classification(SYMBOL='%s', Name='%s', Market='%s', SubSector CODE='%s'>" % (self.SYMBOL, (self.Name).encode('ascii','ignore'), self.Market, self.toSubSector)


IndustryDS    = Row("IndustryDS",    IndustryColumndict, Base)
setattr( IndustryDS, '__repr__' , ICBrepr )

SuperSectorDS = Row("SuperSectorDS", SuperSectorColumndict, Base)
setattr( SuperSectorDS, '__repr__' , ICBrepr )

SectorDS      = Row("SectorDS",      SectorColumndict, Base)
setattr( SectorDS, '__repr__' , ICBrepr )

SubSectorDS   = Row("SubSectorDS",   SubSectorColumndict, Base)
setattr( SubSectorDS, '__repr__' , ICBrepr )

ICBactionDS   = Row("ICBactionDS",     ICBactionColumndict, Base)
setattr( ICBactionDS, '__repr__', ICBactionrepr )


# remember in using build1tomany, the Child needs the Parent's table name, not the class name
IndustryDS, SuperSectorDS = build1tomany( 
    IndustryDS, SuperSectorDS, "toSuperSector", "Industry.CODE", "toIndustry" ) 
SuperSectorDS, SectorDS   = build1tomany( 
    SuperSectorDS, SectorDS, "toSector", "SuperSector.CODE", "toSuperSector" )
SectorDS, SubSectorDS     = build1tomany( 
    SectorDS, SubSectorDS, "toSubSector", "Sector.CODE", "toSector" )
SubSectorDS, ICBactionDS    = build1tomany( 
    SubSectorDS, ICBactionDS, "toICBaction", "SubSector.CODE", "toSubSector" )

ICBSQLdictkeys        = ['Name', 'CODE', 'NYSEcode' ]
ICBSQLdictkeys_Sup    = ['Name', 'CODE', 'toIndustry', 'NYSEcode' ]
ICBSQLdictkeys_S      = ['Name', 'CODE', 'toSuperSector', 'NYSEcode' ]
ICBSQLdictkeys_Sub    = ['Name', 'CODE', 'toSector', 'NYSEcode' ]
ICBSQLdictkeys_action = ['Name', 'SYMBOL', 'Market', 'toSubSector' ]

def ICBpytoSQL(ICBInd, ICBSQLdictkeys, SQLDS ):
    SQLrows = []
    for row in ICBInd:
        SQLDSinst = SQLDS()
        SQLrow = PutinSQLAlch(SQLDSinst, dict(zip(ICBSQLdictkeys, row)))
        SQLrows.append(SQLrow)
    return SQLrows
