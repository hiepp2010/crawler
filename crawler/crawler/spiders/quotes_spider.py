import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["http://www.quotationspage.com/quotes/"]
    #Change url where you want to start 

    def parse(self, response):
        author_page_links = response.css("div.authorletters a")
        yield from response.follow_all(author_page_links, self.parse_author)

       # pagination_links = response.css("li.next a")
       # yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        authors = response.css("div.authorrow a")
        yield from response.follow_all(authors, self.parse_quotes)
        
        #def extract_with_css(query):
         #   return response.css(query).get(default="").strip()
    def parse_quotes(self,response):
        quotes=response.css("dt.quote a::text")
        author=response.css("dd.author b::text").get()
        for quote in quotes:
            yield {
                "name":author,
                "quote":quote.get()
            }
        