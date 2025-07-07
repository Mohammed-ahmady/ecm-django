# Django Railway Deployment Fix Guide

## Problem Identified

The deployment is failing with `gunicorn: command not found` error because:

1. **Incorrect requirements.txt**: Your current requirements.txt contains many unnecessary packages that are causing conflicts during installation
2. **Missing essential packages**: The file is missing some packages needed for Railway deployment

## Root Cause Analysis

Looking at your GitHub repository, I found that your requirements.txt contains:
- Many unnecessary packages (numpy, pandas, pillow, etc.)
- Conflicting package versions
- Missing or incorrectly specified gunicorn

## The Fix

### Step 1: Replace requirements.txt

Replace your current requirements.txt with this minimal, working version:

```
Django==5.2.3
python-decouple
psycopg2-binary
gunicorn
whitenoise
```

### Step 2: Verify Your Procfile

Make sure your Procfile contains exactly this:
```
web: gunicorn ecm_website.wsgi:application --bind 0.0.0.0:$PORT
```

### Step 3: Check Your settings.py

Ensure your settings.py has these configurations:

```python
import os
from decouple import config
from pathlib import Path

# Database configuration for Railway
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
    }
}

# Static files with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... other middleware
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    BASE_DIR / "ecm_website/static",
]

ALLOWED_HOSTS = ["*"]
```

## Deployment Steps

1. **Update your repository:**
   ```bash
   # Replace requirements.txt with the fixed version
   # Commit and push changes
   git add requirements.txt
   git commit -m "Fix requirements.txt for Railway deployment"
   git push origin main
   ```

2. **Redeploy on Railway:**
   - Go to your Railway dashboard
   - Click on your service
   - Click "Deploy" to trigger a new deployment
   - Or Railway will automatically redeploy when you push changes

3. **Set Environment Variables (if not already set):**
   In Railway dashboard, ensure these variables are set:
   - `PGDATABASE`: `${{Postgres.PGDATABASE}}`
   - `PGUSER`: `${{Postgres.PGUSER}}`
   - `PGPASSWORD`: `${{Postgres.PGPASSWORD}}`
   - `PGHOST`: `${{Postgres.PGHOST}}`
   - `PGPORT`: `${{Postgres.PGPORT}}`
   - `SECRET_KEY`: Your Django secret key

## Why This Fixes the Issue

1. **Simplified dependencies**: Only essential packages are included
2. **Correct gunicorn**: Ensures gunicorn is properly installed
3. **No conflicts**: Removes packages that might cause installation conflicts
4. **Railway optimized**: Specifically configured for Railway's environment

## Expected Result

After applying this fix:
- Build should complete successfully
- Gunicorn should start properly
- Your Django app should be accessible
- Database connections should work

## Verification

Once deployed, check:
1. Build logs show successful installation
2. Application starts without errors
3. Website loads at your Railway URL
4. Database operations work correctly

## Additional Notes

- Keep your requirements.txt minimal - only add packages you actually use
- Test locally before deploying
- Monitor Railway logs for any issues
- Your current database data will be preserved

This fix should resolve the deployment issue and get your Django app running on Railway successfully.

