# fastdata

## Overview
`fastdata` is a FastAPI-based interface for accessing data related to financial and commodity markets. Users with a licensed Bloomberg terminal can interact with their data programmatically via a REST API. Regarding commodity-related data, access to European gas storage data is provided via GIE. 

Queries to `fastdata` can be easily performed using the companion client package `fastdata-client`, available separately. It provides a simple Python interface for interacting with the API.

## ⚠️ Disclaimer 
This project is intended for educational purposes only. It is designed to run locally on a machine with a valid Bloomberg Terminal installation. This tool does not redistribute any Bloomberg data and does not bypass any licensing restrictions. Use of this software is still subject to Bloomberg’s licensing terms. The author assumes no responsibility for misuse.


## Planned Improvements
- Add background job handling
    - Integrate Redis, Celery, and Flower to manage and monitor long-running or large Bloomberg queries asynchronously
- Enhance Pydantic models
    - Add stricter type annotations (datetime, Decimal, constr, etc.) for better validation
    - Improve error handling
- Unit tests for routers, models, and dependencies
- Rate-limit sensitive endpoints to prevent abuse
- Improve API documentation
- Create Docker support
- Add caching for repeated queries