from __future__ import unicode_literals
import datetime
from ParkingAttendent.models import *
import random

s = db.session

def propogate():
    u1 = User()
    u1.username = 'kprince3'
    u1.name = 'Kory Prince'
    # hash for 'test'
    u1.pwhash = '$6$rounds=60000$vKgdFaIPHGS.b9w5$7aRo6yUa0RHfnYlyll8kRQN.Zb5LoM4fhqgm7iAB4xFs916yR5TgJOSUlpnwGpzYtLsHA60dz6dEwLPTgy7eq.'
    s.add(u1)

    u2 = User()
    u2.username = 'bsmith1'
    u2.name = 'Bob Smith'
    u2.pwhash = '$6$rounds=60000$vKgdFaIPHGS.b9w5$7aRo6yUa0RHfnYlyll8kRQN.Zb5LoM4fhqgm7iAB4xFs916yR5TgJOSUlpnwGpzYtLsHA60dz6dEwLPTgy7eq.'
    s.add(u2)

    l1 = Lot()
    l1.description = 'RBN'
    s.add(l1)

    l2 = Lot()
    l2.description = 'BUS'
    s.add(l2)

    b1 = Badge()
    b1.user = u1
    b1.description = "First Time"
    b1.date = datetime.datetime.now() - datetime.timedelta(days=1)
    s.add(b1)

    c1 = Checkin()
    c1.user = u1
    c1.lot = l1
    c1.score = 3
    c1.date = b1.date
    s.add(c1)

    for x in xrange(0,100):
        c = Checkin()
        c.user = u1
        c.lot = random.choice([l1,l2])
        c.score = random.randint(0,5)
        c.date = datetime.datetime.now() - datetime.timedelta(minutes=random.randint(0,120)) 
        s.add(c)
    
    s.commit()
