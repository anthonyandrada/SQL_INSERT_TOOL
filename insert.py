'''
Created on Mar 20, 2017

@author: aandrada92
'''

class InsertTool(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.fileName = fileName
    
    def process(self, tableName):
        with open(self.fileName, 'r') as fi:
            with open("output.txt", 'w') as fo:
                firstLine = fi.readline()
                fieldNames = firstLine.split("\t")
                for line in fi:
                    first = True
                    records = line.split("\t")
                    fo.write("INSERT INTO " + tableName + " (")
                    for field in fieldNames:
                        if first:
                            fo.write(field)
                            first = False
                        else:
                            fo.write(", " + field)
                    fo.write(") VALUES (")
                    first = True         
                    for record in records:
                        if first:
                            if record:
                                r = record.rstrip()
                                if r.isdigit():
                                    fo.write(r)
                                else:
                                    fo.write("'" + r + "'")
                            else:
                                fo.write("NULL")    
                            first = False
                        else:
                            if record:
                                r = record.rstrip()
                                if r.isdigit():
                                    fo.write(", " + r)
                                else:    
                                    fo.write(", '" + r + "'")
                            else:
                                fo.write(", NULL")       
                    fo.write(");\n")    
    
