# Flask API Deployment with CI/CD

Basic Flask API deployment with PostgreSQL database hosted on Render, featuring automated CI/CD pipeline using GitHub Actions.

## Features

- PostgreSQL database hosted on Render
- Environment variable configuration
- Swagger UI documentation
- GitHub Actions CI/CD pipeline
- Automatic deployment to Render

## Installation

```
pip install -r requirements.txt
```

## Environment Variables

Create `.env` file with:
DATABASE_URL=your_postgresql_url
SECRET_KEY=your_secret_key

## Deployment

- Hosted on Render: https://se-api-dep.onrender.com
- Swagger UI: https://se-api-dep.onrender.com/swagger

## CI/CD

- GitHub Actions workflow runs tests
- Automatic deployment to Render on successful test completion
