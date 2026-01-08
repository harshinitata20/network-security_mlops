# Network Security API Test Script
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print("Health Check:", response.json())
    assert response.status_code == 200

def test_prediction():
    """Test single prediction endpoint"""
    data = {
        "having_IP_Address": -1,
        "URL_Length": 1,
        "Shortining_Service": 1,
        "having_At_Symbol": 1,
        "double_slash_redirecting": -1,
        "Prefix_Suffix": -1,
        "having_Sub_Domain": -1,
        "SSLfinal_State": -1,
        "Domain_registeration_length": -1,
        "Favicon": 1,
        "port": 1,
        "HTTPS_token": -1,
        "Request_URL": 1,
        "URL_of_Anchor": -1,
        "Links_in_tags": 1,
        "SFH": -1,
        "Submitting_to_email": -1,
        "Abnormal_URL": -1,
        "Redirect": 0,
        "on_mouseover": 1,
        "RightClick": 1,
        "popUpWidnow": 1,
        "Iframe": 1,
        "age_of_domain": -1,
        "DNSRecord": -1,
        "web_traffic": -1,
        "Page_Rank": -1,
        "Google_Index": 1,
        "Links_pointing_to_page": 1,
        "Statistical_report": -1
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print("Prediction Result:", response.json())
    assert response.status_code == 200

if __name__ == "__main__":
    print("Testing Network Security API...")
    print("-" * 50)
    
    try:
        test_health_check()
        print("✓ Health check passed")
    except Exception as e:
        print(f"✗ Health check failed: {e}")
    
    try:
        test_prediction()
        print("✓ Prediction test passed")
    except Exception as e:
        print(f"✗ Prediction test failed: {e}")
    
    print("-" * 50)
    print("Testing completed!")
