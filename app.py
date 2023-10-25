from flask import Flask, render_template, request
from functions.countWords import count_words
from functions.login import login
from functions.average import average
from functions.average import average
from functions.max import max
from functions.min import min
from functions.reverse_string import reverse
from functions.palindrome import palindrome
from functions.factorial import factorial
from functions.count_occurrences import count_occurrences



app = Flask(__name__)




@app.route("/")
def homeRouter():
    return render_template('index.html')

@app.route('/countWords', methods=['GET', 'POST'])
def countWordsRouter():

    if request.method == 'POST':
        # Check if text was submitted
        if ('text' in request.form) and not(request.form['text'] == ""):
            text = request.form['text']
            word_count = count_words(text)
            return render_template('countWords.html', word_count=word_count, text=text)
        
        # Check if file was uploaded
        if ('file' in request.files.keys()) and not(request.files['file'].filename == ""):
            file = request.files['file']
            if file.filename.endswith('.txt'):
                text = file.read().decode('utf-8')
                word_count = count_words(text)
                return render_template('countWords.html', word_count=word_count, file=file.filename)

    # Render the default page
    return render_template('countWords.html')

@app.route('/average', methods=['GET', 'POST'])
def averageRouter():
    if request.method == 'POST':

        input = request.form["input"]
        inputList = [int(n) for n in input.split()]
        
        result = average(inputList)
            
        return render_template('average.html', result=result, input = input)
    
    return render_template('average.html')

@app.route('/max', methods=['GET', 'POST'])
def maxRouter():
    if request.method == 'POST':
        input = request.form["input"]
        inputList = [int(n) for n in input.split()]
        result = max(inputList)
            
        return render_template('max.html', result=result, input = input)
    
    return render_template('max.html')

@app.route('/min', methods=['GET', 'POST'])
def minRouter():
    if request.method == 'POST':
        input = request.form["input"]
        inputList = [int(n) for n in input.split()]
        result = min(inputList)
            
        return render_template('min.html', result=result, input = input)
    
    return render_template('min.html')

@app.route('/factorial', methods=['GET', 'POST'])
def factorialRouter():
    if request.method == 'POST':
        input = request.form["input"]
        result = factorial(int(input))
            
        return render_template('factorial.html', result=result, input = input)
    
    return render_template('factorial.html')

@app.route('/palindrome', methods=['GET', 'POST'])
def palindromeRouter():
    if request.method == 'POST':
        input = request.form["input"]
        result = palindrome(input)
            
        return render_template('palindrome.html', result=result, input = input)
    
    return render_template('palindrome.html')

@app.route('/reverse', methods=['GET', 'POST'])
def reverseRouter():
    if request.method == 'POST':
        input = request.form["input"]
        result = reverse(input)
            
        return render_template('reverse.html', result=result, input = input)
    
    return render_template('reverse.html')

@app.route('/count_occurrences', methods=['GET', 'POST'])
def countOccurrencesRouter():
    if request.method == 'POST':
        input = request.form["input"]
        inputList = input.split()
        result = count_occurrences(inputList)
            
        return render_template('count_occurrences.html', result=result, input = input)
    
    return render_template('count_occurrences.html')



if __name__ == '__main__':
    app.run(debug=True)