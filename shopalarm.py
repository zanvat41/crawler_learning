import asyncio
import time
import winsound
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main(round):
    browser = await launch()
    page = await browser.newPage()
    # await page.goto('http://quotes.toscrape.com/js/')
    # await page.goto('https://blog.csdn.net/weixin_42232219/article/details/89391932')
    # await page.goto('https://order.mandarake.co.jp/order/detailPage/item?itemCode=1190212568&lang=en') #骨雕骨雕
    await page.goto('https://order.mandarake.co.jp/order/detailPage/item?itemCode=1091523939&lang=en')
    # await page.goto('https://order.mandarake.co.jp/order/detailPage/item?itemCode=1189448701&lang=en')

    time.sleep(5)
    # await page.pdf(path="example.pdf")
    doc = pq(await page.content())
    # print("Quotes:",doc('.quote').length)
    # print("Sold out")
    # print(doc('.soldout'))
    # print(doc('.soldout').children().length)
    # if "<p>Soldout</p>" in doc('.soldout')[0]:
    #    print(123)
    # print("Add to cart")
    # print(doc('.material-icons').length)
    # print(doc('#div'))
    len1 = doc('.material-icons').length
    len2 = doc('.other_item').children().length
    # print(doc('.other_item').children().length)
    print(len1)
    print(len2)
    print("-------------Round:",round)
    # If there's item in store, alarm
    if len1 > 0 or len2 > 0:
        for i in range(10):
            winsound.Beep(1000,440)
    await browser.close()


# asyncio.get_event_loop().run_until_complete(main())

# for i in range(2):
for i in range(300):
    asyncio.get_event_loop().run_until_complete(main(i))
    time.sleep(25)


