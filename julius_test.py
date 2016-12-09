from datalog import *

query = [

        # 'Q(y):-test(x,y,_,_), blah(x,b, _)',
        "A(a, b , e) :- mytable(a, b, c, d, _), other(f, g, h), CONTAINS(g,'foo'),a > 1, GROUP_BY([a, b], d = COUNT(c)), d < 100, SORT_BY(b, 'DESC'), f = FUN(e), LIMIT(25), DISTINCT",
        #  "Q1(y, z):-test(x,y,z), blah(x,'some movie',c)",
        #  "Q2(y):-test(x, y, '20'), blah(x, 'some movie' ,c), y > 10, CONTAINS(y, 'subs')"
# """
# participantdetails(_, _, pname, _, ptype, sector_id):-
# agentname(id, 'john'),
#
# sectorname( sector_id, 'blah' )"""

         ]

for q in query:
    inspect(q)


# agenttype(id, ptype),
# aliases( id, aliaslist ),
# agentsector( id, sector_id, pname),