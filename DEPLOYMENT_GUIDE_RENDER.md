# Django ECM Website Deployment Guide for Render.com

This guide will help you deploy your Django ECM website to Render.com for free with PostgreSQL database support.

## What I've Already Done

I've prepared your Django project for deployment by making the following changes:

### 1. Updated `requirements.txt`
Added the following packages:
- `dj-database-url` - For PostgreSQL database configuration
- `gunicorn` - WSGI server for production
- `uvicorn` - ASGI server
- `whitenoise[brotli]` - For serving static files

### 2. Modified `settings.py`
- Added imports for `dj_database_url` and `os`
- Updated database configuration to use PostgreSQL via `DATABASE_URL` environment variable
- Added WhiteNoise middleware for static file serving
- Configured static files for production

### 3. Created `build.sh`
A build script that:
- Installs dependencies
- Collects static files
- Runs database migrations

### 4. Created `render.yaml`
A blueprint file that defines:
- PostgreSQL database configuration
- Web service configuration
- Environment variables

## What You Need to Do

### Step 1: Create a GitHub Repository
1. Create a new repository on GitHub
2. Upload your project files to the repository
3. Make sure all the modified files are included

### Step 2: Sign Up for Render.com
1. Go to [render.com](https://render.com)
2. Sign up for a free account
3. Connect your GitHub account

### Step 3: Deploy Using Blueprint (Recommended)
1. In the Render Dashboard, go to the "Blueprints" page
2. Click "New Blueprint Instance"
3. Select your GitHub repository
4. Click "Connect"
5. Give your blueprint project a name (e.g., "ECM Website")
6. Click "Apply"

### Step 4: Alternative Manual Deployment
If you prefer manual setup:

1. **Create PostgreSQL Database:**
   - In Render Dashboard, create a new PostgreSQL database
   - Name it "ecmdb"
   - Copy the internal database URL

2. **Create Web Service:**
   - Create a new Web Service
   - Connect to your GitHub repository
   - Set Language to "Python 3"
   - Build Command: `./build.sh`
   - Start Command: `python -m gunicorn ecm_website.wsgi:application -k uvicorn.workers.UvicornWorker`

3. **Set Environment Variables:**
   - `DATABASE_URL`: Your PostgreSQL internal database URL
   - `SECRET_KEY`: Generate a random secret key
   - `WEB_CONCURRENCY`: 4

## Important Notes

### Database Migration
Since you mentioned having a local PostgreSQL database, you'll need to:
1. Export your local database data
2. Import it to the Render PostgreSQL database after deployment

### Environment Variables
Create a `.env` file locally with:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-local-postgres-url
```

### Static Files
The project is configured to serve static files using WhiteNoise, so no additional setup is needed.

## Troubleshooting

### Common Issues:
1. **Build fails**: Check that all dependencies are in `requirements.txt`
2. **Database connection errors**: Verify `DATABASE_URL` environment variable
3. **Static files not loading**: Ensure `collectstatic` runs successfully

### Logs:
- Check build logs in Render Dashboard
- Check runtime logs for any errors

## Cost Information
- Render.com free tier includes:
  - 750 hours/month for web services
  - PostgreSQL database with 1GB storage
  - Automatic SSL certificates
  - Custom domains (optional)

Your website will be available at: `https://your-service-name.onrender.com`

## Next Steps After Deployment
1. Test all functionality
2. Set up custom domain (optional)
3. Configure any additional environment variables
4. Set up monitoring and backups

The deployment should take 5-10 minutes once you start the process.

