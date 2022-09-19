
import Main
import unittest
 
class TestMain(unittest.Testcase):
 
   def test_addition(self):
       self.assertEqual (Main.addition(1, 2), 3,"Should be 3")
       self.assertEqual (Main.addition(5, 5), 10,"Should be 10")
       self.assertEqual (Main.addition(40, 20), 60, "Should be 60")
       self.assertEqual (Main.addition(-3, 2), -1,"Should be -1")
 
 
if __name__ ==  ' __main__ ':
 
    unittest.main()