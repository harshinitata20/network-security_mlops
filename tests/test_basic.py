import sys
import pytest
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

def test_exception():
    """Test custom exception"""
    try:
        raise NetworkSecurityException("Test exception", sys)
    except NetworkSecurityException as e:
        assert "Test exception" in str(e)

def test_logging():
    """Test logging functionality"""
    logging.info("Test log message")
    assert True
