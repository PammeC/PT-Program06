from flask import Flask, request
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_prime():
    result = ""
    number = ""
    
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            is_prime = True
            if number < 2:
                is_prime = False
            else:
                for i in range(2, int(number ** 0.5) + 1):
                    if number % i == 0:
                        is_prime = False
                        break
            result = "es primo" if is_prime else "no es primo"
        except ValueError:
            result = "Por favor, ingresa un número válido"
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Verificador de Números Primos</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 90%;
                max-width: 400px;
            }}
            h1 {{
                color: #333;
                margin-bottom: 20px;
                font-size: 24px;
            }}
            .form-group {{
                margin: 20px 0;
            }}
            input[type="number"] {{
                padding: 10px;
                font-size: 16px;
                border: 2px solid #ddd;
                border-radius: 5px;
                width: 200px;
                margin: 10px 0;
            }}
            input[type="submit"] {{
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }}
            input[type="submit"]:hover {{
                background-color: #2980b9;
            }}
            .result {{
                font-size: 18px;
                color: #2c3e50;
                padding: 20px;
                background-color: #f8f9fa;
                border-radius: 5px;
                margin-top: 20px;
                display: {result and 'block' or 'none'};
            }}
            .number {{
                color: #3498db;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Verificador de Números Primos</h1>
            <form method="POST">
                <div class="form-group">
                    <input type="number" 
                           name="number" 
                           placeholder="Ingresa un número"
                           value="{number}"
                           required>
                </div>
                <input type="submit" value="Verificar">
            </form>
            <div class="result">
                {f'El número <span class="number">{number}</span> {result}' if result else ''}
            </div>
        </div>
    </body>
    </html>
    '''
    return html

if __name__ == "__main__":
    def open_browser():
        webbrowser.open("http://127.0.0.1:8080/")
    Timer(1, open_browser).start()
    
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)