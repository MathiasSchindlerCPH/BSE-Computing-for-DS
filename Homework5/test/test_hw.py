#!pip install pytest-cov pytest

import unittest

import sys
sys.path.append('../')

from functions import car_at_light, safe_subtract, retrieve_age_eafp, get_day_month_year, compute_distance, sum_general_int_list

from pandas.testing import assert_frame_equal

from datetime import date
import pandas as pd



class TestHW5(unittest.TestCase):
    #1 
    def test_car_at_light_1(self):
        x = 'red'
        output = car_at_light(x)
        expected_output = 'stop'
        assert output == expected_output
        
    def test_car_at_light_2(self):
        x = 'yellow'
        output = car_at_light(x)
        expected_output = 'wait'
        assert output == expected_output
        
    def test_car_at_light_3(self):
        x = 'green'
        output = car_at_light(x)
        expected_output = 'go'
        assert output == expected_output
        
    #2
    def test_safe_subtract_1(self):
        x1 = 5
        x2 = 3
        output = safe_subtract(x1, x2)
        expected_output = 2
        assert output == expected_output
        
        
    def test_safe_subtract_2(self):
        x1 = 10
        x2 = 30
        output = safe_subtract(x1, x2)
        expected_output = -20
        assert output == expected_output
    
    #3
    def test_retrieve_age_eafp():
        x = {'name': 'Meryl', 'last_name': 'Streep', 'birth': 1949}
        output = retrieve_age_eafp(x)
        expected_output = 'Meryl Streep is 72 years old'
        assert output == expected_output
    
    
    def test_retrieve_age_lbyl():
        x = {'name': 'Will', 'last_name': 'Smith', 'birth': 1968}
        output = retrieve_age_lbyl(x)
        expected_output = 'Will Smith is 53 years old'
        assert output == expected_output
        
    #4
    
    
    #5
    
    
    #6
    

    # 7
    def testGetDayMonthYear(self):
        data = [date(1996, 12, 11), date(1992, 2, 1), date(2021, 11, 11)]
        output = pd.DataFrame(map(get_day_month_year, data))
        expected_output = pd.DataFrame({'day':[11,1,11], 'month':[12,2,11], 'year':[1996,1992,2021]}) 
        assert_frame_equal(output, expected_output)

    # 8
    def testComputeDistance(self):
        data = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
        output = list(map(compute_distance, data))
        expected_output = [31.13186522205169, 157.00582786889402]
        self.assertListEqual(output, expected_output)
    
    # 9
    def testSumGeneralIntList(self):
        data = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
        output = sum_general_int_list(data)
        expected_output = 48
        self.assertEqual(output, expected_output)



#list_of_dates = [date(1996, 12, 11), date(1992, 2, 1), date(2021, 11, 11)]

#df_dates = pd.DataFrame(map(get_day_month_year, list_of_dates))
#print(df_dates)


