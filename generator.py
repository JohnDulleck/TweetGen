# generator.py

from exceptions import Exception

# Error class definition

class StringGenError ( Exception ) : pass
    
StatusOK = True
StatusFail = False

# Process all lines, expand them, and return a list of expanded lines
def ProcessLines ( lines ) :
    exandedLines = []
    
    for line in lines :
        expandedLines += ExpandLine ( line )

    return expandedLines

# Expand a line with word groups into a list of lines with all
# word group permutations
def ExpandLine ( line ) :
    wordGroups = GetWordGroups ( line )
            

# Return a list of word group lists
# and plain (unlisted) text.
# For now, groups must not be nested		
def GetWordGroups(inputString):
    retList = []
    workString = inputString
    lenString = len(workString)
    currLoc = 0
    endLoc = lenString
    while currLoc < endLoc:
        openBracLoc = workString.find('[')
        closeBracLoc = workString.find(']')
        print "open = %d,  close = %d" % (openBracLoc, closeBracLoc)

    if closeBracLoc < openBracLoc:
        raise StringGenError("Close before open")
        
    return retList
    
    
if __name__ == "__main__" :
    Lines =	"This is a [ test, tust, terse ] test"
            
        
    print GetWordGroups ( Lines )
                
    
