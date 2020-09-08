from flask import render_template
from app import app

# views

@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    
    
    title = 'Home - welcome to the best Movie Review Website Online'
    return render_template('index.html', title= title )

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    
    '''
    View movie page function that returns the movie details page and its data
    '''
    title = f'You are viewing {movie_id}'
    return render_template('movie.html',title = title)
