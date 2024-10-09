from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/run-script', methods=['POST'])  # Ensure this accepts POST

def run_script():
    try:
        # Run the Tkinter script
        subprocess.Popen(['python', 'index.py'])  # Runs the Tkinter script
        return "", 200 
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
if __name__ == '__main__':
    app.run(debug=True)
