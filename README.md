# ECM - European Center for Magirus

A professional Django web application for managing and selling Magirus truck spare parts.

## 🚛 About

ECM (European Center for Magirus) is a comprehensive e-commerce platform designed specifically for Magirus truck spare parts. The application provides a user-friendly interface for customers to browse, search, and inquire about authentic Magirus parts.

## ✨ Features

- **Professional Homepage**: Hero section with company branding and featured parts
- **Parts Catalog**: Comprehensive searchable inventory with advanced filtering
- **Part Details**: Detailed specifications, pricing, and compatibility information
- **Inquiry System**: Customer contact form for quotes and part requests
- **Admin Dashboard**: Complete backend management for inventory and inquiries
- **Responsive Design**: Mobile-optimized interface using Tailwind CSS
- **SEO Friendly**: Clean URLs and proper meta tags

## 🛠️ Technology Stack

- **Backend**: Django 5.2.3
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter, Playfair Display)

## 📦 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

4. **Access Application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 📁 Project Structure

```
ECM/
├── ecm_website/          # Main Django project
│   ├── settings.py       # Configuration
│   ├── urls.py          # URL routing
│   └── static/          # Static files
├── parts/               # Parts app
│   ├── models.py        # Data models
│   ├── views.py         # Business logic
│   ├── forms.py         # Form definitions
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
├── templates/           # Global templates
├── media/              # User uploads
├── manage.py           # Django management
└── requirements.txt    # Dependencies
```

## 🎯 Key Models

- **Category**: Part categories (Engine, Brake, Transmission)
- **TruckModel**: Compatible truck models with year ranges
- **Part**: Individual parts with specifications and relationships
- **Inquiry**: Customer inquiry form submissions

## 🔧 Admin Features

- Part inventory management
- Category and truck model administration
- Customer inquiry tracking
- Image upload for parts
- Stock quantity management
- Price and availability control

## 🎨 Design Features

- Modern, professional design
- ECM brand colors and typography
- Responsive grid layouts
- Interactive hover effects
- Smooth animations and transitions
- Mobile-first approach

## 📱 Pages

1. **Home** (`/`): Landing page with featured parts and company info
2. **Parts** (`/parts/`): Searchable catalog with filters
3. **Part Detail** (`/parts/<id>/`): Individual part specifications
4. **Inquiry** (`/inquiry/`): Customer contact form
5. **About** (`/about/`): Company information
6. **Contact** (`/contact/`): Contact details

## 🔍 Search & Filter

- Text search across part names, numbers, and descriptions
- Category-based filtering
- Truck model compatibility filtering
- Pagination for large result sets
- Clear filter options

## 📧 Inquiry System

- Customer name and email capture
- Optional part number specification
- Detailed message field
- Form validation and error handling
- Success confirmation messages

## 🚀 Deployment

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions including:
- Environment configuration
- Database setup
- Static file handling
- Production considerations
- Security recommendations

## 📊 Sample Data

The application includes sample data for testing:
- 3 part categories
- 2 truck models
- 3 sample parts with relationships
- Admin user (username: admin, password: admin123)

## 🔒 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure form handling
- Admin authentication

## 🎯 Future Enhancements

- User authentication and accounts
- Shopping cart functionality
- Payment integration
- Email notifications
- Advanced search features
- Multi-language support
- API endpoints

## 📄 License

This project is proprietary software developed for ECM (European Center for Magirus).

## 🤝 Support

For technical support or questions, please contact the development team or use the admin interface for application management.

---

**Status**: ✅ Production Ready  
**Version**: 1.0  
**Last Updated**: July 7, 2025

