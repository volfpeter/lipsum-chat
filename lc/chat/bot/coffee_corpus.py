from .utils import make_word_sets

sentences: tuple[str, ...] = (
    "Coffee is the perfect way to start your day.",
    "A cup of coffee can instantly boost your mood.",
    "Espresso is the base for many popular coffee drinks.",
    "There are countless ways to brew coffee, from French press to pour-over.",
    "Coffee beans are grown in tropical regions around the world.",
    "Dark roast coffee has a stronger, bolder flavor than light roast.",
    "Caffeine is the primary active ingredient in coffee.",
    "Some people prefer their coffee black, while others add milk or sugar.",
    "Drinking coffee can help improve concentration and alertness.",
    "Coffee is a popular beverage for social gatherings.",
    "A latte is a coffee drink made with espresso and steamed milk.",
    "Cappuccinos are topped with a layer of frothed milk.",
    "Coffee is a great way to fuel your productivity during work.",
    "The aroma of freshly brewed coffee can be very comforting.",
    "Cold brew coffee is a smooth and less acidic alternative to hot coffee.",
    "Many people enjoy a cup of coffee after a meal to aid digestion.",
    "Coffee has been enjoyed for centuries, dating back to the 15th century.",
    "The most popular coffee drink in the U.S. is drip coffee.",
    "A macchiato is an espresso drink with a small amount of milk.",
    "Coffee beans are actually the seeds of the coffee fruit.",
    "The word 'coffee' comes from the Arabic word 'qahwa'.",
    "Some people add flavored syrups to their coffee for extra sweetness.",
    "Coffee shops are a popular place to hang out, study, or work.",
    "Coffee has been linked to a lower risk of certain diseases, including Parkinson's.",
    "A good cup of coffee can be a real treat.",
    "There are many different types of coffee beans, including Arabica and Robusta.",
    "In Italy, espresso is an important part of daily life.",
    "Many people drink coffee to stay awake during long drives or study sessions.",
    "Decaffeinated coffee still has a small amount of caffeine.",
    "Coffee is best enjoyed fresh, right after it's brewed.",
    "A perfect espresso shot is often described as having a layer of crema on top.",
    "Some people drink coffee with a sprinkle of cinnamon or cocoa powder for extra flavor.",
    "Coffee has a rich, complex flavor profile that can vary based on its origin.",
    "The caffeine in coffee can help improve physical performance during exercise.",
    "In the morning, coffee often acts as a wake-up call.",
    "Coffee beans are roasted to develop their unique flavor characteristics.",
    "A flat white is a coffee drink similar to a latte, but with less foam.",
    "Coffee is often enjoyed with a sweet pastry or dessert.",
    "Coffee has become a global cultural phenomenon.",
    "The coffee industry is worth billions of dollars worldwide.",
    "Coffee can help you stay alert during a long workday.",
    "Some people love the ritual of brewing their own coffee every morning.",
    "A French press allows for a full-bodied and rich cup of coffee.",
    "Coffee is often a key ingredient in desserts like tiramisu and coffee cake.",
    "Some coffee drinkers swear by the health benefits of black coffee.",
    "Iced coffee is a refreshing way to enjoy coffee during the summer months.",
    "Caffeine is known to help with focus and mental clarity.",
    "Coffee can be a great conversation starter when meeting new people.",
    "A good cup of coffee can turn an ordinary moment into something special.",
    "Coffee is enjoyed by people of all ages around the world.",
    "Some coffee shops offer unique and creative coffee drinks.",
    "Drinking coffee in moderation can be part of a healthy lifestyle.",
    "The best coffee beans are often grown at high altitudes.",
    "Coffee is a key component of many traditional breakfast routines.",
    "Coffee culture has evolved over the years, with many new trends emerging.",
    "Some coffee drinkers prefer their coffee strong and bold, while others prefer it mild.",
    "Coffee is often used to make various coffee-based cocktails.",
    "The caffeine in coffee can help improve reaction time and coordination.",
    "Many people enjoy a cup of coffee to relax and unwind after a long day.",
    "Coffee can be a great companion while reading a book or working on a project.",
    "Many people find that coffee helps them feel more awake and alert in the morning.",
    "Coffee is often seen as a symbol of energy and productivity.",
    "Coffee beans undergo a complex process of roasting to bring out their flavors.",
    "A coffee grinder is an essential tool for fresh coffee enthusiasts.",
    "Coffee is sometimes paired with chocolate for a delicious combination.",
    "Espresso has a rich, concentrated flavor that many coffee lovers enjoy.",
    "The coffee bean's journey from farm to cup involves many steps.",
    "Iced coffee can be made at home by brewing coffee and chilling it.",
    "Many people enjoy drinking coffee while people-watching at cafés.",
    "Coffee is a source of antioxidants, which can be beneficial to your health.",
    "Drinking coffee can improve mental performance, especially in the morning.",
    "Coffee can be customized in many ways with various types of milk and sweeteners.",
    "A pour-over coffee maker provides control over the brewing process.",
    "Coffee consumption is a daily ritual for millions of people worldwide.",
    "Coffee's popularity has inspired countless cafés and specialty coffee shops.",
    "A coffee mug can be a comforting object that brings warmth and happiness.",
    "Coffee is often enjoyed as a midday pick-me-up.",
    "The coffee industry continues to innovate with new brewing methods and technologies.",
    "Coffee can be enjoyed in both hot and cold forms, depending on your preference.",
    "Many people love the ritual of sipping coffee while starting their day.",
    "Coffee has a complex flavor that varies depending on its roast and origin.",
    "Some coffee aficionados are always searching for the perfect cup of coffee.",
    "A well-made cup of coffee can be a work of art in itself.",
    "Drinking coffee can help you power through tough tasks or long hours of work.",
    "Coffee is a social drink, often shared with friends or colleagues.",
    "Coffee beans are sometimes blended to create unique flavor profiles.",
    "Some people prefer to drink their coffee with a splash of cream or milk.",
    "Coffee lovers enjoy experimenting with different brewing techniques and methods.",
    "The caffeine in coffee can provide a temporary energy boost.",
    "In many cultures, coffee is enjoyed with a sense of ceremony and tradition.",
    "Some people drink coffee to help with focus during study sessions or work meetings.",
    "The rich, bold flavor of coffee can provide a comforting sense of warmth.",
    "Many people find that drinking coffee helps them feel more productive and energetic.",
    "Coffee is often served with a variety of pastries or snacks at cafés.",
    "Some people prefer to drink their coffee black, while others enjoy adding flavors like vanilla or caramel.",
    "Coffee has a way of bringing people together for conversation and bonding.",
    "Caffeine sensitivity varies from person to person, with some people able to handle more than others.",
    "Coffee is sometimes used in desserts like ice cream or cakes for its rich flavor.",
    "A good coffee grinder is essential for ensuring that your coffee is ground to the right consistency.",
    "The coffee plant requires a specific climate and altitude to grow well.",
    "Coffee beans can have a range of flavors, from fruity to nutty to chocolaty.",
    "In many parts of the world, coffee is an integral part of the daily routine.",
    "Coffee is a drink that people often enjoy while relaxing or working on projects.",
    "Many coffee lovers appreciate the ritual of brewing their coffee just the way they like it.",
    "Coffee is known for its ability to provide a boost of energy and alertness.",
    "Espresso is often used as the base for other popular coffee drinks like lattes and cappuccinos.",
    "A well-made cup of coffee can be a satisfying and enjoyable experience.",
)


word_sets = make_word_sets(sentences)
