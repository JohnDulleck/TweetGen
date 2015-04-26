# StringGen.py

import sys
import generator

print "DEBUG: Starting..."
print "Name = '%s'" % __name__
print "dir ( generator ) = ", dir ( generator )

def TweetGen ( inf, outf ) :
    with open ( inf, "r" ) as fi :
        lines = fi.readlines ()

    generatedLines = generator.ProcessLines ( lines )

    with open ( outf, "w" ) as fo :
        fo.writeLines ( generatedLines )

if __name__ == "__main__":
        print "DEBUG: Calling TweetGen..."
        s = "[test, twist, toast]"
        sl = s.split(',')
        print "sl = ", sl
        for idx in range(len(sl)):
            sl[idx] = sl[idx].strip("[]")
        print "sl = ", sl
        # TweetGen ( sys.argv [ 1 ], sys.argv [ 2 ] )
