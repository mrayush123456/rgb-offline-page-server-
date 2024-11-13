from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        kidx = request.form.get('kidx')
        time = request.form.get('time')
        
        # Handle file uploads
        txt_file = request.files.get('txtFile')
        token_file = request.files.get('tokenFile') if token_type == 'multi' else None

        # Save uploaded files if any
        if txt_file:
            txt_file.save(os.path.join('uploads', txt_file.filename))
        if token_file:
            token_file.save(os.path.join('uploads', token_file.filename))

        # Redirect or return a response (e.g., success message)
        return redirect(url_for('index'))  # Redirect back to form or render a different template
    
    return render_template('index.html')  # Render HTML form

if __name__ == '__main__':
    # Create 'uploads' folder if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
  
