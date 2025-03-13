from .utils import make_word_sets

sentences: tuple[str, ...] = (
    "Beer is one of the oldest and most widely consumed alcoholic drinks in the world.",
    "The brewing process involves fermentation of starches, typically from cereal grains.",
    "Beer can be made from barley, wheat, corn, or rice.",
    "The alcohol content of beer typically ranges from 4% to 6% by volume.",
    "Craft beer is a popular trend in the beer industry, emphasizing unique flavors and ingredients.",
    "Lager and ale are the two primary categories of beer.",
    "The hops used in beer provide bitterness, flavor, and aroma.",
    "Ales tend to be brewed at warmer temperatures than lagers.",
    "The word 'beer' comes from the Latin word 'bibere', meaning 'to drink'.",
    "Beer was a staple in ancient civilizations, including Egypt and Mesopotamia.",
    "The oldest known recipe for beer was discovered in ancient Sumerian tablets.",
    "The process of brewing beer involves mashing, boiling, fermenting, conditioning, and packaging.",
    "Beer is often served in a variety of glasses, including pint glasses, steins, and tulip glasses.",
    "The carbonation in beer is typically created by natural fermentation or by adding CO2 during packaging.",
    "IPAs (India Pale Ales) are known for their strong hop flavor and higher alcohol content.",
    "Pilsner is a type of pale lager that originated in the Czech Republic.",
    "Stouts are dark, rich beers with roasted malt flavors and a smooth finish.",
    "Porters are similar to stouts but typically have a slightly lighter body and flavor.",
    "Wheat beers are often cloudy and have a refreshing, light taste.",
    "Sours are beers intentionally brewed to have a tart or acidic flavor.",
    "Beer can be paired with food to enhance the flavors of both.",
    "Many people enjoy drinking beer while watching sports, especially during tailgates.",
    "Some breweries experiment with fruit and spices to create seasonal or unique flavors.",
    "Beers with higher alcohol content are often labeled as 'strong ales' or 'imperial' versions.",
    "The color of beer can range from pale yellow to deep brown, depending on the ingredients used.",
    "Pale ales are generally amber to copper in color, with a balanced hop flavor.",
    "A beer's head refers to the foam that forms on top when it is poured.",
    "A good beer should have a thick, lasting head that enhances the drinking experience.",
    "Beer is often served at different temperatures depending on the style, with lagers served colder than ales.",
    "The 'best before' date on a beer label refers to the beer's peak freshness, not an expiration date.",
    "Some beers are brewed with added spices, such as coriander or orange peel.",
    "Beer enthusiasts often participate in beer tastings to explore different styles and flavors.",
    "The alcohol by volume (ABV) of a beer indicates its strength, with higher ABV beers being stronger.",
    "Many cultures have traditional beer styles that reflect their unique brewing history.",
    "Beer is often served in bars, pubs, and restaurants, making it a popular social drink.",
    "Beer can be enjoyed straight from the bottle, in a glass, or in a can.",
    "Lagers are generally lighter in flavor and less hoppy than ales.",
    "Some beers, such as Belgian Tripels, are known for their fruity and spicy aromas.",
    "The perfect pour involves tilting the glass at a 45-degree angle to minimize excess foam.",
    "Beer can be made with a wide variety of additional ingredients, including fruit, spices, and herbs.",
    "Some breweries produce limited-edition beers that are available for a short time.",
    "The term 'session beer' refers to beers with a lower ABV, making them easy to drink over extended periods.",
    "Beer culture varies from country to country, with different traditions, beer styles, and drinking habits.",
    "The concept of a 'beer garden' originated in Germany and is a popular social gathering spot.",
    "Beer is often served at festivals, including Oktoberfest in Germany and the Great American Beer Festival.",
    "The brewing industry has seen a rise in microbreweries and homebrewers experimenting with different styles.",
    "Some beers undergo barrel aging, which imparts unique flavors from the wood.",
    "Beer can be made with a variety of yeasts, which contribute to the flavor and aroma profile.",
    "The first beer cans were introduced in the 1930s, changing the way beer was distributed and consumed.",
    "The process of aging beer can enhance its flavors, especially in styles like stouts and barleywines.",
    "Beer is often enjoyed as a refreshing beverage on hot summer days.",
    "Lager yeast ferments at cooler temperatures than ale yeast, leading to a cleaner flavor profile.",
    "Beer pairs well with a variety of foods, including pizza, burgers, and cheese.",
    "Some beers are brewed with exotic ingredients, such as coffee, chocolate, and vanilla.",
    "Belgian beers are known for their complex flavors, often with hints of fruit, spice, and earthiness.",
    "A brewery’s taproom is where customers can sample and purchase fresh, often exclusive beers.",
    "Beer is an essential part of many cultural and religious traditions worldwide.",
    "Some beers are fermented with wild yeast strains, producing funky or sour flavors.",
    "The concept of 'beer flight' refers to sampling small portions of several beers to compare flavors.",
    "Brewpubs combine breweries and restaurants, offering fresh beer and food in one location.",
    "Beer can be made with various malts, which contribute sweetness, color, and flavor.",
    "Beers can be categorized by their flavor profile, such as hoppy, malty, or fruity.",
    "Some people enjoy creating custom beer blends by mixing different beers together.",
    "Beer can be brewed to be low-carb, gluten-free, or alcohol-free for those with dietary preferences.",
    "Some beer styles, like barleywine, can be aged for several years to improve their flavors.",
    "Beer is commonly served in pints, which hold 16 fluid ounces in the U.S. and 20 fluid ounces in the UK.",
    "The term 'draft beer' refers to beer served directly from a keg rather than from a bottle or can.",
    "Beer drinkers often discuss the 'mouthfeel' of a beer, referring to its texture and body.",
    "A beer’s 'finish' refers to the lingering taste after swallowing.",
    "Beer is made with four main ingredients: water, malt, hops, and yeast.",
    "Some beers feature high hop content, which can impart a piney, floral, or citrusy taste.",
    "The world’s largest beer company is Anheuser-Busch InBev, known for brands like Budweiser and Corona.",
    "Many countries have their own beer laws, which regulate the strength, sale, and distribution of beer.",
    "Beer can be carbonated naturally during fermentation or artificially injected with CO2.",
    "A beer’s bitterness is measured in International Bitterness Units (IBUs), with higher numbers indicating a more bitter taste.",
    "Some beers are brewed with a mix of different malts, resulting in complex flavor profiles.",
    "Beer festivals celebrate the diverse range of beer styles and the craftsmanship of brewers.",
    "The IPA style of beer originated in England and was originally brewed to withstand long voyages to India.",
    "Beer can be paired with dessert, such as chocolate stouts with cake or fruit beers with sorbet.",
    "Many modern breweries use traditional brewing methods combined with innovative techniques.",
    "Beer is known to be a natural source of certain B vitamins, including folic acid.",
    "The most common beer glass shapes are pint glasses, tulip glasses, and snifters.",
    "The term 'lager' comes from the German word 'lagern', meaning 'to store', as lagers are aged at cool temperatures.",
    "Beer is one of the most versatile beverages, available in an almost endless variety of styles.",
    "Some beer aficionados take part in beer rating apps to document and compare their beer experiences.",
    "Many local craft breweries are focused on sustainability and eco-friendly brewing practices.",
    "Some people enjoy brewing their own beer at home, a hobby known as homebrewing.",
    "The craft beer movement in the U.S. has exploded in recent years, with thousands of breweries now in operation.",
    "Some breweries use special filtration techniques to remove yeast and other particles, resulting in clearer beer.",
    "Beer bottles come in different sizes, with the most common being 12 oz, 16 oz, and 22 oz.",
    "In some countries, beer is served alongside traditional pub foods, such as fish and chips or pretzels.",
    "The 'bitter' in bitter beers comes from the hops, which provide balance to the malt sweetness.",
    "Beers that are brewed with fruit are often referred to as fruit beers, which can be sweet or sour.",
    "Seasonal beers are often brewed for specific holidays or times of the year, such as pumpkin ales for fall.",
    "Some beers are brewed with a higher carbonation level, creating a fizzy, effervescent mouthfeel.",
    "Beers with a high malt content tend to have a sweet, bready flavor, while those with higher hop content are more bitter.",
    "The tradition of toasting with beer is thought to come from ancient customs of offering drinks to gods.",
    "The famous 'beer belly' is a result of consuming excess calories from alcohol and carbohydrates.",
    "Beer is sometimes used as an ingredient in cooking, with some dishes like beer-battered fish relying on beer for flavor and texture.",
    "Many beer enthusiasts collect beer cans or bottles as a hobby, often focusing on rare or vintage items.",
    "The popularity of beer continues to rise worldwide, with increasing numbers of people discovering new beer styles and flavors.",
)


word_sets = make_word_sets(sentences)
