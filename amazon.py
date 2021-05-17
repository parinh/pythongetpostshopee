from bs4 import BeautifulSoup

class Amazon:
    def getItemDataForAmazonSearch(self,soup):
        a=[]
    # Get Name
        item_n = soup.select_one("a.a-link-normal.a-text-normal > span.a-size-base-plus.a-color-base.a-text-normal" )
        if (item_n):
            a.append(item_n.get_text())
            # print(item_n.get_text())
        else:
            a.append("no name")
            # print("no name")

        # Price
        price = soup.select_one("span.a-price > span.a-offscreen")
        if (price):
            a.append(price.get_text())
            # print(price.get_text())
        else:
            a.append("no price found")
            # print("no price found")

        # rating
        rating = soup.select_one("i > span.a-icon-alt")
        if (rating):
            a.append(rating.get_text())
            # print(rating.get_text())
        else:
            a.append("no rating found")
            # print("no rating found")

        #review
        review = soup.select_one("a.a-link-normal > span.a-size-base")
        if (review):
            a.append(review.get_text())
            # print(review.get_text())
        else:
            a.append("no review")
            # print("no review")
            
        imgs = soup.select_one("img.s-image")
        a.append(imgs['src'])
        # print(imgs['src'])
        return a
    
    def getDataFromPostForAmazonSearch(self,html):
        b=[]
        print ("get data..")
        soup = BeautifulSoup(html, "html.parser")
        for item_n in soup.find_all('div',  class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20'):
            b.append(self.getItemDataForAmazonSearch(item_n))
        
        return b