## toSQL.py
## toSQL.py puts things into SQL
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
## toSQL.py
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

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship, backref

def build1tomany(Parent,Child,relationshipname,parentid,childid):
    """
    build1tomany = build1tomany(Parent,Child,relationshipname,parentid,childid)
    build1tomany builds a one-to-many relationship between Parent and a Child. 
    A single parent can have many children.

    INPUTS:
    Parent           - this must be a declarative meta, not an instance e.g. Parent
    Child            - this must be a declarative meta, not an instance, e.g. Child
    relationshipname - this is of type string, and it's the relationship name for the Parent,
                       in the Parent, to the Child, e.g. "children"
    parentid         - this is a string, with the attribute that will be the parentid for the 
                       ForeignKey, e.g. "parent.id"
                     - remember in using build1tomany, the Child needs the Parent's table name,
                       not the class name, e.g. "FRBtables.ID", not "FRB.ID"
    childid          - this is a string, with the attribute that will be the childid for the 
                       ForeignKey, e.g. "parent_id"

    EXAMPLE of usage, e.g.:
    class Parent(Base):
     __tablename__ = 'parent'
     id            = Column(Integer, primary_key=True)
     children      = relationship("Child", backref="parent")
     
    class Child(Base):
     __tablename__ = 'child'
     id            = Column(Integer,primary_key=True)
     parent_id     = Column(Integer,ForeignKey('parent.id')
     
    # Parent needs
     - to set the relationship, relationship name, the name of the Child class, 
       not the child's instance, and the backref back to the parent
    """
    
    setattr(Child,childid,Column(String,ForeignKey(parentid)))

    # this is a check of the argument, parentid, because we need to put in a string that is 
    # manually put in, but this string must exactly be from the Parent
    if not (Parent.__tablename__ == parentid.split('.')[0]):
        print "Warning, the parentid argument inputted isn't the same as the Parent table name \n"
        print "Parent table name : " , Parent.__tablename__
        print "parentid argument : " , parentid
    
    parent_relation = relationship(Child.__name__,backref=Parent.__tablename__)
    setattr(Parent,relationshipname,parent_relation)
    return Parent, Child

def Row(clsname,dict,base):
    """
    Row
    Row sets up a row for SQL table
    """
    Row = type(str(clsname),(base,),dict)
    return Row

def PutinSQLAlch(cls,dict):
    """
    PutinSQLAlch = PutinSQLAlch(cls,dict)
    PutinSQLAlch aka Put into SQLAlchemy 
    PutinSQLAlch puts in the dict into the class cls, 
     so to give the values to populate the columns for a row

    EXAMPLE of USAGE, try 

    Tbl = TblinSet( 'Tblrow', Tbldicteg)
    type(Tbl)  # <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>

    Tbl0dic = { 
    'id' : 0 , 'name' : 'Tbl0' , 'desc' : 'Table 0 in Set', 'created' : datetime.utcnow() 
    }
    Tbl1dic = { 
    'id' : 1 , 'name' : 'Tbl1' , 'desc' : 'Table 1 in Set', 'created' : datetime.utcnow() 
    }

    # So it works like this:
    Tbl0 = Tbl()
    Tbl0 = PutinSQLAlch(Tbl0,Tbl0dic)
    Tbl1 = Tbl()
    Tbl1 = PutinSQLAlch(Tbl1,Tbl1dic)
    """

    for key in dict:
        setattr(cls,key,dict[key] )
    return cls

    

