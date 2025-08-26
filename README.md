# Streamlit Cookies Manager v2

> **Note**: This is a modernized fork of the original [streamlit-cookies-manager](https://github.com/ktosiek/streamlit-cookies-manager) by Tomasz Kontusz. The core functionality and most of the codebase remains his work. This fork updates the package for Streamlit 1.18+ compatibility and modern Python tooling.

## What's New in This Fork

- ✅ **Compatible with Streamlit 1.18+** - Uses `st.cache_data` instead of deprecated `st.cache`
- ✅ **Updated Dependencies** - All dependencies updated to latest stable versions
- ✅ **Modern Build System** - Switched from Poetry to UV (by Astral) for faster dependency management
- ✅ **Python 3.9+ Support** - Tested with Python 3.9, 3.10, 3.11, 3.12, and 3.13
- ✅ **PEP 621 Compliant** - Uses modern `pyproject.toml` format

## Installation

### From PyPI
```bash
pip install streamlit-cookies-manager-v2

# Or using UV
uv pip install streamlit-cookies-manager-v2
```

### From GitHub (Development)
```bash
pip install git+https://github.com/JohnDoeData/streamlit-cookies-manager.git

# Or using UV
uv pip install git+https://github.com/JohnDoeData/streamlit-cookies-manager.git
```

## Usage

Access and change browser cookies from Streamlit scripts:

```python
import os
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="myapp/streamlit-cookies-manager/",
    # You should really setup a long COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    password=os.environ.get("COOKIES_PASSWORD", "My secret password"),
)
if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

st.write("Current cookies:", cookies)
value = st.text_input("New value for a cookie")
if st.button("Change the cookie"):
    cookies['a-cookie'] = value  # This will get saved on next rerun
    if st.button("No really, change it now"):
        cookies.save()  # Force saving the cookies now, without a rerun
```

## Features

### Basic Cookie Manager
```python
from streamlit_cookies_manager import CookieManager

cookies = CookieManager()
if not cookies.ready():
    st.stop()

# Get a cookie
value = cookies.get('cookie_name')

# Set a cookie
cookies['cookie_name'] = 'cookie_value'

# Delete a cookie
del cookies['cookie_name']

# Save immediately (without waiting for rerun)
cookies.save()
```

### Encrypted Cookie Manager
```python
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    password="your_secret_password",
    prefix="myapp/",  # Optional: prefix for all cookies
)

# All operations are the same as CookieManager
# but cookie values are automatically encrypted/decrypted
```

## Requirements

- Python 3.9+
- Streamlit 1.18.0+
- cryptography

## Development

This project uses [UV](https://github.com/astral-sh/uv) for dependency management:

```bash
# Clone the repository
git clone https://github.com/JohnDoeData/streamlit-cookies-manager.git
cd streamlit-cookies-manager

# Create virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .

# Build JavaScript component
cd streamlit_cookies_manager
npm install
npm run build
```

## Changes from Original

1. **Caching Update**: Replaced deprecated `@st.cache` with `@st.cache_data` for Streamlit 1.18+ compatibility
2. **Dependency Updates**: Updated all Python and JavaScript dependencies to latest stable versions
3. **Build System**: Migrated from Poetry to UV for faster, more reliable dependency management
4. **Package Format**: Updated to PEP 621 compliant `pyproject.toml` format
5. **Version**: Continuing from 0.3.1 to show continuity from the original project

## Credits

**Original Author**: [Tomasz Kontusz](https://github.com/ktosiek) - [streamlit-cookies-manager](https://github.com/ktosiek/streamlit-cookies-manager)

**Current Maintainer**: [JohnDoeData](https://github.com/JohnDoeData)

This fork is maintained to ensure compatibility with modern Streamlit versions. The majority of the codebase and functionality was created by the original author.

## License

Apache-2.0 (same as original)