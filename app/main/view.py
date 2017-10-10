from . import main


@main.route('/',methods=['GET','POST'])
def index():
    return "<h1>index page</h1>"
