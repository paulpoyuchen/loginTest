import sys
from login_test import loginTest

def test_case_1():
    print "test_case_1"
    user = "testing@test.com"
    password = "wrong"
    
    assert (loginTest(user, password) == '{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}' or
           loginTest(user, password) == 'error":{"details":null,"message":"Invalid Username or Password","type":"invalid_grant"}}')

def test_case_2():
    print "test_case_2"
    user = "testing@test.com"
    password = "stillwrong"

    assert (loginTest(user, password) == '{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}' or
           loginTest(user, password) == 'error":{"details":null,"message":"Invalid Username or Password","type":"invalid_grant"}}')

def test_case_3():
    print "test_case_3 (correct password)"
    user = "testing@test.com"
    password = "correct"

    assert (loginTest(user, password) != '{"error":{"message":"Invalid Username or Password","type":"invalid_grant"}}' or
           loginTest(user, password) != 'error":{"details":null,"message":"Invalid Username or Password","type":"invalid_grant"}}')
