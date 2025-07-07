# Django ECM Website Deployment Guide for Railway

This guide will help you deploy your Django ECM website to Railway with PostgreSQL database support.

## What I've Already Done

I've prepared your Django project for Railway deployment by making the following changes:

### 1. Updated `requirements.txt`
Added the following packages:
- `gunicorn` - WSGI server for production
- `whitenoise` - For serving static files
- `psycopg[binary,pool]` - PostgreSQL adapter for Django

### 2. Modified `settings.py`
- Added `import os` for environment variables
- Updated database configuration to use PostgreSQL via environment variables:
  - `PGDATABASE`
  - `PGUSER`
  - `PGPASSWORD`
  - `PGHOST`
  - `PGPORT`
- Added WhiteNoise middleware for static file serving
- Configured static files for production
- Set `ALLOWED_HOSTS = ["*"]` for Railway deployment

### 3. Created `Procfile`
A process file that tells Railway how to run your Django app:
```
web: gunicorn ecm_website.wsgi:application --bind 0.0.0.0:$PORT
```

### 4. Removed Render-specific files
- Removed `render.yaml` as it's not needed for Railway

## What You Need to Do

### Step 1: Create a GitHub Repository
1. Create a new repository on GitHub
2. Upload your project files to the repository
3. Make sure all the modified files are included

### Step 2: Sign Up for Railway
1. Go to [railway.app](https://railway.app)
2. Sign up for a free account
3. Connect your GitHub account

### Step 3: Deploy Using Railway CLI (Recommended)

#### Install Railway CLI
1. Install the Railway CLI:
   ```bash
   npm install -g @railway/cli
   ```
   Or download from: https://docs.railway.app/develop/cli

2. Login to Railway:
   ```bash
   railway login
   ```

#### Deploy Your Project
1. Navigate to your project directory
2. Initialize Railway project:
   ```bash
   railway init
   ```
3. Add PostgreSQL database:
   ```bash
   railway add
   ```
   Select PostgreSQL when prompted

4. Set environment variables:
   ```bash
   railway variables set PGDATABASE=${{Postgres.PGDATABASE}}
   railway variables set PGUSER=${{Postgres.PGUSER}}
   railway variables set PGPASSWORD=${{Postgres.PGPASSWORD}}
   railway variables set PGHOST=${{Postgres.PGHOST}}
   railway variables set PGPORT=${{Postgres.PGPORT}}
   railway variables set SECRET_KEY=your-secret-key-here
   ```

5. Deploy your app:
   ```bash
   railway up
   ```

### Step 4: Alternative - Deploy via Dashboard

1. **Connect GitHub Repository:**
   - In Railway Dashboard, click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Add PostgreSQL Database:**
   - Click "Add Service"
   - Select "Database" → "PostgreSQL"

3. **Configure Environment Variables:**
   Go to your web service settings and add:
   - `PGDATABASE`: `${{Postgres.PGDATABASE}}`
   - `PGUSER`: `${{Postgres.PGUSER}}`
   - `PGPASSWORD`: `${{Postgres.PGPASSWORD}}`
   - `PGHOST`: `${{Postgres.PGHOST}}`
   - `PGPORT`: `${{Postgres.PGPORT}}`
   - `SECRET_KEY`: Generate a random secret key

4. **Deploy:**
   - Railway will automatically deploy your app
   - Check the deployment logs for any issues

## Important Notes

### Database Migration
Since you mentioned having a local PostgreSQL database, you'll need to:
1. Export your local database data:
   ```bash
   pg_dump -h localhost -U your_username -d your_database > backup.sql
   ```
2. Import it to Railway PostgreSQL database after deployment

### Environment Variables
Create a `.env` file locally with:
```
SECRET_KEY=your-secret-key-here
PGDATABASE=your-local-db-name
PGUSER=your-local-username
PGPASSWORD=your-local-password
PGHOST=localhost
PGPORT=5432
```

### Static Files
The project is configured to serve static files using WhiteNoise, so no additional setup is needed.

## Troubleshooting

### Common Issues:
1. **Build fails**: Check that all dependencies are in `requirements.txt`
2. **Database connection errors**: Verify environment variables are set correctly
3. **Static files not loading**: Ensure `collectstatic` runs successfully
4. **Port binding errors**: Make sure Procfile uses `$PORT` variable

### Logs:
- Check deployment logs in Railway Dashboard
- Use `railway logs` command to view runtime logs

## Cost Information
- Railway free tier includes:
  - $5 credit per month
  - 500 hours of usage
  - PostgreSQL database
  - Custom domains
  - Automatic SSL certificates

Your website will be available at: `https://your-service-name.up.railway.app`

## Next Steps After Deployment
1. Test all functionality
2. Set up custom domain (optional)
3. Configure any additional environment variables
4. Set up monitoring and backups
5. Import your local database data

The deployment should take 5-10 minutes once you start the process.

## Database Import Instructions

After successful deployment, to import your local PostgreSQL data:

1. Get Railway database connection string from dashboard
2. Use pg_restore or psql to import your data:
   ```bash
   psql "your-railway-postgres-connection-string" < backup.sql
   ```

Your Django ECM website will then be fully functional on Railway!

