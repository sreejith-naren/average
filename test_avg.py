from average import average_num

def testMultiple():
    ret= average_num([4,2,3])
    assert ret== 3

def testemtpy():
    ret= average_num([])
    assert ret== None

     