from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'sira_consulting_ai_2026'

# డమ్మీ యూజర్ డేటా
USER_DATA = {"admin@siraconsulting.com": "ai_impact_2026"}

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    pw = request.form.get('password')
    if email in USER_DATA and USER_DATA[email] == pw:
        session['user'] = email
        return redirect(url_for('dashboard'))
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html')

@app.route('/api/stats')
def get_stats():
    # LLM తరహాలో బిజినెస్ ఇన్సైట్స్ -
    llm_insights = [
        "AI detected a 15% surge in market demand. Inventory adjustment recommended.",
        "Predictive analysis shows a 12% potential growth in the next quarter.",
        "Operational efficiency is at its peak. Automation reduces manual errors.",
        "Customer sentiment is high. AI suggests launching a personalized campaign."
    ]
    return jsonify({
        "efficiency": f"+{random.randint(25, 45)}%",
        "bar_data": [random.randint(20, 100) for _ in range(6)],
        "donut_data": [random.randint(40, 60), random.randint(20, 30), 15],
        "narrative": random.choice(llm_insights)
    })

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
