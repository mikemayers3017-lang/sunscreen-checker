# Sunscreen SPF Checker Web App

A Flask-based web application to check and analyze sunscreen SPF (Sun Protection Factor) levels with personalized recommendations.

## Features

- **SPF Level Analysis**: Input any SPF value and get detailed protection information
- **Product Tracking**: Name your sunscreen products for easy reference
- **Protection Levels**: Categorizes SPF into Low, Moderate, High, and Very High
- **UVA Protection Indicator**: Shows if the sunscreen likely provides UVA protection
- **Smart Recommendations**: Personalized usage recommendations based on SPF level
- **Responsive Design**: Works on desktop and mobile devices
- **Clean UI**: Modern gradient design with intuitive interface

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python sunscreen_checker.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Enter your sunscreen product name and SPF level to check

## How It Works

### SPF Categories
- **SPF 0-14**: Minimal protection (not recommended for outdoor activities)
- **SPF 15-29**: Moderate protection (light outdoor activities)
- **SPF 30-49**: High protection (regular outdoor activities)
- **SPF 50+**: Very High protection (prolonged sun exposure)

### UVA Protection
Products with SPF 30+ typically include UVA protection. Lower SPF products may not indicate UVA coverage.

### Recommendations
- **Reapply** sunscreen every 2 hours
- **Apply generously**: Most people don't apply enough sunscreen
- **Use daily**: Even on cloudy days, UV rays can penetrate
- **Broad-spectrum**: Always look for broad-spectrum protection

## API Endpoints

### Check SPF
**POST** `/api/check-spf`

Request:
```json
{
    "product_name": "Coppertone Sport",
    "spf_value": 50
}
```

Response:
```json
{
    "success": true,
    "product_name": "Coppertone Sport",
    "spf": 50,
    "category": "very_high",
    "protection_level": "Very High",
    "uva_protection": true,
    "recommendation": "Recommended for prolonged sun exposure and sensitive skin..."
}
```

### Get SPF Info
**GET** `/api/spf-info`

Returns reference information about SPF levels and UV protection.

## File Structure

```
.
├── sunscreen_checker.py      # Flask application and API logic
├── templates/
│   └── index.html            # Web interface
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Technologies Used

- **Python 3.x**: Backend language
- **Flask**: Web framework
- **HTML5/CSS3/JavaScript**: Frontend
- **Responsive Design**: Mobile-friendly interface

## Tips for Sunscreen Use

✓ Apply 15-30 minutes before sun exposure
✓ Use about 1 ounce (shot glass full) for full body coverage
✓ Reapply after swimming or heavy sweating
✓ Don't forget ears, top of feet, and part line
✓ Use year-round for daily protection
✓ Store away from heat and direct sunlight

## Future Enhancements

- Product database with popular sunscreen brands
- SPF effectiveness calculator based on reapplication
- UV index integration
- Ingredient analysis
- User accounts and product history
- Expiration date tracking

## License

Open source educational project

## Disclaimer

This tool provides general information about SPF levels. Always follow manufacturer instructions and consult a dermatologist for personalized skincare advice.
