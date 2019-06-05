# -*- coding: utf-8 -*-
from plant_models import Plant

def seed_db():
    trad_zeb = Plant(name="Tradescantia zebrina", 
                color="Purple",
                description="The stripey purple leaves on this trailing houseplant make for such a pretty pop of color. This plant prefers full sun—the more light it gets, the more purple you will see, according to the blog Plants Are the Strangest People. Keep the soil wet for best results.",
                url="https://media2.s-nbcnews.com/j/newscms/2016_08/985021/wandering-jew_9b05b2da5364db514cd04d816b54e96c.fit-560w.jpg"
            )
    trad_zeb.put()

    oxalis = Plant(name="Oxalis Purple Clover", 
                color="Purple",
                description="Get the right balance of light and temperature to produce these royal purple leaves with a unique shamrock shape. Medium light near a window should give you the best and brightest leaves.",                
                url="http://cdn.shopify.com/s/files/1/1419/7120/files/oxalis_triang_skybluebowl_large.jpg?v=1492464702"
            )
    oxalis.put()

    orchid = Plant(name="Phalaenopsis Orchid", 
                color="White",
                description="This classic orchid has long sprays of large white flowers that are well known for their elegant, sophisticated look on coffee or side tables—or anywhere! There are many species of this plant, which favors bright, indirect sunlight and humid conditions, according to Just Add Ice Orchids.",      
                url="https://target.scene7.com/is/image/Target/GUEST_d3d5aad8-68f2-46d9-ad8a-3df9d32f3959?wid=488&hei=488&fmt=pjpeg"
            )
    orchid.put()

    jasmine = Plant(name="Jasmine", 
                color="White",
                description="The fragrance that wafts from the white or pink flowers on jasmine plants can be downright intoxicating. The plants are vining, so you can train them into pretty topiaries indoors. According to Life on the Balcony, jasmine prefers bright, filtered light and a bit of humidity—so a bathroom could be just right.",                
                url="https://media3.s-nbcnews.com/j/newscms/2016_08/985046/jasmine_0d8b6c152719ea9c287b93589e7fa07e.fit-560w.jpg"
            )
    jasmine.put()

    dieff = Plant(name="Dieffenbachia", 
                color="Green",
                description="For a pretty pop of green anywhere around the house, this is a hardy and quick-growing plant with visually interesting leaves that can have spots or stripes. (It’s also known as “dumb cane” for the effects of its toxic sap—so use caution.) It favors moderate to low light and moderate to heavy watering, according to the blog Houseplant Care Tips.",                
                url="https://assets.bakker.com/ProductPics/810x978/71899-00-BAKIE_20190510104204.jpg"
            )
    dieff.put()


    cala = Plant(name="Calathea", 
                color="Green",
                description="It’s easy to see why these are nicknamed “peacock plants.” Their variegated, tropical foliage spans from green to purple, and the unique pattern of the leaves does indeed recall peacock feathers. It may be a tad more fussy than other tropical plants, preferring shade or dappled light and some humidity, but the final result is well worth it.",                
                url="https://res.cloudinary.com/patch-gardens/image/upload/c_fill,f_auto,h_840,q_auto:good,w_840/v1539774938/products/calathea-19d9d9.jpg"
            )
    cala.put()

    anth = Plant(name="Anthurium", 
                color="Red",
                description="The flowering version of this plant has pretty red or yellow blooms that conjure lush, tropical gardens. Try one in your home if you can provide bright light and low to moderate watering, according to the Houseplant Care Tips blog.",                
                url="https://res.cloudinary.com/bloomnation/c_pad,d_vendor:global:catalog:product:image.png,f_auto,fl_preserve_transparency,q_auto/v1487098715/vendor/2805/catalog/product/w/e/web-fotos-2014-023.jpg"
            )
    anth.put()

    cliv = Plant(name="Clivia", 
            color="Red",
            description="This South African plant has become sought-after due to its lovely orange-red flowers, which are reminiscent of hibiscus. They thrive in bright indirect light and don’t mind if you forget about them occasionally.",                
            url="https://q7i2y6d5.stackpathcdn.com/wp-content/uploads/2010/07/clivia-400x300.jpg"
        )
    cliv.put()

    ama = Plant(name="Yellow Goddess Amaryllis", 
            color="Yellow",
            description="Talk about a cheery pop of color! This lovely plant has pretty trumpet-shaped yellow blooms, and a relatively compact size for easy placement around the house. It does well in bright, indirect light according to the blog Cozy Bliss.",                
            url="http://d3t0t2nqwmr1c9.cloudfront.net/photos/2122/Amaryllis_Hippeastrum_Yellow_Goddess-1.medium.jpg"
        )
    ama.put()

    zebra = Plant(name="Zebra Plant", 
            color="Yellow",
            description="Shiny, appealingly zebra-like leaves make this an instant winner, but if you’re willing to help the plant through a period of dormancy, you’ll also find that super-saturated yellow blossoms appear like a crown atop this stunning plant.",                
            url="https://static1.squarespace.com/static/599ca6a3e4fcb572c84c0670/t/5a32a454ec212d09e401275d/1513268309072/FullSizeRender.jpg"
        )
    zebra.put()