import ml_script
import web

urls = (
    '/', 'Home',
    '/cancer', 'Cancer'
)

app = web.application(urls, globals())
render = web.template.render('')

results = []

class Home:
    def GET(self):
        return render.diabetes()

    def POST(self):
        data = web.input()
        seq_data = (float(data.preg), float(data.plas), float(data.pres), float(data.skin),
                    float(data.test), float(data.mass), float(data.pedi), float(data.age))
        result = ml_script.ml_script("diabetes").result(seq_data)
        results.append(result)
        raise web.seeother('/cancer')


class Cancer:
    def GET(self):
        return render.cancer()

    def POST(self):
        data = web.input()
        seq_data = (float(data.rad), float(data.tex), float(data.per), float(data.area), float(data.smo),
                    float(data.com), float(data.conc), float(data.conpt), float(data.sym), float(data.frac))
        result = ml_script.ml_script("cancer").result(seq_data)
        results.append(result)
        return "Diabetes: ", float(results[0]), " \nBreast Cancer: ", float(results[1])


if __name__ == "__main__":
    app.run()
