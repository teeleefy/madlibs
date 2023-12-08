#---------------------APP PREP: Accessing FLASK, TOOLBAR, and JINJA---------------
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'candy-apple'
toolbar = DebugToolbarExtension(app)
#----------------------------------------------------------------------------------

@app.route('/')
def madlib():
    '''Shows home madlib page'''
    new_story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    my_prompts= new_story.prompts
    return render_template('madlib.html', prompts = my_prompts)

@app.route('/story')
def make_story():
    '''Shows the story created'''
    new_story = Story(["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    # my_noun= "giraffe"
    # my_verb= "pet"
    my_obj = {}
    my_prompts = new_story.prompts
    for word in my_prompts:
        my_obj.update({word: request.args[word]})
    # my_noun = request.args['noun']
    # my_verb = request.args['verb']
    # my_obj = {'noun': my_noun, 'verb': my_verb}
    return render_template('story.html', story = new_story, ans = my_obj)

