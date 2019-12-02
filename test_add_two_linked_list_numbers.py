import unittest
from typing import List
from add_two_linked_list_numbers import Solution

class TestSolution(unittest.TestCase):

    
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_addTwoNumbers_when_two_numbers_provided_should_return_sum_in_reverse(self):
        sol = Solution()
        list_node1 = sol.get_linked_list('243')
        list_node2 = sol.get_linked_list('564')
        result_linked_list = sol.addTwoNumbers(list_node1, list_node2)
        result_string = sol.get_num_in_reverse_from_linked_list(result_linked_list)
        self.assertEqual(result_string, '708')

    
if __name__ == '__main__':
    unittest.main()


