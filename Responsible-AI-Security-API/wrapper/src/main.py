'''
MIT license https://opensource.org/licenses/MIT
Copyright 2024 Infosys Ltd
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

"""
app: Project Management service 
fileName: main.py
description: Project management services helps to create Usecase and projects .
             This app handles the services for usecase module which perform CRUD operaions.
"""
from typing import List

import uvicorn
import os
from app.config.logger import CustomLogger
from app.config.config import read_config_yaml
from app.service.service import Bulk
from fastapi import Depends, FastAPI,  Request, Response
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.routing.routers import attack,bulk
from fastapi.middleware.cors import CORSMiddleware

from aicloudlibs.utils.global_exception import UnSupportedMediaTypeException
from aicloudlibs.utils import global_exception_handler
from starlette.middleware.base import BaseHTTPMiddleware
from dotenv import load_dotenv

load_dotenv()
origins =os.getenv("ALLOW_ORIGINS")

log=CustomLogger()

## initialize the app with openapi and docs url
#app = FastAPI(openapi_url="/api/v1/ai/openapi.json", docs_url="/api/v1/ai/docs")
app = FastAPI(**read_config_yaml('../config/metadata.yaml'))
"""

    Adding the CORS Middleware which handles the requests from different origins

    allow_origins - A list of origins that should be permitted to make cross-origin requests.
                    using ['*'] to allow any origin
    allow_methods - A list of HTTP methods that should be allowed for cross-origin requests.
                    using ['*'] to allow all standard method
    allow_headers - A list of HTTP request headers that should be supported for cross-origin requests. 
                    using ['*'] to allow all headers
"""
class CacheControlMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "private, no-store"
        return response
 
class XSSProtectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Security-Policy'] = "default-src 'self'; img-src data: https:; object-src 'none'; script-src https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js 'self' 'unsafe-inline';style-src https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css 'self' 'unsafe-inline'; upgrade-insecure-requests;"
        return response
    
app.add_middleware(CacheControlMiddleware)
#app.add_middleware(XSSProtectionMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_methods=["POST","DELETE"],
    allow_headers=[origins]
)

class ContentTypeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
       
        # X-Content-Type-Options: nosniff
        response.headers['X-Content-Type-Options'] = 'nosniff'
       
        # Verify Content-Type header and set defaults
        content_type = response.headers.get('Content-Type', 'application/octet-stream')
       
        if content_type == 'application/octet-stream':
            response.headers['Content-Type'] = 'application/octet-stream'
            response.headers['Content-Disposition'] = 'attachment; filename=default'
 
        if 'charset=' not in content_type:
            response.headers['Content-Type'] = f"{content_type}; charset=utf-8"
       
        return response
app.add_middleware(ContentTypeMiddleware)

"""
FAST API raise RequestValidationError in case request contains invalid data.
A global exception handler function to handle the requests which contains the invalid data

"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return  global_exception_handler.validation_error_handler(exc)


"""
A global exception handler function to handle the unsupported media type exception
"""
@app.exception_handler(UnSupportedMediaTypeException)
async def unsupported_mediatype_error_handler(request: Request, exc: UnSupportedMediaTypeException):
    return  global_exception_handler.unsupported_mediatype_error_handler(exc)



"""
A global exception handler function to handle the http exception
"""
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
     return  global_exception_handler.http_exception_handler(exc)



"""
incude the routing details of service
"""
app.include_router(attack,tags=["Attack"])
app.include_router(bulk,tags=["Bulk Vulneribility Assessment"])

if __name__ == "__main__":
    
    Bulk.loadApi()
    uvicorn.run("main:app", host="0.0.0.0", port=80)
