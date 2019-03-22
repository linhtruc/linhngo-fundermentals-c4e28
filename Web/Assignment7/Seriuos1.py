from flask import Flask, render_template
app = Flask(__name__)

#without render

@app.route('/bmi1/<int:weight>/<int:height>')
def bmi1(weight, height):
    bmi = (weight/((height/100)*(height/100)))
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# with render

@app.route('/bmi2/<int:weight>/<int:height>')
def bmi2(weight, height):
    bmi = (weight/((height/100)*(height/100)))
    return render_template('Serious1.html', bmi=bmi)

        
if __name__ == '__main__':
  app.run(debug=True)