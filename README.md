# bbmirror

## Overview
`bbmirror` is a FastAPI-based interface for accessing financial data using the blp Python library (https://pypi.org/project/blp/). It is designed for licensed Bloomberg Terminal users who want to interact with their data programmatically via a REST API.

## ⚠️ Disclaimer 
This project is intended for educational purposes only. It is designed to run locally on a machine with a valid Bloomberg Terminal installation. This tool does not redistribute any Bloomberg data and does not bypass any licensing restrictions. Use of this software is still subject to Bloomberg’s licensing terms. The author assumes no responsibility for misuse.

## Structure of the Project
```
bbmirror/
│── app/                            # Main application folder
│   ├── routers/                    # API route handlers (modular)
│   │   ├── __init__.py             # Makes `routers` a package
│   │   ├── bdh_router.py           # BDH API route
│   │   ├── bdp_router.py           # BDP API route
│   │   ├── bds_router.py           # BDS API route
│   │   ├── bdip_router.py          # BDIP API route
│   │
│   ├── dependencies/               # Shared dependencies
│   │   ├── __init__.py             # Makes `dependencies` a package
│   │   ├── bloomberg.py            # Bloomberg API connection dependency
│   │
│   ├── models/                     # Pydantic models
│   │   ├── __init__.py             # Makes `models` a package
│   │   ├── bdh_model.py            # BDH request models
│   │   ├── bdp_model.py            # BDP request models
│   │   ├── bds_model.py            # BDS request models
│   │   ├── bdip_model.py           # BDIP request models
│   │
│   ├── main.py                     # Entry point for FastAPI
│
│── tests/                          # Unit, integration, and other tests
│   ├── test.ipynb                  # Blp package-related tests in Jupyter
│
│── requirements.txt                # Python dependencies
│── README.md                       # Documentation
│── .gitignore                      # Ignore unnecessary files
```

Breakdown of the structure:
- routers/ → Contains separate routers for different API endpoints (e.g., bdh_router.py, bdp_router.py).
- dependencies/ → Stores shared dependency functions like bbconnect() (bloomberg.py file).
- models/ → Stores pydantic models for API request validation (helps keep routers/ clean).
- tests/ → Unit tests, integration, and other tests.
- main.py → Only responsible for initializing FastAPI & registering routers.

