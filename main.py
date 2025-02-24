from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template App",  # The title of the API (appears in OpenAPI docs).
    description="A simple FastAPI template app.",  # Description of the API.
    version="0.1.0",  # Version of the API.
    terms_of_service="https://example.com/terms/",  # Link to the terms of service.
    contact={
        "name": "Your Name",
        "url": "https://yourwebsite.com",
        "email": "your.email@example.com",
    },  # Contact details for the API maintainers.
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },  # License details.
    docs_url="/docs",  # URL path for the Swagger UI documentation (default: "/docs").
    redoc_url="/redoc",  # URL path for the ReDoc documentation (default: "/redoc").
    openapi_url="/openapi.json",  # URL path to the OpenAPI schema JSON file.
)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Template App"}