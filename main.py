from flask import Flask #, render_template
# import get_data as gd
# from models.database import Session

app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello, Vercel!'
    # global session
    # plot = gd.print_counted_dates(gd.get_counted_dates(session))
    # return render_template('base.html', days_plot=plot)

if __name__ == '__main__':
    # session = Session()
    app.run()