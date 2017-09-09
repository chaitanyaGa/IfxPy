# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import IfxPy
import config
from testfunctions import IfxPyTestFunctions

class IfxPyTestCase(unittest.TestCase):

  def test_161_FetchBothNestedSelects_01(self):
    obj = IfxPyTestFunctions()
    obj.assert_expect(self.run_test_161)

  def run_test_161(self):
    conn = IfxPy.connect(config.ConnStr, config.user, config.password)

    server = IfxPy.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'Inf'):
      op = {IfxPy.ATTR_CASE: IfxPy.CASE_UPPER}
      IfxPy.set_option(conn, op, 1)

    result = IfxPy.exec_immediate(conn, "select * from emp_act order by projno desc")
    row = IfxPy.fetch_both(result)
    count = 1
    while ( row ):
      print "Record",count,": %6s  %-6s %3d %9s %10s %10s %6s " % (row[0], row[1], row[2], row['EMPTIME'], row['EMSTDATE'], row['EMENDATE'], row[0])
      
      result2 = IfxPy.exec_immediate(conn,"select * from employee where employee.empno='" + row['EMPNO'] + "'")
      row2 = IfxPy.fetch_both(result2)
      if row2:        
         print ">>%s,%s,%s,%s,%s,%s,%s" % (row2['EMPNO'], row2['FIRSTNME'],row2['MIDINIT'], row2[3], row2[3], row2[5], row2[6])
      count = count + 1
      if (count > 10):
          break
      row = IfxPy.fetch_both(result)
#__END__
#__LUW_EXPECTED__
#Record 1 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 2 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 3 : 000340  OP2013 140      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 4 : 000340  OP2013 170      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 5 : 000330  OP2012 140      0.25 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 6 : 000330  OP2012 160      0.75 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 7 : 000320  OP2011 140      0.75 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 8 : 000320  OP2011 150      0.25 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 9 : 000050  OP2010  10      0.75 1982-01-01 1983-02-01 000050 
#>>000050,JOHN,B,GEYER,GEYER,6789,1949-08-17
#Record 10 : 000100  OP2010  10      1.00 1982-01-01 1983-02-01 000100 
#>>000100,THEODORE,Q,SPENSER,SPENSER,0972,1980-06-19
#__ZOS_EXPECTED__
#Record 1 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 2 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 3 : 000340  OP2013 170      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 4 : 000340  OP2013 140      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 5 : 000330  OP2012 160      0.75 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 6 : 000330  OP2012 140      0.25 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 7 : 000320  OP2011 150      0.25 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 8 : 000320  OP2011 140      0.75 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 9 : 000100  OP2010  10      1.00 1982-01-01 1983-02-01 000100 
#>>000100,THEODORE,Q,SPENSER,SPENSER,0972,1980-06-19
#Record 10 : 000050  OP2010  10      0.75 1982-01-01 1983-02-01 000050 
#>>000050,JOHN,B,GEYER,GEYER,6789,1949-08-17
#__SYSTEMI_EXPECTED__
#Record 1 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 2 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 3 : 000340  OP2013 140      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 4 : 000340  OP2013 170      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 5 : 000330  OP2012 140      0.25 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 6 : 000330  OP2012 160      0.75 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 7 : 000320  OP2011 140      0.75 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 8 : 000320  OP2011 150      0.25 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 9 : 000050  OP2010  10      0.75 1982-01-01 1983-02-01 000050 
#>>000050,JOHN,B,GEYER,GEYER,6789,1949-08-17
#Record 10 : 000100  OP2010  10      1.00 1982-01-01 1983-02-01 000100 
#>>000100,THEODORE,Q,SPENSER,SPENSER,0972,1980-06-19
#__IDS_EXPECTED__
#Record 1 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 2 : 000020  PL2100  30      1.00 1982-01-01 1982-09-15 000020 
#>>000020,MICHAEL,L,THOMPSON,THOMPSON,3476,1973-10-10
#Record 3 : 000340  OP2013 140      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 4 : 000340  OP2013 170      0.50 1982-01-01 1983-02-01 000340 
#>>000340,JASON,R,GOUNOT,GOUNOT,5698,1947-05-05
#Record 5 : 000330  OP2012 140      0.25 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 6 : 000330  OP2012 160      0.75 1982-01-01 1983-02-01 000330 
#>>000330,WING, ,LEE,LEE,2103,1976-02-23
#Record 7 : 000320  OP2011 140      0.75 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 8 : 000320  OP2011 150      0.25 1982-01-01 1983-02-01 000320 
#>>000320,RAMLAL,V,MEHTA,MEHTA,9990,1965-07-07
#Record 9 : 000100  OP2010  10      1.00 1982-01-01 1983-02-01 000100 
#>>000100,THEODORE,Q,SPENSER,SPENSER,0972,1980-06-19
#Record 10 : 000050  OP2010  10      0.75 1982-01-01 1983-02-01 000050 
#>>000050,JOHN,B,GEYER,GEYER,6789,1949-08-17
