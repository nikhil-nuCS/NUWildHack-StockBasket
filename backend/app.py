# from dotenv import load_dotenv
# load_dotenv()
from flask import Flask, request, Response
from flask_cors import CORS
from flask_restful import Api
from flask import render_template
from views import initialize_routes
from firebaseconfig import FirebaseFlaskConfig

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
api = Api(app)
app.url_map.strict_slashes = False
firebase_app = FirebaseFlaskConfig()

initialize_routes(api, firebase_app)
@app.route('/')
def home():   
    return render_template(
        'index.html', 
    )

# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()
