import unittest

import main

class TestMain(unittest.TestCase):

    ### find_day unit Testing
    def test_find_day(self):
        date = '05-06-2021'
        result = main.find_day(date)
        self.assertEqual(result, "Saturday")
    
    def test_find_day_2(self):
        date = '05-27-2021'
        result = main.find_day(date)
        self.assertEqual(result, None)
    
    ### get_time unit Testing
    def test_get_time(self):
        time = "05:20"
        result = main.get_time(time)
        self.assertEqual(result, (5, 20))
    
    def test_get_time_2(self):
        time = "85:20"
        result = main.get_time(time)
        self.assertEqual(result, None)

    def test_get_time_3(self):
        time = "09:740"
        result = main.get_time(time)
        self.assertEqual(result, None)

    # Check plate unittest
    def test_check_plate(self):
        plate = 'AAA0123'
        result = main.check_plate(plate)
        self.assertEqual(result, 3)

    def test_check_plate_2(self):
        plate = 'AAA01'
        result = main.check_plate(plate)
        self.assertEqual(result, 0)
    
    def test_check_plate_3(self):
        plate = 'AAA012j'
        result = main.check_plate(plate)
        self.assertEqual(result, None)
    
    #_is_pico_y_placa_activated unittest
    def test_is_pico_y_placa_activated(self):
        hour = 9
        minutes = 31
        result = main._is_pico_y_placa_activated(hour, minutes)
        self.assertEqual(result, False)
    
    def test_is_pico_y_placa_activated_2(self):
        hour = 7
        minutes = 20
        result = main._is_pico_y_placa_activated(hour, minutes)
        self.assertEqual(result, True)
    
    def test_is_pico_y_placa_activated_3(self):
        hour = 23
        minutes = 59
        result = main._is_pico_y_placa_activated(hour, minutes)
        self.assertEqual(result, False)

    def test_is_pico_y_placa_activated_4(self):
        hour = 16
        minutes = 1
        result = main._is_pico_y_placa_activated(hour, minutes)
        self.assertEqual(result, True)
    


unittest.main()