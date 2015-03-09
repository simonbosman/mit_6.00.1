# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    #is frob atMe the last frob in the list
    if atMe.getAfter() == None:
        #is newFrob bigger then frob atMe
        if newFrob.myName() >= atMe.myName():
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
            return
    
    #is frob atMe the first frob in the list
    if atMe.getBefore() == None:
        #is newFrob smaller then frob atMe
        if newFrob.myName() < atMe.myName():
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            return
             
    #is new frob bigger or equel to frob atMe and smaller then the next frob in the list
    if newFrob.myName() >= atMe.myName() and newFrob.myName() < atMe.getAfter().myName():
        newFrob.setBefore(atMe)
        newFrob.setAfter(atMe.getAfter())
        atMe.getAfter().setBefore(newFrob)
        atMe.setAfter(newFrob)
    #move one frob up in the list
    elif newFrob.myName() >= atMe.myName():
        return insert(atMe.getAfter(), newFrob)
    
    #is new frob smaller or equel to frob atMe and bigger then the previous frob in the list
    if newFrob.myName() < atMe.myName() and newFrob.myName() > atMe.getBefore().myName():
        newFrob.setAfter(atMe)
        newFrob.setBefore(atMe.getBefore())
        atMe.getBefore().setAfter(newFrob)
        atMe.setBefore(newFrob)
    #move one frob down in the list
    elif newFrob.myName() < atMe.myName():
        return insert(atMe.getBefore(), newFrob)
 
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())
   

abby = Frob('abby')
xander = Frob('xander')
beto = Frob('beto')
insert(abby, xander)
insert(abby, beto)


print beto.myName()
print beto.getBefore().myName()
print beto.getAfter().myName()
print xander.getBefore().myName()
print findFront(xander).myName()
