from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# SPF reference data and recommendations
SPF_LEVELS = {
    'low': {'min': 0, 'max': 14, 'protection': 'Minimal', 'uva': False},
    'medium': {'min': 15, 'max': 29, 'protection': 'Moderate', 'uva': False},
    'high': {'min': 30, 'max': 49, 'protection': 'High', 'uva': True},
    'very_high': {'min': 50, 'max': float('inf'), 'protection': 'Very High', 'uva': True}
}

def check_spf_validity(spf_value):
    """Check if SPF value is valid and return category"""
    try:
        spf = float(spf_value)
        if spf < 0:
            return {'valid': False, 'error': 'SPF cannot be negative'}
        
        for category, limits in SPF_LEVELS.items():
            if limits['min'] <= spf <= limits['max']:
                return {
                    'valid': True,
                    'spf': spf,
                    'category': category,
                    'protection_level': limits['protection'],
                    'uva_protection': limits['uva']
                }
    except ValueError:
        return {'valid': False, 'error': 'SPF must be a number'}
    
    return {'valid': False, 'error': 'Invalid SPF value'}

def get_recommendation(spf_info):
    """Generate sunscreen recommendation based on SPF"""
    if not spf_info['valid']:
        return None
    
    spf = spf_info['spf']
    category = spf_info['category']
    
    recommendations = {
        'low': 'Not recommended for outdoor activities. Better for daily moisturizers.',
        'medium': 'Suitable for light outdoor activities or supplementary protection.',
        'high': 'Recommended for regular outdoor activities and water sports.',
        'very_high': 'Recommended for prolonged sun exposure and sensitive skin.'
    }
    
    uva_note = 'Also provides UVA protection.' if spf_info['uva_protection'] else 'Consider UVA protection with a broad-spectrum sunscreen.'
    
    return f"{recommendations[category]} {uva_note}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check-spf', methods=['POST'])
def check_spf_api():
    """API endpoint to check SPF value"""
    data = request.json
    spf_value = data.get('spf_value', '')
    product_name = data.get('product_name', 'Unknown Product')
    
    spf_info = check_spf_validity(spf_value)
    
    if spf_info['valid']:
        recommendation = get_recommendation(spf_info)
        return jsonify({
            'success': True,
            'product_name': product_name,
            'spf': spf_info['spf'],
            'category': spf_info['category'],
            'protection_level': spf_info['protection_level'],
            'uva_protection': spf_info['uva_protection'],
            'recommendation': recommendation
        })
    else:
        return jsonify({
            'success': False,
            'error': spf_info['error']
        }), 400

@app.route('/api/spf-info', methods=['GET'])
def spf_info_api():
    """Get SPF reference information"""
    return jsonify({
        'levels': SPF_LEVELS,
        'info': {
            'uva': 'UVA protection is important for anti-aging and skin health',
            'broad_spectrum': 'Look for broad-spectrum sunscreens that protect against both UVA and UVB',
            'reapplication': 'Reapply sunscreen every 2 hours or after swimming/sweating'
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
