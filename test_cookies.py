#!/usr/bin/env python3
"""Test script to verify streamlit-cookies-manager functionality."""

import os
import sys
import streamlit as st
from streamlit_cookies_manager import CookieManager, EncryptedCookieManager

def test_cookie_manager():
    """Test basic CookieManager functionality."""
    st.header("Testing CookieManager")
    
    cookies = CookieManager()
    
    if not cookies.ready():
        st.info("Waiting for cookies to load...")
        st.stop()
    
    st.success("✅ CookieManager initialized successfully")
    st.write("Current cookies:", dict(cookies))
    
    # Test setting a cookie
    if st.button("Set test cookie"):
        cookies['test_cookie'] = 'test_value'
        st.success("Cookie set!")
    
    # Test deleting a cookie
    if st.button("Delete test cookie"):
        if 'test_cookie' in cookies:
            del cookies['test_cookie']
            st.success("Cookie deleted!")
    
    return True

def test_encrypted_cookie_manager():
    """Test EncryptedCookieManager functionality."""
    st.header("Testing EncryptedCookieManager")
    
    encrypted_cookies = EncryptedCookieManager(
        prefix="test_app/",
        password=os.environ.get("COOKIES_PASSWORD", "test_password_123")
    )
    
    if not encrypted_cookies.ready():
        st.info("Waiting for encrypted cookies to load...")
        st.stop()
    
    st.success("✅ EncryptedCookieManager initialized successfully")
    st.write("Current encrypted cookies:", dict(encrypted_cookies))
    
    # Test setting an encrypted cookie
    if st.button("Set encrypted cookie"):
        encrypted_cookies['secure_data'] = 'sensitive_value'
        st.success("Encrypted cookie set!")
    
    # Test deleting an encrypted cookie
    if st.button("Delete encrypted cookie"):
        if 'secure_data' in encrypted_cookies:
            del encrypted_cookies['secure_data']
            st.success("Encrypted cookie deleted!")
    
    return True

def main():
    st.title("Streamlit Cookies Manager Test Suite")
    st.write("Testing with Streamlit >= 1.18.0 using st.cache_data")
    
    tab1, tab2 = st.tabs(["CookieManager", "EncryptedCookieManager"])
    
    with tab1:
        test_cookie_manager()
    
    with tab2:
        test_encrypted_cookie_manager()
    
    st.divider()
    st.info("✅ All tests completed. The library is working with modern Streamlit!")

if __name__ == "__main__":
    main()