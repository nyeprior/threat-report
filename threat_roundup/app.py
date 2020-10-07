from flask import Flask, render_template, request
import datetime
web_app = Flask(__name__)
pages = ["home", "malware", "ttp", "apt", "vulnerabilities", "other", "generate"]

malwareArticles = []
ttpArticles = []
aptArticles = []
vulnsArticles = []
otherArticles = []
today = datetime.datetime.utcnow().strftime('%B %d %Y')
counters = {}


@web_app.before_request
def before_request_func():
    global counters
    no_malware = len(malwareArticles)
    no_ttp = len(ttpArticles)
    no_apt = len(aptArticles)
    no_vulns = len(vulnsArticles)
    no_other = len(otherArticles)
    counters = {"malware": no_malware, "ttp": no_ttp,
                "apt": no_apt, "vulnerabilities": no_vulns, "other": no_other}


@web_app.route('/', methods=["GET"])
@web_app.route('/home', methods=["GET"])
def index():
    if request.method == "GET":
        return render_template('index.html', pages=pages, counters=counters)
    else:
        return render_template('generate.html', pages=pages, counters=counters)


@web_app.route('/generate', methods=["GET", "POST"])
def generate():
    newsletter = render_template('newsletter.html', pages=pages,
                                 malwareArticles=malwareArticles,
                                 ttpArticles=ttpArticles,
                                 vulnsArticles=vulnsArticles,
                                 otherArticles=otherArticles,
                                 aptArticles=aptArticles,
                                 today=today, counters=counters)
    with open('newsletter.txt', 'w') as f:
        f.write(newsletter)
    return newsletter


@web_app.route('/malware', methods=["GET", "POST"])
def malware():
    global malwareArticles
    if request.method == "GET":
        #counters = refresh_counters()
        return render_template('articles/malware.html',
                               pages=pages,
                               malwareArticles=malwareArticles, counters=counters)
    else:
        url = request.form.get('url')
        headline = request.form.get('headline')
        if url == "" or url is None or headline == "" or headline is None:
            error = True
            return render_template('articles/malware.html',
                                   pages=pages,
                                   malwareArticles=malwareArticles,
                                   error=error, counters=counters)
        if url[:4] != "http":
            url = "http://" + url
        malwareArticles.append(
            {"url": url, "headline": headline})
        before_request_func()
        return render_template('articles/malware.html',
                               pages=pages,
                               malwareArticles=malwareArticles, counters=counters)


@web_app.route('/apt', methods=["GET", "POST"])
def apt():
    global aptArticles
    if request.method == "GET":
        #counters = refresh_counters()
        return render_template('articles/apt.html',
                               pages=pages,
                               aptArticles=aptArticles, counters=counters)
    else:
        url = request.form.get('url')
        headline = request.form.get('headline')
        if url == "" or url is None or headline == "" or headline is None:
            error = True
            return render_template('articles/apt.html',
                                   pages=pages,
                                   aptArticles=aptArticles,
                                   error=error, counters=counters)
        if url[:4] != "http":
            url = "http://" + url
        aptArticles.append(
            {"url": url, "headline": headline})
        before_request_func()
        return render_template('articles/apt.html',
                               pages=pages,
                               aptArticles=aptArticles, counters=counters)


@web_app.route('/ttp', methods=["GET", "POST"])
def ttp():
    #counters = refresh_counters()
    global ttpArticles
    if request.method == "GET":
        return render_template('articles/ttp.html',
                               pages=pages,
                               ttpArticles=ttpArticles, counters=counters)
    else:
        url = request.form.get('url')
        headline = request.form.get('headline')
        if url == "" or url is None or headline == "" or headline is None:
            error = True
            return render_template('articles/ttp.html',
                                   pages=pages,
                                   ttpArticles=ttpArticles,
                                   error=error, counters=counters)
        if url[:4] != "http":
            url = "http://" + url
        ttpArticles.append(
            {"url": url, "headline": headline})
        before_request_func()
        return render_template('articles/ttp.html',
                               pages=pages,
                               ttpArticles=ttpArticles, counters=counters)


@web_app.route('/vulns', methods=["GET", "POST"])
@web_app.route('/vulnerabilities', methods=["GET", "POST"])
def vulns():
    #counters = refresh_counters()
    global vulnsArticles
    if request.method == "GET":
        return render_template('articles/vulns.html',
                               pages=pages,
                               vulnsArticles=vulnsArticles, counters=counters)
    else:
        url = request.form.get('url')
        headline = request.form.get('headline')
        if url == "" or url is None or headline == "" or headline is None:
            error = True
            return render_template('articles/vulns.html', pages=pages,
                                   vulnsArticles=vulnsArticles,
                                   error=error, counters=counters)
        if url[:4] != "http":
            url = "http://" + url
        vulnsArticles.append(
            {"url": url, "headline": headline})
        before_request_func()
        return render_template('articles/vulns.html',
                               pages=pages,
                               vulnsArticles=vulnsArticles, counters=counters)


@web_app.route('/other', methods=["GET", "POST"])
def other():
    #counters = refresh_counters()
    global otherArticles
    if request.method == "GET":
        return render_template('articles/other.html', pages=pages,
                               otherArticles=otherArticles, counters=counters)
    else:
        url = request.form.get('url')
        headline = request.form.get('headline')
        if url == "" or url is None or headline == "" or headline is None:
            error = True
            return render_template('articles/other.html', pages=pages,
                                   otherArticles=otherArticles,
                                   error=error, counters=counters)
        if url[:4] != "http":
            url = "http://" + url
        otherArticles.append(
            {"url": url, "headline": headline})
        before_request_func()
        return render_template('articles/other.html',
                               pages=pages,
                               otherArticles=otherArticles, counters=counters)
