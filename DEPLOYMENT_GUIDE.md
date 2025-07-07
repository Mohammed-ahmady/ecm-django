# ECM Django Application - Deployment Guide

## Overview
The ECM (European Center for Magirus) Django application is a fully functional car parts store website for Magirus truck spare parts. This guide provides instructions for deploying and running the application.

## Application Features
- **Home Page**: Professional landing page with hero section, statistics, and featured parts
- **Parts Catalog**: Searchable and filterable parts inventory with pagination
- **Part Details**: Individual part pages with specifications and pricing
- **Inquiry System**: Contact form for customer inquiries and quotes
- **Admin Interface**: Django admin for managing parts, categories, and inquiries
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS

## Prerequisites
- Python 3.11+
- Django 5.2.3
- SQLite (for development) or PostgreSQL (for production)
- Node.js (for Tailwind CSS, optional)

## Installation Instructions

### 1. Extract and Setup
```bash
# Extract the application files
unzip ECM.zip
cd ECM

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DATABASE_NAME=ecm_db
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 3. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Load sample data (optional)
python manage.py shell
# Then run the sample data creation script
```

### 4. Static Files
The application uses Tailwind CSS via CDN for styling. No additional build steps required for basic functionality.

### 5. Run Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```

## Application Structure

### Models
- **Category**: Product categories (Engine Parts, Brake System, etc.)
- **TruckModel**: Compatible truck models (Deutz-Magirus, Iveco Magirus)
- **Part**: Individual parts with specifications, pricing, and relationships
- **Inquiry**: Customer inquiry form submissions

### Views
- **Home**: Landing page with featured parts
- **PartListView**: Searchable parts catalog with filters
- **PartDetailView**: Individual part details
- **InquiryCreateView**: Customer inquiry form

### Templates
- **base.html**: Main template with navigation and footer
- **home.html**: Landing page
- **parts/part_list.html**: Parts catalog
- **parts/part_detail.html**: Part details
- **inquiry.html**: Contact form

## Admin Interface
Access the admin interface at `/admin/` using the superuser credentials:
- Manage parts, categories, and truck models
- View and respond to customer inquiries
- Upload part images
- Control part availability and pricing

## Sample Data
The application includes sample data:
- 3 categories (Engine Parts, Brake System, Transmission)
- 2 truck models (Deutz-Magirus, Iveco Magirus)
- 3 sample parts with relationships

## Configuration Notes

### Database
- Currently configured for SQLite (development)
- For production, update settings.py to use PostgreSQL
- Media files are configured for local storage

### Static Files
- Tailwind CSS loaded via CDN
- Custom color scheme: ECM Primary (#1f2937), ECM Accent (#f97316)
- Font Awesome icons and Google Fonts included

### Security
- DEBUG=True for development (change for production)
- ALLOWED_HOSTS=['*'] for development (restrict for production)
- CSRF protection enabled
- SQL injection protection via Django ORM

## Production Deployment Recommendations

### 1. Environment Variables
- Set DEBUG=False
- Configure proper SECRET_KEY
- Restrict ALLOWED_HOSTS
- Set up database credentials

### 2. Database
- Use PostgreSQL for production
- Configure database backups
- Set up connection pooling

### 3. Static Files
- Configure static file serving (nginx/Apache)
- Set up media file storage (AWS S3/local storage)
- Enable GZIP compression

### 4. Security
- Configure HTTPS
- Set up proper firewall rules
- Enable security headers
- Configure logging

### 5. Performance
- Set up caching (Redis/Memcached)
- Configure database indexing
- Enable query optimization
- Set up monitoring

## Troubleshooting

### Common Issues
1. **URL Reverse Errors**: Ensure URL patterns match template references
2. **Static Files Not Loading**: Check STATIC_URL and STATICFILES_DIRS
3. **Database Errors**: Verify database configuration and migrations
4. **Form Submission Issues**: Check CSRF token and form validation

### Logs
- Django logs available in console output
- Check for 404/500 errors in browser network tab
- Admin interface provides error details

## Support and Maintenance

### Regular Tasks
- Update part inventory via admin interface
- Monitor customer inquiries
- Backup database regularly
- Update dependencies as needed

### Customization
- Modify templates for branding changes
- Add new part categories via admin
- Extend models for additional features
- Customize email notifications

## Contact Information
For technical support or questions about the application, refer to the admin interface or modify the contact information in the templates.

---

**Application Status**: ✅ Fully Functional
**Last Updated**: July 7, 2025
**Version**: 1.0

