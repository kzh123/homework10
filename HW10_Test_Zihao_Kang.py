from HW10_Zihao_Kang import Repository
import unittest


class TestRepository(unittest.TestCase):
    def test_HW09(self):
        """test for homework09"""

        self.assertEqual(str(Repository('./', print_pt=False).pt_instructors),
                         str("+-------+-------------+------+---------+----------+\n\
|  CWID |     Name    | Dept |  Course | Students |\n\
+-------+-------------+------+---------+----------+\n\
| 98765 | Einstein, A | SFEN | SSW 567 |    4     |\n\
| 98764 |  Feynman, R | SFEN | SSW 564 |    3     |\n\
| 98764 |  Feynman, R | SFEN | SSW 687 |    3     |\n\
| 98764 |  Feynman, R | SFEN |  CS 501 |    1     |\n\
| 98764 |  Feynman, R | SFEN |  CS 545 |    1     |\n\
| 98763 |  Newton, I  | SFEN | SSW 555 |    1     |\n\
| 98763 |  Newton, I  | SFEN | SSW 689 |    1     |\n\
| 98765 | Einstein, A | SFEN | SSW 540 |    2     |\n\
| 98760 |  Darwin, C  | SYEN | SYS 800 |    1     |\n\
| 98760 |  Darwin, C  | SYEN | SYS 750 |    1     |\n\
| 98760 |  Darwin, C  | SYEN | SYS 611 |    2     |\n\
| 98760 |  Darwin, C  | SYEN | SYS 645 |    1     |\n\
+-------+-------------+------+---------+----------+"))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
