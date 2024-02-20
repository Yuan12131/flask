from flask import Flask, render_template, request

app = Flask(__name__)

# GET 요청 처리: index.html을 클라이언트에 전달
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# POST 요청 처리: 받은 데이터를 터미널에 출력하고 클라이언트에 전달
@app.route('/submit', methods=['POST'])
def submit():
    input_data = request.form['inputData']  # input 요소의 name 속성을 사용
    print('Received data:', input_data)
    return render_template('index.html', result=input_data)

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
