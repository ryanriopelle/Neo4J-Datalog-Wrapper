from datalog import *

query = [

        # 'Q(y):-test(x,y,_,_), blah(x,b, _)',
        # 'A(a, b , d) :- rel(a, b, c, _), a > 1, GROUP_BY([a, b], d = COUNT(c)), d < 100, SORT_BY(b, "DESC"), f = FUN(d), LIMIT(25), DISTINCT',
        #  "Q1(y, z):-test(x,y,z), blah(x,'some movie',c)",
         "Q2(y):-test(x, y, '20'), blah(x,'some movie',c), y > 10, CONTAINS(y, 'subs')"
         ]

for q in query:
    inspect(q)