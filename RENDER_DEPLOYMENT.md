# Deploying to Render

This guide will help you deploy the Flask backend to Render.

## Prerequisites

- A Render account (free tier available)
- Your code pushed to a Git repository (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### 1. Create a New Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your Git repository
4. Select the repository containing this backend

### 2. Configure Build Settings

- **Name**: `legal-docs-backend` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT --workers 4 --timeout 120 app:app`

Alternatively, Render will automatically detect the `Procfile` if present.

### 3. Set Environment Variables

In the Render dashboard, go to "Environment" and add these variables:

```
PORT=3001
FRONTEND_URL=https://your-frontend-domain.onrender.com
DEBUG=False
FLASK_ENV=production
HOST=0.0.0.0
```

**Important Notes:**
- Render automatically sets the `PORT` environment variable, so you don't need to set it manually
- Update `FRONTEND_URL` with your actual frontend URL (or multiple URLs separated by commas)
- Set `DEBUG=False` for production
- If your frontend is also on Render, use the format: `https://your-frontend-service.onrender.com`

### 4. Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Start the service using the Procfile or start command

### 5. Verify Deployment

Once deployed, test your endpoints:

```bash
# Health check
curl https://your-backend-service.onrender.com/api/health

# Test search
curl -X POST https://your-backend-service.onrender.com/api/generate \
  -H "Content-Type: application/json" \
  -d '{"query": "contract law"}'
```

## Important Configuration Notes

### CORS Configuration

The backend is configured to accept requests from the `FRONTEND_URL` you specify. If you need to allow multiple origins, separate them with commas:

```
FRONTEND_URL=https://frontend1.onrender.com,https://frontend2.vercel.app
```

### Port Configuration

Render automatically assigns a port via the `PORT` environment variable. The application reads this automatically, so you don't need to configure it manually.

### Production Settings

- `DEBUG=False` - Disables Flask debug mode
- `FLASK_ENV=production` - Sets production environment
- Gunicorn is used as the production WSGI server (configured in Procfile)

## Troubleshooting

### Build Fails

- Check that `requirements.txt` is in the root directory
- Verify Python version compatibility (runtime.txt specifies Python 3.11)
- Check build logs in Render dashboard

### Service Won't Start

- Verify the start command is correct
- Check that `app.py` is in the root directory
- Review logs in Render dashboard for error messages

### CORS Errors

- Ensure `FRONTEND_URL` matches your frontend URL exactly (including https://)
- Check that the frontend is making requests to the correct backend URL
- Verify CORS headers in browser developer tools

### 502 Bad Gateway

- Check that the service is running (not sleeping on free tier)
- Verify the health endpoint responds: `/api/health`
- Review application logs for errors

## Free Tier Limitations

Render's free tier has some limitations:
- Services spin down after 15 minutes of inactivity
- First request after spin-down may be slow (cold start)
- Limited to 750 hours/month

For production use, consider upgrading to a paid plan.

## Custom Domain

To use a custom domain:
1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain and follow DNS configuration instructions

## Monitoring

- View logs in real-time in the Render dashboard
- Set up alerts for service failures
- Monitor response times and errors

## Updating the Deployment

Simply push changes to your Git repository. Render will automatically:
1. Detect the changes
2. Rebuild the service
3. Deploy the new version

You can also manually trigger deployments from the Render dashboard.

