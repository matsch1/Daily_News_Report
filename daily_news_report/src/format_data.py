from retrieve_data import APICollector


class JSONFormatter():
    def __init__(self, input_json) -> None:
        self.json = input_json
        self.articles = self.json['articles']

        self.print_articles()

    def print_articles(self):
        number_of_articles = len(self.articles)

        self.report = open("report.html", "w")

        self.report.write(
            "<html>\n<head>\n<title> \n News Report \n </title>\n</head>\n<body>\n")
        for article in self.articles:
            self.print_article_information(article)
        self.report.write("</body>\n <html>")
        self.report.close()

    def print_article_information(self, article):
        self.report.write("<h1>" + article['title'] + "<\h1>")
        self.report.write("<h2>" + article['description'] + "<\h2>")
        # print(article['source']['name'])
        # print(article['urlToImage'])
        print("<a href = " + article['url'] + "><\\a>")


if __name__ == "__main__":
    api_collector = APICollector()
    json_formatter = JSONFormatter(api_collector.get_news_json())
